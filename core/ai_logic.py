def generate_test_questions(education, interests):
    # Dummy questions; replace with GPT API calls later
    questions = [
        {"id": "q1", "text": "Do you enjoy solving complex problems?", "type": "yesno"},
        {"id": "q2", "text": "Would you rather build or explain?", "type": "choice", "options": ["Build", "Explain"]},
        {"id": "q3", "text": "How comfortable are you with numbers?", "type": "scale", "options": range(1, 6)},
    ]
    return questions

def calculate_results(education, interests, answers):
    # Dummy logic; refine with AI later
    skills = {"Analytical Thinking": 8, "Communication": 6, "Technical Aptitude": 7}
    careers = [
        {"name": "Data Analyst", "desc": "Use data to solve problems", "earnings": "₹50K"},
        {"name": "Tech Creator", "desc": "Make videos on tech", "earnings": "₹1L+"},
    ]
    return skills, careers