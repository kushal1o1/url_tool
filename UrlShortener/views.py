from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import uuid
from .models import Url
from django.utils.html import escape
from decouple import config 


def index(request):
    urls= Url.objects.all().order_by('-created_at')
    context = {
         'urls':urls,
         'HOST_URL': config('HOST_URL')
    }
    return render(request, 'index.html',context)

def createShortUrl(request):
    if request.method == 'POST':
        rawUrl = request.POST['url_link']
        url_link=escape(rawUrl)
        uid = str(uuid.uuid4())[:3]
        print(uid)
        url_object = Url(url_link=url_link,uuid=uid)
        url_object.save()
        return HttpResponse(uid)
    
def go(request, pk):
    try:
        url_details = get_object_or_404(Url, uuid=pk)
        return redirect(url_details.url_link)
    except:
        return render(request, 'pageNotFound.html')


def about(request):
    return render(request,'about.html')


def notFound(request):
    return render(request,'pageNotFound.html')
