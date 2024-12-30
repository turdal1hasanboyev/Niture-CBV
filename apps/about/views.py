from django.shortcuts import render, redirect

from django.views import View

from .models import About
from apps.common.models import SubEmail


class AboutView(View):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        about = About.objects.filter(is_active=True, id=1).first()
        context = {
            'about': about,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        sub_email = request.POST.get('sub_email')

        if sub_email:
            SubEmail.objects.create(email=sub_email)
            return redirect('about')

about_as_view = AboutView.as_view()
