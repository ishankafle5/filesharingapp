from django.shortcuts import redirect, render

from users.models import User

# Create your views here.


def signup_page(request):
    if (request.method == 'GET'):
        return render(request, 'signup.html')
    elif (request.method == 'POST'):
        username = request.POST['username']
        email = request.POST.get('email')
        number = request.POST.get('number')
        password1 = request.POST['password']
        confirm_pw = request.POST.get('confirm')

        print(username+" "+email+" "+number+" "+password1+" "+confirm_pw)

        try:
            number = int(number)
        except:
            return render(request, 'signup.html', {'msg': "Phone number doesn't match"})

        if (password1 != confirm_pw):
            return render(request, 'signup.html', {'msg': "Phone number doesn't match"})

        else:
            user = User.objects.create(fullname=username,
                                       email=email, phonenumber=number, password=password1)

            return redirect('/login')


def login_page(request):
    if (request.method == 'GET'):
        return render(request, 'login.html')

    email = request.POST['email']
    password = request.POST['password']

    print(email+password)

    object = User.objects.filter(email=email, password=password)
    if object:
        return render(request, 'uploadfile.html')