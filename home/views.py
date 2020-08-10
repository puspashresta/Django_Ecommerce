from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

# Create your views here.

from home.models import *
from django.views.generic.base import View, View


class BaseView(View):
    template_views={}
    template_views['categories'] = Category.objects.all()
    template_views['subcategories'] = Subcategory.objects.all()

class HomeView(BaseView):
    def get(self,request):
        self.template_views['items']=Item.objects.filter(front=True)

        self.template_views['sliders'] = Slider.objects.all()
        self.template_views['banners'] = Banner.objects.all()
        self.template_views['special_offers']=Item.objects.filter(special_offer=True)

        return render(request,'index.html',self.template_views)

class ItemView(BaseView):
    def get(self, request,slug):
        self.template_views['view_items'] = Item.objects.filter(slug=slug)
        return render(request,'single.html',self.template_views)

class CategoryView(BaseView):
    def get(self,request,slug):
        category_id = Category.objects.get(slug = slug).id
        self.template_views['category_item']=Item.objects.filter(category_id=category_id)

        return render(request, 'category.html', self.template_views)


class SubcategoryView(BaseView):
    def get(self,request,slug):
        subcategory_id=Subcategory.objects.get(slug = slug).id
        self.template_views['subcategory_item']=Item.objects.filter(subcategory_id=subcategory_id)

        return render(request,'subcategory.html',self.template_views)

class SearchView(BaseView):
    def get(self,request):
        query = request.GET.get('search','None')
        if not None:
            self.template_views['search_results'] = Item.objects.filter(title__icontains = query)

        self.template_views['Search_for'] = query

        return render(request, 'search.html', self.template_views)

def Signup(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username= username).exists():
                messages.error(request, "Try others, this usernamae already exist!!!")
                return redirect('home:signup')

            elif User.objects.filter(email= email).exists():
                messages.error(request, "The email is already exist!!")
                return redirect('home:signup')

            else:
                user=User.objects.create_user(
                    username = username,
                    email = email,
                    password = password
                )
                user.save()
                messages.success(request, "you are signed in with us!!")
                return redirect('home:login')

        else:
            messages.error(request, "Password not matches!!")
            return redirect('home:signup')

    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Password not matches!!")
            return redirect('home:login')


    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def cart(request):
    views={}
    views['carts']=Cart.objects.filter(checkout=False, user = request.user)

    return render(request, 'cart.html', views)

# @login_required
def add_to_cart(request):
    if request.method == "POST":
        slug = request.POST['slug']
        title = request.POST['title']
        image = request.POST['image']
        description = request.POST['description']
        price = request.POST['price']

        if  Cart.objects.filter(slug=slug).exists():
            quantity = Cart.objects.get(slug=slug).quantity
            Cart.objects.filter(slug=slug).update(quantity= quantity+1)

            return redirect('home:cart')
        else:
            my_cart = Cart.objects.create(
                user=request.user,
                slug=slug,
                title=title,
                image=image,
                description=description,
                price= price
        )
        my_cart.save()
        return redirect('home:cart')
    else:
        return redirect('/')


def delete_cart(request,slug):
    if Cart.objects.filter(slug=slug).exists():
        quantity = Cart.objects.get(slug=slug).quantity
        Cart.objects.filter(slug=slug).delete()
        messages.success(request,"The item is deleted")

        return redirect('home:cart')
    else:

        return redirect('home:cart')
        messages.error(request, "Item is not exist in your cart")

# class ContactView(BaseView):
#
#     def get(self, request):

        # if self.request.method == "POST":
        #     self.name = self.request.POST['name'],
        #     self.subject = self.request.POST['subject'],
        #     self.email = self.request.POST['email'],
        #     self.message = self.request.POST['message']
        #     contact= Contact.objects.create(
        #         name = self.name,
        #         subject = self.subject,
        #         email = self.email,
        #         message = self.message
        #     )
        #
        #     contact.send()
        #
        #     email = EmailMessage(
        #         'New Message',
        #         f'<b>{self.name}</b> is sending you message that <i>{self.message}</i>',
        #         self.email,
        #         ['puspa0sh@gmail.com']
        #     )
        #     email.send()
        #
        #     messages.success(request, "Successfully sent messages!")
        #     return redirect('home:contact')

        # return render(request, "contact.html")   class based garda message send vayena meroma so i did on function based way
def contact(request):
    if request.method == "POST":
        name = request.POST['name'],
        subject = request.POST['subject'],
        email = request.POST['email'],
        message = request.POST['message']
        contact = Contact.objects.create(
            name=name,
            subject=subject,
            email=email,
            message=message
        )

        contact.save()

        email = EmailMessage(
            'New Message',
            f'<html><body><b>{name}</b> is sending you message that <i>{message}</body></html></i>',
            email,
            ['puspa0sh@gmail.com']
        )
        email.content_subtype='html'
        email.send()

        messages.success(request, "Successfully sent messages!")
        return redirect('home:contact')

    # else:
    #     messages.error(request, "Error in sending messages!")
    #     return redirect('home:contact')

    return render(request, "contact.html")


# for rREST API

from rest_framework import viewsets, generics
from home.serializers import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializers

# FOR FILTER

class ItemFilterListView(generics.ListAPIView):
    serializer_class = ItemSerializers
    queryset = Item.objects.all()

    filter_backends = (DjangoFilterBackend,OrderingFilter,SearchFilter)

    filter_fields = ['id','title','price','discounted_price','stock','brand','labels','special_offer','category','subcategory']

    ordering_fields = ['id','title','price','labels']

    search_fields = ['title','description']