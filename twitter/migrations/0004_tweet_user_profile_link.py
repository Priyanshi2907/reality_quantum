# Generated by Django 5.0.4 on 2024-04-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_tweet_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='user_profile_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
