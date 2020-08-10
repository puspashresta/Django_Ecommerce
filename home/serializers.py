from .models import *
from rest_framework import serializers
from .views import *

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','title','price','discounted_price','image','slug','stock','brand','labels','special_offer','category','subcategory']

class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['title','image','category']
