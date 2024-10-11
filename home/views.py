from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import EmailVerification
import random
import string
from home.utils import send_mail_to_client
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'index.html')

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to index page after successful login
            return redirect('/')
        else:
            error_message = "Invalid username or password"

    return render(request, 'login.html', {'error_message': error_message})

def send_email(request):
    send_mail_to_client()
    return redirect('/')

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

# def signup(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(f"First Name: {first_name}, Last Name: {last_name}")
#         # Create user but don't activate yet (set is_active to False)
#         user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name, is_active=False)

#         otp = generate_otp()
#         EmailVerification.objects.create(user=user, otp=otp)

#         subject = 'Verify your email address'
#         message = f'Your OTP is {otp}. It is valid for 10 minutes.'
#         from_email = settings.DEFAULT_FROM_EMAIL
#         recipient_list = [email]
#         send_mail(subject, message, from_email, recipient_list)

#         # Store email in session to access in the verification view
#         request.session['email'] = email

#         return redirect('verify_otp')  # Redirect to OTP verification page

    # return render(request, 'signup.html')

from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate
def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        # Check if any of the fields are empty
        if not first_name or not last_name or not username or not email or not password:
            messages.error(request, "All fields are required!")
            return render(request, 'signup.html')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_active=False  # Activate after email verification
            )
            

            otp = generate_otp()
            EmailVerification.objects.create(user=user, otp=otp)

            # Send verification email
            subject = 'Verify your email address'
            message = f'Your OTP is {otp}. It is valid for 10 minutes.'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            # Store email in session to access in OTP verification
            request.session['email'] = email

            return redirect('verify_otp')

        except IntegrityError:
            messages.error(request, "A user with that email or username already exists.")
            return render(request, 'signup.html')

    return render(request, 'signup.html')

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        email = request.session.get('email')  # Get email from session
        if email:
            try:
                verification = EmailVerification.objects.get(otp=otp, user__email=email)
                if verification.is_valid():
                    user = verification.user
                    user.is_active = True
                    user.save()  # Activate user
                    verification.delete()  # Remove OTP record after successful verification
                    messages.success(request, 'Your email has been verified successfully!')
                    return redirect('login')  # Redirect to login page
                else:   
                    messages.error(request, 'OTP has expired.')
            except EmailVerification.DoesNotExist:
                messages.error(request, 'Invalid OTP.')
        else:
            messages.error(request, 'Session expired. Please sign up again.')
            
    return render(request, 'otp_verification.html')


# def menu(request):
#     return render(request, 'menu.html')


from django.shortcuts import render
from .classifier import predict_flavor

def submit_quiz(request):
    if request.method == 'POST':
        # Collect answers from the POST request form
        user_answers = [
            int(request.POST['q1']),  # Get answer for Question 1
            int(request.POST['q2']),  # Get answer for Question 2
            int(request.POST['q3']),  # Get answer for Question 3
            int(request.POST['q4']),  # Get answer for Question 4
            int(request.POST['q5']),  # Get answer for Question 5
            int(request.POST['q6'])   # Get answer for Question 6
        ]
        
        # Predict the flavor using the classifier
        predicted_flavor = predict_flavor(user_answers)
        image_path = f'images/{predicted_flavor.lower().replace(" ", "-")}.jpeg'

        # Render the result page, passing the predicted flavor and image path
        return render(request, 'result.html', {
            'flavor': predicted_flavor,
            'image_path': image_path
        })

    # If request is GET, simply load the quiz page
    return render(request, 'ice_cream_quiz.html')

from django.shortcuts import render

