
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('delete/<int:tid>/',views.delete,name='delete'),
    path('edit/<int:tid>/',views.edit,name='edit'),
    path('classlview/',views.classlist.as_view(),name='classlistview'),
    path('classd/<int:pk>/',views.classdetail.as_view(),name='classdetail'),
    path('classupdate/<int:pk>/',views.classup.as_view(),name='classup'),
    path('classdelete/<int:pk>/',views.classdel.as_view(),name='cassdel')
]