from rest_framework import serializers
from .models import *

class WebScrapingJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebScrapingJob
        fields = ['title', 'description', 'tags', 'fixed_price', 'est_budget', 'posted_date']
        read_only_fields = ['posted_date']


class AIProposalResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIProposalResponse
        fields = '__all__'
