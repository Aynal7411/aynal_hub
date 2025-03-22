from django.urls import path
from .views import landing_page,project_list,project_detail,blog_post_list,blog_post_detail,consult_page,tutorial_list,tutorial_detail

urlpatterns = [
    
    path('projects/', project_list, name='project_list'),
    path('projects/<slug:slug>/', project_detail, name='project_detail'),

    path('blog/',blog_post_list, name='blog_post_list'),
    path('blog/<slug:slug>/',blog_post_detail, name='blog_post_detail'),
    path('consult/',consult_page,name="consult_page"),

    path('tutorials/', tutorial_list, name='tutorial_list'),
    path('tutorials/<slug:slug>/', tutorial_detail, name='tutorial_detail'),
]
