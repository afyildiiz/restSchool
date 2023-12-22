from django.urls import path, include
from ogrenci.api import views 



urlpatterns = [
    path('ogrenciler/', views.OgrenciApiView.as_view(), name='ogrenciler'),
    path('ogrenciler/<int:pk>',views.OgrenciDetailView.as_view(),name='ogrenci-detail')
    ]



# function based views
# urlpatterns = [
#     path('ogrenciler/', views.api_list, name='ogrenciler'),
#     path('ogrenciler/<int:pk>',views.api_detail,name='ogrenci-detail')
#     ]