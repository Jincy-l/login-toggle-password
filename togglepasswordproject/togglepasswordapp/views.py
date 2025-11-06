from django.shortcuts import render,redirect
from .models import Register



def login(request):
    return render(request,'login.html')

def register_view(request):



    if request.method == "POST":
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address = request.POST.get('address')
        profile_pic = request.FILES.get('profile_pic')
        resume = request.FILES.get('resume')

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        Register.objects.create(
            name=name,
            dob=dob,
            email=email,
            password=password,
            confirm_password=confirm_password,
            address=address,
            profile_pic=profile_pic,
            resume=resume
        )
        return redirect('success')  # redirect to a success page

    return render(request, 'register.html')

def success(request):
    return render(request,'success.html')
def profile_view(request):
    return render(request,'profileview.html')
def edit_profile(request):
    return render(request,"editprofile.html")

    