from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name='index'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^index/product_details/(?P<productcode>.+)/$', views.product_details, name='product_details'),
    url(r'^product_details/(?P<productcode>.+)/$', views.product_details, name='product_details'),
    url(r'^products/$', views.products, name='products'),
    url(r'^register/$', views.register, name='register'),
<<<<<<< HEAD
    url(r'^search/$', views.search, name='search'),
=======
    # url(r'^quer', views.search, name = 'search'),
>>>>>>> 0e8581563a4da58d567bbeb2ef0602e6244234ff
]
