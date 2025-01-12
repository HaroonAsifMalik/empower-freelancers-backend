from django.db import models

class WebScrapingJob(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.JSONField()
    fixed_price = models.CharField(max_length=50)
    est_budget = models.CharField(max_length=50)
    posted_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title




class AIProposalResponse(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.JSONField()
    fixed_price = models.CharField(max_length=50)
    est_budget = models.CharField(max_length=50)
    posted_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

