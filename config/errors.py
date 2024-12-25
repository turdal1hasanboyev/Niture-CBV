from django.views import View

from django.shortcuts import render


class PageNotFoundView(View):
    def get(self, request, *args, **kwargs):
        return render(request, '404.html', status=404)
    
page_not_found_as_view = PageNotFoundView.as_view()
