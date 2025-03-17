from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, TestResult
from .ai_logic import generate_test_questions, calculate_results  # We'll define this next
import json
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from django.http import HttpResponse
import io

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        education = request.POST.get('education')
        interests = request.POST.getlist('interests')
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, education=education, interests=interests)
            login(request, user)
            return redirect('test')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def test(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    profile = request.user.profile
    if request.method == 'POST':
        answers = {k: v for k, v in request.POST.items() if k.startswith('q')}
        skills, careers = calculate_results(profile.education, profile.interests, answers)
        TestResult.objects.create(user=request.user, skills=skills, careers=careers)
        return redirect('results')
    questions = generate_test_questions(profile.education, profile.interests)
    return render(request, 'test.html', {'questions': questions})

def results(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    result = TestResult.objects.filter(user=request.user).latest('created_at')
    return render(request, 'results.html', {'skills': result.skills, 'careers': result.careers})

def download_pdf(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    result = TestResult.objects.filter(user=request.user).latest('created_at')
    
    # Generate PDF
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = [Paragraph(f"Skills: {json.dumps(result.skills)}", style=None),
             Paragraph(f"Careers: {json.dumps(result.careers)}", style=None)]
    doc.build(story)
    buffer.seek(0)
    
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="YourPath.pdf"'
    return response