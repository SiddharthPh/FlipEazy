from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'main/index.html')
def login(request):
    return render(request, 'main/login.html')
def marketplace(request):
    return render(request, 'main/Marketplace.html')
def blog(request):
    return render(request, 'main/blog.html')
