from django.contrib import admin
from django.urls import include, path,re_path

from polls.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls',namespace="index") ),
    path('barcode_view', include('polls.urls',namespace="barcode_view")),  
    path('create_qr', include('polls.urls',namespace="create_qr")),  
    path('create_barcode', include('polls.urls',namespace="create_barcode")),  
    path('qr_lists', include('polls.urls',namespace="qr_lists")),  
    path('show_qr', include('polls.urls',namespace="show_qr")),  
]
