# Generated by Django 5.0.4 on 2024-04-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_influencers'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
