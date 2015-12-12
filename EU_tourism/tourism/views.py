from django.shortcuts import render

import json

def menu(request):
    return render(request, 'static/lsly/menu.html')
def aboutUs(request):
    return render(request, 'static/lsly/aboutUs.html')

def tourismlist(request):
    tourism = None
    if request.POST.has_key('id'):
        id = request.POST['id']
    if request.POST.has_key('name'):
        name = request.POST['name']
    print id,"id"
    print name,"name"
#    result = 
#    result = json.dumps(result)
    return HttpResponse('0', content_type='application/json')

# Create your views here.
