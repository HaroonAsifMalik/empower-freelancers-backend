from django.db import models
from accounts.models import CustomUser


class Project(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="projects"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    generated_proposal = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("Ongoing", "Ongoing"),
            ("Completed", "Completed"),
        ],
        default="Pending",
    )

    def __str__(self):
        return self.title
