
from django.urls import path,include
from . import views
app_name='blog'
urlpatterns = [

    path('', views.all_blog, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('somehtml',views.somehtml,name='some')
]