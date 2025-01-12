# Generated by Django 5.1.3 on 2025-01-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_textgen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AIProposalResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('tags', models.JSONField()),
                ('fixed_price', models.CharField(max_length=50)),
                ('est_budget', models.CharField(max_length=50)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
