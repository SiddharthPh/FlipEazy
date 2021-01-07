from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect,HttpResponse
# from main.forms import toolform
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from typing import List
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

import json
# Create your views here.
# Testing
def home_page(request):
    return render(request,'main/index.html')
def login(request):
    return render(request, 'main/log_sign.html')
def marketplace(request):
    return render(request, 'main/Marketplace.html')
def blog(request):
    return render(request, 'main/blog.html')
def contact_us(request):
    return  render(request,'main/contact_us.html')
def about_us(request):
    return render(request,'main/aboutus.html')
@login_required    
def buysite(request):
    return render(request,'main/buy_site.html')
@login_required
def sellsite(request):
    return render(request,'main/sell_site.html')
# def about_us(request):
#     return render(request,'main/aboutus.html')
def valuationtool(request):
    return render(request, 'main/valuationtool.html')
def email_list(request):
    return render(request, 'main/EmailList.html')
def automation(request):
    return render(request, 'main/Automation.html')
def factors(request):
    return render(request, 'main/WHAT FACTORS DETERMINES YOUR WEBSITES WORTH.html')
def whymarket_place(request):
    return render(request,'main/whymarketplace.html')
def onlinebusiness(request):
    return render(request, 'main/What_is_an_Online_Business_Why_should_you_Own_One.html')
def leveragecontent(request):
    return render(request,'main/LeverageContent.html')
def signin_submit(request):
    if request.method=='POST':
        username=request.POST['username1']
        password=request.POST['password1']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid Credentials')
            return redirect('/login')


def signup_submit(request):
    if request.method =='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('/login')
        else:
            user=User.objects.create_user(username=username, email=email, password=password)
            user.save()
            print("user created")
            return redirect('/')
    else:
        return redirect('/login')

def data_submit(request):
    if request.method == 'POST':
        name=request.POST['full_name']
        url=request.POST['url']
        email=request.POST['email']
        # revenue=request.POST['monthly_revenue']
        profit=request.POST['monthly_profit']
        profit_1=int(profit)*27
        context={'profit':profit_1}
        tool_obj=tool.objects.create(name=name,email=email,url=url)
        tool_obj.save()
    return render(request,'main/charts.html',context)
def sell_now(request):
    return render(request,'main/sellnow.html')
# def submit(request):
#    if request.method =='POST':
#         mail=request.POST.get('mail')
#         # income=request.POST.get('inc','')
#         tool_obj=tool(mail=mail)
#         tool_obj.save()
#         return HttpResponseRedirect(reverse(''))

# def toolview(request):
#     if request.method =='POST':
#         # form=toolform(request.POST)
#         # url=request.POST.get('url','')
#         mail=request.POST.get('mail')
#         print(mail)
#         # income=request.POST.get('inc','')
#         tool_obj=tool(mail=mail)
#         tool_obj.save()
#         return HttpResponseRedirect(reverse('home'))

def contactus_form_view(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        contactus_form_obj=contactus_form.objects.create(name=name,email=email,message=message)
        contactus_form_obj.save()
        send_mail(
            subject='Test Mail',
            message=message,
            from_email='siddharthapothukuchi@gmail.com',
            recipient_list=['saitejasuggala458@gmail.com'],
            fail_silently=False
        )
    return redirect('home')
# def send_email(from_addr: settings.EMAIL_HOST_USER, to_addr: "saitejasuggala458@gmail.com", subject: "message"):
#         msg = message
#         with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT) as server:
#             server.starttls()
#             server.login(SMTP_USER, SMTP_PASSWORD)
#             server.sendmail(from_addr, to_addr, msg)
#     return redirect('home')

def newsletter_view(request):
    if request.method=='POST':
        email=request.POST['email_letter']
        news_obj=newsletter.objects.create(email=email)
        news_obj.save()
    return redirect('home')
@login_required
def logout(request):
    django_logout(request)
    return redirect('home')