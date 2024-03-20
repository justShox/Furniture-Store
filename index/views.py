from django.shortcuts import render, redirect


# Create your views here.


def home(request):
    return render(request, 'index2.html')


def blog(request):
    return render(request, 'blog.html')


def blog_detail(request):
    return render(request, 'blog-detail.html')


def contact_us(request):
    return render(request, 'contact-us.html')


def detail(request):
    return render(request, 'detail.html')


def listing_grid(request):
    return render(request, 'listing-grid.html')


def shoppingcart(request):
    return render(request, 'shoppingcart.html')


def page_not_found(request):
    return render(request, '404.html')
