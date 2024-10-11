"""
URL configuration for icecream project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home.views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', home, name="home"),  # home page
    path('menu/', menu, name="menu"),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('quiz/', submit_quiz, name='submit_quiz'),
    path('result/', submit_quiz, name='result'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('send-email/', send_email, name='send_email'),
    path('recipe/<str:recipe_name>/', recipe_view, name='recipe_view'),
     # URL to handle adding items to the cart
    path('add-to-cart/', add_to_cart, name='add_to_cart'),

    # URL to retrieve cart items (for viewing the cart)
    path('cart-items/', get_cart_items, name='get_cart_items'),
    path('admin/', admin.site.urls),
]
