from django.shortcuts import redirect, render

from users.models import User

# Create your views here.


def signup_page(request):
    if (request.method == 'GET'):
        return render(request, 'signup.html')
    elif (request.method == 'POST'):
        username = request.POST['fullname']
        email = request.POST.get('email')
        number = request.POST.get('number')
        password1 = request.POST['password']
        confirm_pw = request.POST.get('confirm')

        try:
            number = int(number)
        except:
            return render(request, 'signup.html', {'msg': "Phone number doesn't match"})

        if (password1 != confirm_pw):
            return render(request, 'signup.html', {'msg': "Phone number doesn't match"})

        else:
            checking = User.objects.filter(email=email)
            if (checking.exists()):
                return render(request, 'signup.html', {'msg': "Email is already registered"})

            user = User.objects.create(fullname=username,
                                       email=email, phonenumber=number, password=password1)

            return redirect('/login')


def login_page(request):
    if (request.method == 'GET'):
        if (request.session.get('user_email')):
            return redirect('/uploadpage')
        else:
            return render(request, 'login.html')
    email = request.POST['email']
    password = request.POST['password']
    object = User.objects.filter(email=email, password=password)
    if object:
        request.session['user_email'] = email
        return redirect('/uploadpage')
    else:
        return render(request, 'login.html', {'msg': "User name and password doesn't match !"})
