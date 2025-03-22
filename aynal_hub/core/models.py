
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Project(models.Model):
    # Basic Information
    title = models.CharField(
        max_length=200,
        help_text="The title of the project.",
        validators=[MinLengthValidator(5), MaxLengthValidator(200)]
    )
    short_description = models.CharField(
        max_length=300,
        help_text="A short description of the project (max 300 characters).",
        validators=[MinLengthValidator(10), MaxLengthValidator(300)]
    )
    detailed_description = models.TextField(
        help_text="A detailed description of the project."
    )
    image = models.ImageField(
        upload_to='projects/',
        help_text="Upload a high-quality image or screenshot of the project."
    )
    thumbnail = models.ImageField(
        upload_to='projects/thumbnails/',
        help_text="Upload a smaller thumbnail image for the project.",
        blank=True,
        null=True
    )
    url = models.URLField(
        blank=True,
        help_text="The live URL of the project (if applicable)."
    )
    github_repo = models.URLField(
        blank=True,
        help_text="The GitHub repository URL of the project (if applicable)."
    )

    # Project Metadata
    start_date = models.DateField(
        help_text="The start date of the project."
    )
    end_date = models.DateField(
        blank=True,
        null=True,
        help_text="The end date of the project (if completed)."
    )
    is_active = models.BooleanField(
        default=False,
        help_text="Is the project currently active?"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Should this project be featured on the homepage?"
    )

    # Technologies Used
    technologies_used = models.CharField(
        max_length=500,
        help_text="Comma-separated list of technologies used in the project.",
        blank=True
    )

    # Client/Organization Information
    client_name = models.CharField(
        max_length=200,
        help_text="The name of the client or organization (if applicable).",
        blank=True
    )
    client_url = models.URLField(
        blank=True,
        help_text="The URL of the client or organization (if applicable)."
    )

    # SEO and Visibility
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="A URL-friendly slug for the project.",
        blank=True
    )
    meta_description = models.CharField(
        max_length=300,
        help_text="Meta description for SEO (max 300 characters).",
        blank=True
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-is_featured', '-start_date']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

from django.utils.text import slugify
from django.urls import reverse

class BlogPost(models.Model):
    # Basic Information
    title = models.CharField(
        max_length=200,
        help_text="The title of the blog post.",
        validators=[MinLengthValidator(5), MaxLengthValidator(200)]
    )
    content = models.TextField(
        help_text="The main content of the blog post."
    )
    excerpt = models.CharField(
        max_length=300,
        help_text="A short excerpt or summary of the blog post (max 300 characters).",
        validators=[MinLengthValidator(10), MaxLengthValidator(300)]
    )
    cover_image = models.ImageField(
        upload_to='blog/covers/',
        help_text="Upload a cover image for the blog post.",
        blank=True,
        null=True
    )
    thumbnail = models.ImageField(
        upload_to='blog/thumbnails/',
        help_text="Upload a smaller thumbnail image for the blog post.",
        blank=True,
        null=True
    )

    # SEO and Visibility
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="A URL-friendly slug for the blog post.",
        blank=True
    )
    meta_description = models.CharField(
        max_length=300,
        help_text="Meta description for SEO (max 300 characters).",
        blank=True
    )
    is_published = models.BooleanField(
        default=False,
        help_text="Is the blog post published and visible to the public?"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Should this blog post be featured on the homepage?"
    )

    # Author Information
    author_name = models.CharField(
        max_length=200,
        help_text="The name of the author of the blog post.",
        blank=True
    )
    author_bio = models.TextField(
        help_text="A short bio of the author.",
        blank=True
    )
    author_image = models.ImageField(
        upload_to='blog/authors/',
        help_text="Upload an image of the author.",
        blank=True,
        null=True
    )

    # Categories and Tags
    category = models.CharField(
        max_length=100,
        help_text="The category of the blog post.",
        blank=True
    )
    tags = models.CharField(
        max_length=500,
        help_text="Comma-separated list of tags for the blog post.",
        blank=True
    )

    # Timestamps
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text="The date when the blog post was published."
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.is_published and not self.published_date:
            self.published_date = models.DateTimeField(auto_now_add=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-is_featured', '-published_date']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"    


       

#tutorial sections

class Tutorial(models.Model):
    # Basic Information
    title = models.CharField(
        max_length=200,
        help_text="The title of the tutorial.",
        validators=[MinLengthValidator(5), MaxLengthValidator(200)]
    )
    short_description = models.CharField(
        max_length=300,
        help_text="A short description of the tutorial (max 300 characters).",
        validators=[MinLengthValidator(10), MaxLengthValidator(300)]
    )
    content = models.TextField(
        help_text="The main content of the tutorial."
    )
    cover_image = models.ImageField(
        upload_to='tutorials/covers/',
        help_text="Upload a cover image for the tutorial.",
        blank=True,
        null=True
    )
    thumbnail = models.ImageField(
        upload_to='tutorials/thumbnails/',
        help_text="Upload a smaller thumbnail image for the tutorial.",
        blank=True,
        null=True
    )

    # SEO and Visibility
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="A URL-friendly slug for the tutorial.",
        blank=True
    )
    meta_description = models.CharField(
        max_length=300,
        help_text="Meta description for SEO (max 300 characters).",
        blank=True
    )
    is_published = models.BooleanField(
        default=False,
        help_text="Is the tutorial published and visible to the public?"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Should this tutorial be featured on the homepage?"
    )

    # Author Information
    author_name = models.CharField(
        max_length=200,
        help_text="The name of the author of the tutorial.",
        blank=True
    )
    author_bio = models.TextField(
        help_text="A short bio of the author.",
        blank=True
    )
    author_image = models.ImageField(
        upload_to='tutorials/authors/',
        help_text="Upload an image of the author.",
        blank=True,
        null=True
    )

    # Categories and Tags
    category = models.CharField(
        max_length=100,
        help_text="The category of the tutorial.",
        blank=True
    )
    tags = models.CharField(
        max_length=500,
        help_text="Comma-separated list of tags for the tutorial.",
        blank=True
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text="The date when the tutorial was published."
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.is_published and not self.published_date:
            self.published_date = models.DateTimeField(auto_now_add=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-is_featured', '-published_date']
        verbose_name = "Tutorial"
        verbose_name_plural = "Tutorials" 