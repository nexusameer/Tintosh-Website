# Generated by Django 5.0.6 on 2024-05-16 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('happy_clients', models.CharField(max_length=200)),
                ('project_completed', models.CharField(max_length=200)),
                ('positive_feedback', models.TextField()),
                ('years_of_experience', models.IntegerField()),
                ('address', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('facebook_profile', models.URLField(blank=True, null=True)),
                ('insta_profile', models.URLField(blank=True, null=True)),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='clients/')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('project_category', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='team/')),
                ('facebook_profile', models.URLField(blank=True, null=True)),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('github_profile', models.URLField(blank=True, null=True)),
                ('twitter_profile', models.URLField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
