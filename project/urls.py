"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from user.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("availability",availability, name="availability"),
    path("collective",collective, name="collective"),
    path("contact",contact, name="contact"),
    path("dashboard",dashboard, name="dashboard"),
    path("features",features, name="features"),
    path("group_meetings",group_meetings , name="group_meetings"),
    path("",index, name="index"),
    path("integrations",integrations, name="integrations"),
    path("user_login",user_login, name="user_login"),
    path("new_meeting",new_meeting, name="new_meeting"),
    path("one_to_one",one_to_one, name="one_to_one"),
    path("profile",profile, name="profile"),
    path("round_robin",round_robin, name="round_robin"),
    path("sign_up",sign_up, name="sign_up"),
    path("meet",meet, name="meet"),
    path("otp/<int:id>",otp, name="otp"),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='logout'),
]
urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
