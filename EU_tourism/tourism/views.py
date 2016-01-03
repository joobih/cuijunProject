from django.shortcuts import render_to_response
from django.template import loader, Context
from django.http import HttpResponse
from models import *

import json

def routeDetails(request, route_id):
    b = BoutiqueLine.objects.get(id = route_id)
    b_d = BoutiqueLineDetails.objects.filter(boutiqueline = b)
    print b_d
    return render_to_response('routeDetails.html')

def personalTailor(request):
    if request.method == 'POST':#request.POST:
        print "bbb"
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        destination = request.POST.get('destination')
        days = request.POST.get('days')
        price = request.POST.get('price')
        approach = request.POST.get('approach','')
        hotel = request.POST.get('hotel','')
        travel_requirement = request.POST.get('travel_requirement', '') 
        print name,phone,destination,days,price,approach
        strjson = {}
        strjson['ret_code'] = 0 
        return HttpResponse(json.dumps(strjson), content_type='application/json')
#        HttpResponse(json.dumps(name_dict), content_type='application/json')
#        return render_to_response('personalTailor.html',{'data':0}, context_instance=RequestContext(request))
    else:
        return render_to_response('personalTailor.html')#,context_instance=RequestContext(request))


def view(request,template_name):
    if template_name == 'menu.html':
        print "adfs"
        menu = BoutiqueLine.objects.all()
        menu_list = []
        for m in menu:
            menu_list.append({'name':m.name, 'pic_address':m.pic_address, 'price':str(m.price)})
        t = loader.get_template('menu.html')
        c = Context({'menu_list':json.dumps(menu_list)})
        return HttpResponse(t.render(c))
    return render_to_response(template_name)

#def menu(request):
#    return render(request, 'static/lsly/menu.html')
#def aboutUs(request):
#    return render(request, 'static/lsly/aboutUs.html')

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
