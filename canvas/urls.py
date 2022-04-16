from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('draw', views.DrawView.as_view(), name='draw'),
    path('getImage', views.getImage, name='get_image')
]