# Hard-coded data for the recipes
recipes = {
    'Vanilla Berry Cone': {
        'image': 'images/blueberry.jpg',
        'description': "Indulge in the Vanilla Berry Temptation Cone! It’s a perfect blend of creamy, crunchy, and tart flavors, making it an irresistible treat! 🍦🍫🍓",
        'ingredients': ['Vanilla ice cream', 'Blueberries', 'Waffle cone', 'Chocolate drizzle'],
        'instructions': "Scoop vanilla ice cream into the waffle cone, top with fresh blueberries, and drizzle with chocolate."
    },
    'Strawberry Dream Delight': {
        'image': 'images/icecreamShake.jpg',
        'description': "A perfect blend of sweetness and freshness.",
        'ingredients': ['Strawberries', 'Vanilla ice cream', 'Whipped cream', 'Milk'],
        'instructions': "Blend strawberries, vanilla ice cream, and milk together. Top with whipped cream."
    },
    'Strawberry Bliss Rolls': {
        'image': 'images/roll1.jpg',
        'description': "Vibrant pink ice cream rolls made with fresh strawberries.",
        'ingredients': ['Strawberries', 'Milk', 'Sugar', 'Ice cream base'],
        'instructions': "Mix strawberries, milk, and sugar. Freeze and roll the mixture into ice cream rolls."
    },
    'Melting Ice Cream Cake': {
        'image': 'images/iceCake.jpg',
        'description': "A fun cake with an upside-down ice cream cone on top.",
        'ingredients': ['Cake base', 'Vanilla ice cream', 'Chocolate', 'Ice cream cone'],
        'instructions': "Bake a cake, top with ice cream, dip the cone in chocolate, and place on top."
    },
    'Chocolate Brownie Sizzler': {
        'image': 'images/sizzler.jpg',
        'description': "A sizzling brownie topped with vanilla ice cream.",
        'ingredients': ['Brownie', 'Vanilla ice cream', 'Chocolate syrup'],
        'instructions': "Heat the brownie on a sizzler plate, top with vanilla ice cream, and drizzle with chocolate syrup."
    },
    'Cherry-Berry Sundae': {
        'image': 'images/sundae.jpg',
        'description': "A sundae topped with whipped cream and cherries.",
        'ingredients': ['Vanilla ice cream', 'Whipped cream', 'Cherries', 'Syrup'],
        'instructions': "Layer vanilla ice cream, whipped cream, and cherries in a sundae glass."
    }
}

def recipe_view(request, recipe_name):
    # Fetch the recipe based on the name from the dictionary
    recipe = recipes.get(recipe_name)
    
    if recipe:
        return render(request, 'recipe.html', {'recipe': recipe, 'name': recipe_name})
    else:
        # If the recipe is not found, you can show a 404 page or an error message
        return render(request, '404.html', status=404)

from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout

def logout_view(request):
    auth_logout(request)
    return redirect('/login/')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')

from django.http import JsonResponse
import redis
import json

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        user = request.user

        if user.is_authenticated:
            # The key for the user's cart in Redis
            cart_key = f"cart:{user.username}"

            # Check if the item already exists in the user's cart
            if redis_client.hexists(cart_key, item_name):
                # If item exists, increment its quantity
                item_data = json.loads(redis_client.hget(cart_key, item_name))
                item_data['quantity'] += 1
            else:
                # If item doesn't exist, create it with quantity 1
                item_data = {
                    'item_name': item_name,
                    'item_price': item_price,
                    'quantity': 1
                }

            # Store the updated item back in Redis
            redis_client.hset(cart_key, item_name, json.dumps(item_data))

            # Return the current quantity of the item to the frontend
            return JsonResponse({'success': True, 'item_name': item_name, 'quantity': item_data['quantity']})
        else:
            return JsonResponse({'success': False, 'message': 'User not authenticated'})

    return JsonResponse({'success': False, 'message': 'Invalid request'})

def get_cart_items(request):
    user = request.user
    if user.is_authenticated:
        cart_key = f"cart:{user.username}"
        cart_items = redis_client.hgetall(cart_key)  # Get all items in the user's cart

        # Decode each item from JSON and prepare the data
        cart_data = {item_name: json.loads(item_details) for item_name, item_details in cart_items.items()}
        
        return JsonResponse({'success': True, 'cart': cart_data})
    else:
        return JsonResponse({'success': False, 'message': 'User not authenticated'})
from django.template.context_processors import csrf

def menu(request):
    context = {}
    context.update(csrf(request))
    return render(request, 'menu.html', context)
