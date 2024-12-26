from django.shortcuts import render
from django.views import View


class HomePageView(View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
    
home_page_as_view = HomePageView.as_view()
