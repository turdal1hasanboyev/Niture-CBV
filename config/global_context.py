from apps.product.models import Category


def object(request):
    categories = Category.objects.filter(is_active=True).order_by('name')[:3]
    context = {}
    context['categories'] = categories
    return context
