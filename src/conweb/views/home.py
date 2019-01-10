
from django.shortcuts import render

from mezzanine.blog.models import BlogPost


def home(request):
    blog_posts = BlogPost.objects.published(for_user=request.user)
    return render(request, "index.html", {"blog_posts": blog_posts})
