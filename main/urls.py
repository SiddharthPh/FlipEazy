from django.urls import path
from . import views
urlpatterns=[
    path('',views.home_page,name="home_page"),
    path('login/',views.login,name="login"),
    path('marketplace/',views.marketplace,name="marketplace"),
    path('blogs/',views.blog,name="blog"),
    path('contactus/',views.contact_us,name="contact_us")
]
