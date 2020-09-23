from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect,HttpResponse
# from main.forms import toolform
from .models import tool
import json
# Create your views here.
# Testing
def home_page(request):
    return render(request,'main/index.html')
def login(request):
    return render(request, 'main/login.html')
def marketplace(request):
    return render(request, 'main/Marketplace.html')
def blog(request):
    return render(request, 'main/WHAT FACTORS DETERMINES YOUR WEBSITES WORTH.html')
def contact_us(request):
    return  render(request,'main/contact_us.html')
def valuationtool(request):
    return render(request, 'main/valuationtool.html')
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
        return HttpResponse('Success')
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

            