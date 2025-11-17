from django.shortcuts import render,redirect
from .models import Register
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages



def login(request):
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Register.objects.get(email=email, password=password)
            request.session["email"] = user.email
            return redirect("profile")
        except ObjectDoesNotExist:
            messages.error(request, "Invalid email or password!")
            return redirect("login")

    return render(request, "login.html")

    

def register_view(request):



    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     dob = request.POST.get('dob')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     confirm_password = request.POST.get('confirm_password')
    #     address = request.POST.get('address')
    #     profile_pic = request.FILES.get('profile_pic')
    #     resume = request.FILES.get('resume')

    #     if password != confirm_password:
    #         return render(request, 'register.html', {'error': 'Passwords do not match'})

    #     Register.objects.create(
    #         name=name,
    #         dob=dob,
    #         email=email,
    #         password=password,
    #         confirm_password=confirm_password,
    #         address=address,
    #         profile_pic=profile_pic,
    #         resume=resume
    #     )
    #     return redirect('success')  # redirect to a success page
    

    if request.method == "POST":
        name = request.POST.get("name")
        dob = request.POST.get("dob")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        address = request.POST.get("address")
        profile_pic = request.FILES.get("profile_pic")
        resume = request.FILES.get("resume")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if Register.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("register")

        reg = Register.objects.create(
            name=name,
            dob=dob,
            email=email,
            password=password,
            confirm_password=confirm_password,
            address=address,
            profile_pic=profile_pic,
            resume=resume
        )
        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    return render(request, "register.html")

    

def success(request):
    return render(request,'success.html')
def profile_view(request):
    
    if "email" not in request.session:
        return redirect("login")

    user = Register.objects.get(email=request.session["email"])
    return render(request, "profile.html", {"user": user})

    
def edit_profile(request):
    
    if "email" not in request.session:
        return redirect("login")

    user = Register.objects.get(email=request.session["email"])

    if request.method == "POST":
        user.name = request.POST.get("name")
        user.dob = request.POST.get("dob")
        user.address = request.POST.get("address")

        if request.FILES.get("profile_pic"):
            user.profile_pic = request.FILES.get("profile_pic")

        if request.FILES.get("resume"):
            user.resume = request.FILES.get("resume")

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile")

    return render(request, "edit_profile.html", {"user": user})

    

    