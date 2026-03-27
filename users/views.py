from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile

@login_required
def profile(request):
    # This ensures a profile exists for the user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')  # reload page after save
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile.html', context)


from django.shortcuts import render, redirect
from users.services.user_service import UserService

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        result = UserService.register_user(username, email, password)

        if "error" in result:
            return render(request, "users/register.html", {"error": result["error"]})

        return redirect("login")

    return render(request, "users/register.html")

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")  # or dashboard
        else:
            return render(request, "users/login.html", {"error": "Invalid credentials"})

    return render(request, "users/login.html")

from django.shortcuts import render

def home(request):
    return render(request, 'users/home.html')


from .decorators import role_required

@role_required(['admin'])
def admin_dashboard(request):
    try:
        user_role = request.user.profile.role
    except:
        return HttpResponse("Profile not found")

    if user_role != "admin":
        return HttpResponse("Access Denied")
    return render(request, 'admin/dashboard.html')

@role_required(['seller'])
def seller_dashboard(request):
    return render(request, 'seller/dashboard.html')

@role_required(['customer'])
def customer_home(request):
    return render(request, 'customer/home.html')

@role_required(['admin', 'seller'])
def add_product(request):
    return render(request, 'products/add.html')

