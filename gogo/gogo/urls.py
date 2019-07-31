"""gogo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blog.views
import imageview.views
import login.views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('blog/',include('blog.urls')),
    path('login/',include('login.urls')),
    path('', blog.views.index, name="index"),
    path('imageview/',imageview.views.imageview, name="imageview"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # path('new',blog.views.new, name="new"),
    # path('<int:post_id>/',blog.views.detail, name="detail"),
    # path('create/',blog.views.create, name="create"),
    # path('modify/<int:post_id>',blog.views.modify, name="modify"),
    # path('update/<int:post_id>',blog.views.update, name="update"),
    # path('delete/<int:post_id>',blog.views.delete, name="delete"),
    # path('newpost/',blog.views.newpost, name="newpost"),