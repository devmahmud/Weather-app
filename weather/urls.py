from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('addcity',views.addcity, name='addcity'),
    path('delete/<city_id>',views.delete, name='delete')
]
