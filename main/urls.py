from django.urls import path
from . import views
urlpatterns=[
    path('',views.home_page,name="home_page"),
    path('login/',views.login,name="login"),
    path('buysite/',views.buysite,name="buysite"),
    path('sellsite/',views.sellsite,name="sellsite"),
    # path('aboutus/',views.about_us,name="about_us"),
    path('marketplace/',views.marketplace,name="marketplace"),
    path('blogs/',views.blog,name="blog"),
    path('contactus/',views.contact_us,name="contact_us"),
    path('evaluationtool/', views.valuationtool, name="valuationtool"),
    path('emaillist/',views.email_list,name="email_list"),
    path('automation/',views.automation,name="automation"),
    path('factors/',views.factors,name="factors"),
    path('whymarketplace/',views.whymarket_place,name="whymarketplace"),
    path('OnlineBusiness/',views.onlinebusiness,name="onlinebusiness"),
    path('leverageContent/',views.leveragecontent,name="leverage"),
    path('data_submit/',views.data_submit, name="data_submit"),
    path('signup/', views.signup_submit, name="signup_submit"),
    path('signin/',views.signin_submit,name="signin_submit")
]
