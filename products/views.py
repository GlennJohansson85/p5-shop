from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from category.models import Category
from cart.models import CartItem
from django.db.models import Q

from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from orders.models import OrderProduct
from django.http import HttpResponse
from django.contrib import messages


def products(request, category_slug=None):
    '''
    Displays products based on the selected category slug.
    If no category is selected, displays all available products paginated.
    '''
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, category_slug, product_slug):
    '''
    Displays the details of a single product identified by its category slug
    and product slug.
    '''
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()

    except Exception as e:
        raise e

    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user,product_id=single_product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None

    else:
        orderproduct = None

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        'orderproduct': orderproduct,
    }
    return render(request, 'products/product_detail.html', context)


def search(request):
    '''
    Searches for products based on the provided keyword
    in the request GET parameters.
    '''
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']

        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'products/products.html', context)
