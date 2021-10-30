from django.urls import path

from . import views

 

urlpatterns = [

    path('register',views.register,name='register'),
 
   # path('home', views.home,name='home'),
    
    path('show', views.show,name='show'),
    #path('/new1', views.new1,name='new1'),
    path('no', views.no ,name='no'),
    path('addresses', views.addresses,name="addresses"),
    path('slides', views.slides, name="slides"),
    path('cart', views.cart, name="cart"),
   # path('delete/<str:id>',views.delete, name='delete'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('lappy', views.lappy, name="lappy"),
  

]