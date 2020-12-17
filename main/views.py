from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect,HttpResponse
# from main.forms import toolform
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import tool
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
    return  render(request,'main/aboutus.html')
def buysite(request):
    return render(request,'main/buy_site.html')
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
    # form = NameForm(request.GET)
    # form.your_name=
    if request.method == 'POST':
        data=request.body
        data=data.decode("utf-8") 
        data=json.loads(data)
        tool.objects.create(
            name=data['name'],
            url=data['url'],
            email=data['email']
        )
        # tool_obj=tool(name=name1)
        # tool_obj.name=name1
        # tool_obj.save()
    return render(request,'main/charts.html')
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

            