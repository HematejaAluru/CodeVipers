from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from .models import posts12
from blog.models import reply
from blog.models import Post
from selenium import webdriver
from twilio.rest import Client 
defultname="okay"
chatroom="none"
postlist=[]
def home(request):
    return render(request,'home.html')
def testee(request):
    v1=request.POST["user_name"]
    v2=request.POST["pass"]
    v3=request.POST["email"]
    v4=request.POST['phone']
    user=User.objects.create_user(username= v1,email= v3,password= v2)
    user.save();
    subject='Trust us its gonna be better...'
    message='You have successfully completed joining our CodeVipers community and this will make your job life a lot easier. If you are preparing for the interviews this is a great chance to overcome the tension and make your goal possible in the eleventh hour.'
    from_email=settings.EMAIL_HOST_USER
    to_list=[v3,settings.EMAIL_HOST_USER]
    send_mail(subject,message,from_email,to_list,fail_silently=False)
    
 
    '''account_sid = 'ACbcea9c59574a613760875bfa4835cb79' 
    auth_token = '21acc33904600818ef9b6b9b78cae70c' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create( 
                              from_='+15104220161',  
                              body='You have successfully completed joining our CodeVipers community and this will make your job life a lot easier. If you are preparing for the interviews this is a great chance to overcome the tension and make your goal possible in the eleventh hour.',      
                              to='+918688951346',
                          ) 
    print(message.sid)'''
    


    return render(request,'test.html')
def login2(request):
    v4=request.POST["user_namee"]
    v5=request.POST["passs"]
    user=authenticate(username=v4,password=v5)
    if user is not None:
        global defultname
        defultname=v4
        P= Post.objects.all()
        Q=reply.objects.all()
        content={'P':P,'Q':Q,'p1':v4}
        return render(request,'poster.html',content)
    else:
        return render(request,'login.html')
def forgotpass(request):
    return render(request,'forgotpass.html')
def login(request):
    return render(request,'login.html')
def registers(request):
    return render(request,'register.html')
def test(request):
    return render(request,'test.html')
def tester(request):
    return render(request,'test.html')
def neural(request):
    return render(request,'neuralnetworks.html')
def temp(request):
    user=User.objects.get(username="avnmht")
    listfinal={"user":user}
    return render(request,'afterlogin.html',listfinal)
def parallel(request):
    return render(request,'index.html')
def roomname(request):
    chatroom=request.POST['okna']


'''def index(request):
    return render(request, 'index.html')'''

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name,
        'defult': defultname
    })

def ideer(request):
    vv=request.POST['ider']
    vn=request.POST['ide']
    content={
        'pp':vv,
        'nn':vn
    }
    return render(request,'reply.html',content)
def createreply(request):
    P=Post.objects.all()
    Q=reply.objects.all()
    vq=request.POST.get('replyid')
    vw=request.POST.get('reply')
    uploaded_filer=request.FILES['filerr']
    ff=reply.objects.create(name=defultname,connector=vq,reply=vw,replyimage=uploaded_filer)
    
    content={'P':P,'Q':Q}
    return render(request,'poster.html',content)
def r(request):
    return render(request,'reply.html')