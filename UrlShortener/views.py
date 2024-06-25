from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import uuid
from .models import Url
# Create your views here.
def index(request):
    urls= Url.objects.all().order_by('-created_at')
    context = {
         'urls':urls
    }
    return render(request, 'index.html',context)

def createShortUrl(request):
    if request.method == 'POST':
        url_link = request.POST['url_link']
        print(url_link)
        uid = str(uuid.uuid4())[:3]
        print(uid)
        url_object = Url(url_link=url_link,uuid=uid)
        url_object.save()
        return HttpResponse(uid)
    
def go(request, pk):
    url_details = get_object_or_404(Url, uuid=pk)
    return redirect(url_details.url_link)