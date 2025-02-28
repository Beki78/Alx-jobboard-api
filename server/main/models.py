from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Job(models.Model):

    class EmploymentType(models.TextChoices):
        FULL_TIME = "FT", "Full Time"
        PART_TIME = "PT", "Part Time"
        CONTRACT = "C", "Contract"
        FREELANCE = "F", "Freelance"
        INTERN = "I", "Intern"

    class ExperienceLevel(models.TextChoices):
        BEGINNER = "E", "Entry Level"
        INTERMEDIATE = "M", "Mid Level"
        ADVANCED = "S", "Senior Level"

    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(
        upload_to="logos/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])],
    )
    location = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)
    salary_range = models.CharField(max_length=50)
    employmentType = models.CharField(max_length=2, choices=EmploymentType.choices, default=EmploymentType.FULL_TIME)
    experienceLevel = models.CharField(max_length=1, choices=ExperienceLevel.choices, default=ExperienceLevel.BEGINNER)

class Application(models.Model):
  jobId = models.ForeignKey(Job, on_delete=models.CASCADE)
  resume = models.CharField(max_length=1000)
  appliedAt = models.DateTimeField(auto_now_add=True)
  postedAt = models.DateTimeField(auto_now_add=True)
  userID = models.ForeignKey(User, on_delete=models.CASCADE)
