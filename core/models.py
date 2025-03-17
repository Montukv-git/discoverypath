from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    education = models.CharField(max_length=100)  # e.g., "B.Sc Physics"
    interests = models.JSONField()  # e.g., ["Tech", "Teaching"]

    def __str__(self):
        return f"{self.user.username}'s Profile"

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.JSONField()  # e.g., {"Analytical Thinking": 8, "Communication": 6}
    careers = models.JSONField()  # e.g., [{"name": "Data Analyst", "desc": "...", "earnings": "₹50K"}]
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Result"