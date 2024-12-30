from django.shortcuts import render, redirect

from django.views import View

from .models import Blog
from apps.common.models import SubEmail


class BlogView(View):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.filter(is_active=True).order_by('id')[:4]
        return render(request, 'blog.html', {'blogs': blogs})
    
    def post(self, request, *args, **kwargs):
        url = request.build_absolute_uri()
        sub_email = request.POST.get('sub_email')
        if sub_email:
            subs_email = SubEmail(
                email=sub_email,
            )
            subs_email.save()
            return redirect(url)
