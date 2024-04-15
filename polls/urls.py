from django.urls import path, re_path

from . import views
app_name = 'polls'


urlpatterns = [
    path('', views.index, name='index'),   
    path('index', views.index, name='index'),
    path('qr_lists', views.qr_lists, name='qr_lists'),
    path('show_qr/<slug:slug>', views.show_qr, name='show_qr'),
    path('show_barcode/<slug:slug>', views.show_barcode, name='show_barcode'),
    path('create_qr', views.create_qr, name='create_qr'),
    path('barcode_view', views.barcode_view, name='barcode_view'),
    path('create_barcode', views.create_barcode, name='create_barcode'),
    


]

