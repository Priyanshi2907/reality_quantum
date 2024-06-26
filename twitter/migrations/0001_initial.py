# Generated by Django 5.0.4 on 2024-04-30 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=100)),
                ('created_at', models.CharField(max_length=100)),
                ('tweet_link', models.URLField(blank=True, null=True)),
                ('user_screen_name', models.CharField(blank=True, max_length=100, null=True)),
                ('user_location', models.CharField(blank=True, max_length=100, null=True)),
                ('user_followers_count', models.IntegerField(default=0)),
                ('user_friends_count', models.IntegerField(blank=True, null=True)),
                ('retweet_count', models.IntegerField(blank=True, null=True)),
                ('favorite_count', models.IntegerField(blank=True, null=True)),
                ('lang', models.CharField(blank=True, max_length=40, null=True)),
                ('reach', models.IntegerField(blank=True, null=True)),
                ('hashtags', models.CharField(blank=True, max_length=500, null=True)),
                ('organization', models.CharField(blank=True, max_length=500, null=True)),
                ('person', models.CharField(blank=True, max_length=500, null=True)),
                ('sentiment', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
