from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Banner, Product, Review
from ..common.models import SubEmail
from apps.contact.models import Contact


class HomePageView(View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        banners = Banner.objects.filter(is_active=True).order_by('-id')[:3]
        products = Product.objects.filter(is_active=True).order_by('-id')[:3]
        context = {}
        context['banners'] = banners
        context['products'] = products
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        url = request.build_absolute_uri()
        sub_email = request.POST.get('sub_email')
        name = request.POST.get('name') # xavfsiz
        email = request.POST['email'] # xavfsiz emas (majburiy bolishi kerak)
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        if sub_email:
            SubEmail.objects.create(email=sub_email)
            return redirect(url)
        if name and email and phone_number and message:
            contact = Contact.objects.create(
                name=name,
                email=email,
                phone=phone_number,
                message=message,
            )
            contact.save()
            return redirect('/')
    
home_page_as_view = HomePageView.as_view()


class ProductView(View):
    template_name = 'product.html'
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(is_active=True).order_by('-id')[:6]
        context = {
            'products': products,
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        sub_email = SubEmail()
        sub_email.email = request.POST.get('sub_email')
        sub_email.save()
        return redirect(request.build_absolute_uri())

product_as_view = ProductView.as_view()


class ProductDetailView(View):
    template_name = 'product_detail.html'

    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Product, is_active=True, slug__exact=slug)
        product.views += 1
        product.save()
        reviews = Review.objects.filter(is_active=True, product__slug__exact=product.slug)

        context = {
            'product': product,
            'reviews': reviews,
        }

        return render(request=request, template_name=self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        url = request.build_absolute_uri()
        sub_email = request.POST.get('sub_email')
        SubEmail.objects.create(email=sub_email)
        return redirect(url)
