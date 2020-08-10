from .views import *
from django.urls import *
app_name='home'

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('product/<slug>',ItemView.as_view(),name='product'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('subcategory/<slug>', SubcategoryView.as_view(), name='subcategory'),
    path('search', SearchView.as_view(), name='search'),
    path('signup', Signup, name='signup'),
    path('login', login, name='login'),
    path('cart', cart, name='cart'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
    # path('contact', ContactView.as_view(), name='contact'),
    path('contact', contact, name='contact'),

]