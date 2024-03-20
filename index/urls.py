from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blog', views.blog, name='blog'),
    path('blog-detail', views.blog_detail, name='blog-detail'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('detail', views.detail, name='detail'),
    path('listing-grid', views.listing_grid, name='listing-grid'),
    path('shoppingcart', views.shoppingcart, name='shoppingcart'),
    path('404', views.page_not_found, name='404'),
]
