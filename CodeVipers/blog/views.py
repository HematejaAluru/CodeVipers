from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from blog.models import Post
from blog.models import reply
# Create your views here.
def index(request):
    P= Post.objects.all()
    content={'P':P,'p1':'avnmht'}
    return render(request,'poster.html',content)
def create(request):
    P=Post.objects.all()
    Q=reply.objects.all()
    vq= request.POST.get('userer')
    vw= request.POST.get('ques')
    if 'filer' in request.FILES:
        uploaded_file=request.FILES['filer']
        kk=Post.objects.create(name=vq,question=vw,postimage=uploaded_file)
    else:
        kk=Post.objects.create(name=vq,question=vw)
    content={'P':P,'Q':Q,'p1':vq}
    return render(request,'poster.html',content)
def createreply(request):
    P=Post.objects.all()
    Q=reply.objects.all()
    vq= request.POST.get('replyid')
    vw= request.POST.get('replynam')
    vg=request.POST.get('replyy')
    if 'frame' in request.FILES:
        uploaded__file=request.FILES["frame"]
        ff=reply.objects.create(name=vw,connector=vq,reply=vg,replyimage=uploaded__file)
    else:    
        ff=reply.objects.create(name=vw,connector=vq,reply=vg)    
    content={'P':P,'Q':Q,'p1':vq}
    return render(request,'poster.html',content)