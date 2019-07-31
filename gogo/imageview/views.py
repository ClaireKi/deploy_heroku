from django.shortcuts import render
from .models import Imageview
# Create your views here.

def imageview(request):
    user = request.user
    if user.is_active:
        imageviews = Imageview.objects
        return render(request, 'image.html',{'imgclass':imageviews})
    else:
        return render(request, 'plzLogin.html')