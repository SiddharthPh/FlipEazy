from django.urls import path
from . import views
urlpatterns=[
    path('',views.home_page,name="home_page"),
    path('login/',views.login,name="login"),
    path('buysite/',views.buysite,name="buysite"),
    path('sellsite/',views.sellsite,name="sellsite"),
    path('aboutus/',views.about_us,name="about_us"),
    path('marketplace/',views.marketplace,name="marketplace"),
    path('blogs/',views.blog,name="blog"),
    path('contactus/',views.contact_us,name="contact_us"),
    path('evaluationtool/', views.valuationtool, name="valuationtool"),
    path('data_submit/',views.data_submit, name="data_submit")
]
