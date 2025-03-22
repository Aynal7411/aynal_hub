from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request,"landing.html")
 #projects sections
from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    """
    View to list all projects.
    """
    projects = Project.objects.filter(is_active=True).order_by('-is_featured', '-start_date')
    context = {
        'projects': projects,
    }
    return render(request, 'project_list.html', context)

def project_detail(request, slug):
    """
    View to display details of a single project.
    """
    project = get_object_or_404(Project, slug=slug, is_active=True)
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)

#Blog sections

from .models import BlogPost

def blog_post_list(request):
    """
    View to list all blog posts.
    """
    posts = BlogPost.objects.filter(is_published=True).order_by('-is_featured', '-published_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog_post_list.html', context)

def blog_post_detail(request, slug):
    """
    View to display details of a single blog post.
    """
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    context = {
        'post': post,
    }
    return render(request, 'blog_post_detail.html', context)

def consult_page(request):
    return render(request,'consult.html')



from .models import Tutorial

def tutorial_list(request):
    """
    View to list all tutorials.
    """
    tutorials = Tutorial.objects.filter(is_published=True).order_by('-is_featured', '-published_date')
    context = {
        'tutorials': tutorials,
    }
    return render(request, 'tutorial_list.html', context)

def tutorial_detail(request, slug):
    """
    View to display details of a single tutorial.
    """
    tutorial = get_object_or_404(Tutorial, slug=slug, is_published=True)
    context = {
        'tutorial': tutorial,
    }
    return render(request, 'tutorial_detail.html', context)