from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    if(request.method=='POST'):
        if(request.POST[loginbtn]):
            print('login!!!')
            us=request.POST['user']
            pw=request.POST['pw']
            
            try:
                record=User.objects.get(username=us)
                dbpw=record.password

                if(pw==dbpw):
                    return render(request, 'home.html')
                else:
                    print('password incorrect!')
                    return render(request, 'login.html')
            except:
                print("user not found!!!")
                return render(request, 'login.html')
            

            else:
                return render(request, 'login.html')



