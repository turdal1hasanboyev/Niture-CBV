from django.shortcuts import render, redirect

from django.views import View

from .models import Contact
from apps.common.models import SubEmail


class ContactView(View):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        url = request.build_absolute_uri()

        sub_email = request.POST.get('sub_email')
        
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        if sub_email:
            SubEmail.objects.create(email=sub_email)
            return redirect(url)
        
        if name and message and email and phone_number:
            contact = Contact()
            contact.name = name
            contact.email = email
            contact.phone = phone_number
            contact.message = message
            contact.save()
            return redirect('contact')

contact_as_view = ContactView.as_view()
