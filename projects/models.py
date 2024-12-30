from django.db import models

class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('Ongoing', 'Ongoing'),
            ('Completed', 'Completed'),
        ],
        default='Pending',
    )

    def __str__(self):
        return self.title
