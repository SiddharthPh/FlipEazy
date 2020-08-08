from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
# from main.forms import toolform
from .models import tool

# Create your views here.
# Testing
def home_page(request):
    return render(request,'main/index.html')
def login(request):
    return render(request, 'main/login.html')
def marketplace(request):
    return render(request, 'main/Marketplace.html')
def blog(request):
    return render(request, 'main/blog.html')
def contact_us(request):
    return  render(request,'main/contact_us.html')
def submit(request):
    if request.method =='POST':
        mail=request.POST.get('mail')
        # income=request.POST.get('inc','')
        tool_obj=tool(mail=mail)
        tool_obj.save()
        return HttpResponseRedirect(reverse(''))

# def toolview(request):
#     if request.method =='POST':
#         # form=toolform(request.POST)
#         # url=request.POST.get('url','')
#         mail=request.POST.get('mail')
#         # income=request.POST.get('inc','')
#         tool_obj=tool(mail=mail)
#         tool_obj.save()
#         return HttpResponseRedirect(reverse('home'))

            