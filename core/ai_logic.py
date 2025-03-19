from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Set key in environment variables

def generate_test_questions(education, interests):
    prompt = f"Generate 5 short, adaptive questions for a student with education '{education}' and interests {interests} to assess skills like Analytical Thinking, Communication, and Creativity. Return as JSON."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    return json.loads(response.choices[0].message.content)

def calculate_results(education, interests, answers):
    prompt = f"Based on education '{education}', interests {interests}, and test answers {answers}, calculate 5 skills (rated out of 10) and suggest 5 career paths (traditional and unconventional) with descriptions and earnings in INR. Return as JSON."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    data = json.loads(response.choices[0].message.content)
    return data["skills"], data["careers"]