from django.db import models
from django.contrib.auth import  get_user_model
User = get_user_model()


class Project(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="projects"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
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
    link = models.URLField(max_length=500, blank=True, null=True)
    languages = models.JSONField(
        default=list,
        help_text="List of programming languages used (e.g., ['Python', 'JavaScript'])"
    )
    frameworks = models.JSONField(
        default=list,
        help_text="List of frameworks or libraries used (e.g., ['Django', 'React'])"
    )

    def __str__(self):
        return self.title
