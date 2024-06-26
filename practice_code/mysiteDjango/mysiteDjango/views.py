from django.shortcuts import HttpResponse,render

def login(request):
    print(request.POST)
    email = request.POST.get("email",None)
    pwd = request.POST.get("pwd",None)
    print(email, pwd)
    #return HttpResponse("OK!!!")
    return render(request, "login.html",)