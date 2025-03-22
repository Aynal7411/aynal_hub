# Generated by Django 5.1.7 on 2025-03-22 04:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the blog post.', max_length=200, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(200)])),
                ('content', models.TextField(help_text='The main content of the blog post.')),
                ('excerpt', models.CharField(help_text='A short excerpt or summary of the blog post (max 300 characters).', max_length=300, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(300)])),
                ('cover_image', models.ImageField(blank=True, help_text='Upload a cover image for the blog post.', null=True, upload_to='blog/covers/')),
                ('thumbnail', models.ImageField(blank=True, help_text='Upload a smaller thumbnail image for the blog post.', null=True, upload_to='blog/thumbnails/')),
                ('slug', models.SlugField(blank=True, help_text='A URL-friendly slug for the blog post.', max_length=200, unique=True)),
                ('meta_description', models.CharField(blank=True, help_text='Meta description for SEO (max 300 characters).', max_length=300)),
                ('is_published', models.BooleanField(default=False, help_text='Is the blog post published and visible to the public?')),
                ('is_featured', models.BooleanField(default=False, help_text='Should this blog post be featured on the homepage?')),
                ('author_name', models.CharField(blank=True, help_text='The name of the author of the blog post.', max_length=200)),
                ('author_bio', models.TextField(blank=True, help_text='A short bio of the author.')),
                ('author_image', models.ImageField(blank=True, help_text='Upload an image of the author.', null=True, upload_to='blog/authors/')),
                ('category', models.CharField(blank=True, help_text='The category of the blog post.', max_length=100)),
                ('tags', models.CharField(blank=True, help_text='Comma-separated list of tags for the blog post.', max_length=500)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('published_date', models.DateTimeField(blank=True, help_text='The date when the blog post was published.', null=True)),
            ],
            options={
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
                'ordering': ['-is_featured', '-published_date'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the project.', max_length=200, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(200)])),
                ('short_description', models.CharField(help_text='A short description of the project (max 300 characters).', max_length=300, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(300)])),
                ('detailed_description', models.TextField(help_text='A detailed description of the project.')),
                ('image', models.ImageField(help_text='Upload a high-quality image or screenshot of the project.', upload_to='projects/')),
                ('thumbnail', models.ImageField(blank=True, help_text='Upload a smaller thumbnail image for the project.', null=True, upload_to='projects/thumbnails/')),
                ('url', models.URLField(blank=True, help_text='The live URL of the project (if applicable).')),
                ('github_repo', models.URLField(blank=True, help_text='The GitHub repository URL of the project (if applicable).')),
                ('start_date', models.DateField(help_text='The start date of the project.')),
                ('end_date', models.DateField(blank=True, help_text='The end date of the project (if completed).', null=True)),
                ('is_active', models.BooleanField(default=False, help_text='Is the project currently active?')),
                ('is_featured', models.BooleanField(default=False, help_text='Should this project be featured on the homepage?')),
                ('technologies_used', models.CharField(blank=True, help_text='Comma-separated list of technologies used in the project.', max_length=500)),
                ('client_name', models.CharField(blank=True, help_text='The name of the client or organization (if applicable).', max_length=200)),
                ('client_url', models.URLField(blank=True, help_text='The URL of the client or organization (if applicable).')),
                ('slug', models.SlugField(blank=True, help_text='A URL-friendly slug for the project.', max_length=200, unique=True)),
                ('meta_description', models.CharField(blank=True, help_text='Meta description for SEO (max 300 characters).', max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['-is_featured', '-start_date'],
            },
        ),
    ]
