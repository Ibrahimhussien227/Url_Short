from django.shortcuts import redirect, render
from root.models import Url

# Create your views here.
def createUrl(req):
    if req.method == "POST":
        # here we get what the user write in the site so we can after create new url from it
        full_url = req.POST.get('full_url')
        obj = Url.create(full_url)
        return render(req, 'root/index.html', {
            'full_url' : obj.full_url,
            # for making local host + the the new short url together so i can show it in index.html
            'short_url' :  obj.short_url
        })

    return render(req, 'root/index.html')

# and here we redirect to the new short_url
def routeToURL(req, key):
    try:
        obj = Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        return redirect(createUrl)
