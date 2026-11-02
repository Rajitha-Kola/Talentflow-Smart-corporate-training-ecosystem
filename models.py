from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Training(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    trainer_name = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    duration = models.CharField(max_length=50)  # Example: "2 days", "1 week"
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
    

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who enrolls
    course = models.ForeignKey(Training, on_delete=models.CASCADE)  # The course being enrolled in
    enrollment_date = models.DateTimeField(auto_now_add=True)  # Automatically set when enrolled

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"