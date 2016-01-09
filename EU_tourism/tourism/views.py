#encoding: utf-8
from django.shortcuts import render_to_response
from django.template import loader, Context
from django.http import HttpResponse
from models import *
from django.views.decorators.csrf import csrf_exempt

import json

def routeDetails(request, route_id):
    b = BoutiqueLine.objects.get(id = route_id)
    b_d = BoutiqueLineDetails.objects.filter(boutiqueline = b)
    routeDet = []
    title = b.name
    map_pic_address = b.map_pic_address
    for r in b_d:
        routeDet.append({'day_numbers':r.day_numbers,'node_details':r.node_details,'approach':r.approach,\
                         'detail_pic_number':r.detail_pic_number,'detail_pic_address':r.detail_pic_address})
    t = loader.get_template('routeDetails.html')
    c = Context({'routeDet':json.dumps(routeDet),'title':json.dumps(title),'map':json.dumps(map_pic_address)})
    print "routeDetails"
    return HttpResponse(t.render(c))

#def seachRoute(request):
        

def personalTailor(request):
    if request.method == 'POST':
        print "bbb"
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        destination = request.POST.get('destination')
        days = request.POST.get('days')
        price = request.POST.get('price')
        approach = request.POST.get('approach','')
        hotel = request.POST.get('hotel','')
        travel_requirement = request.POST.get('travel_requirement', '')
        strjson = {}
        if not name:
            strjson['ret_code'] = -1
            strjson['msg'] = u"名字不能为空"
            print strjson
            return HttpResponse(json.dumps(strjson), content_type='application/json')
        if not phone:
            strjson['ret_code'] = -1
            strjson['msg'] = u"电话不能为空"
            print strjson
            return HttpResponse(json.dumps(strjson), content_type='application/json')
        travel = PrivateOrder(name = name, phone = phone, destination = destination, days = days, price = price, 
                              approach = approach, hotel = hotel, travel_requirement = travel_requirement)
        travel.save()
        print name,phone,destination,days,price,approach
        strjson['ret_code'] = 0 
        return HttpResponse(json.dumps(strjson), content_type='application/json')
    else:
        return render_to_response('personalTailor.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        print "注册提交"
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
#        print name,phone,email,password
        strjson = {}
        if not name:
            strjson['ret_code'] = -1
            strjson['msg'] = "名字不能为空"
            print strjson
            return HttpResponse(json.dumps(strjson), content_type='application/json')
        if not phone:
            strjson['ret_code'] = -2
            strjson['msg'] = "电话不能为空"
            print strjson
            return HttpResponse(json.dumps(strjson), content_type='application/json')
        if not password:
            strjson['ret_code'] = -3
            strjson['msg'] = "密码不能为空"
            return HttpResponse(json.dumps(strjson), content_type='application/json')
        u = User.objects.get(phone = phone)
        if u:
            strjson['ret_code'] = 1
            strjson['msg'] = "该号码已注册"
            return HttpResponse(json.dumps(strjson), content_type='application/json')
        user = User(name = name, phone = phone, email = email, password = password)
        user.save()
        strjson['ret_code'] = 1
        strjson['msg'] = "恭喜你！注册成功！"
        print name,phone,password,email
        return HttpResponse(json.dumps(strjson), content_type='application/json')
    else:
        return render_to_response('lshy.html')

def leavemessage(request):
    if request.method == 'POST':
        print "留言"
        title = request.POST.get('name')
        content = request.POST.get('content')
        
        #email = request.POST.get('')

def view(request,template_name):
    if template_name == 'menu.html':
        print "adfs"
        menu = BoutiqueLine.objects.all()
        menu_list = []
        message_list = []
        for m in menu:
            menu_list.append({'menu_id':m.id, 'name':m.name, 'pic_address':m.pic_address, 'price':str(m.price)})
        message = LeaveMessage.objects.all()
        for ms in message:
            message_list.append({'title':ms.title,'content':ms.content,'create_time':ms.create_time})
        t = loader.get_template('menu.html')
        c = Context({'menu_list':json.dumps(menu_list),'message_list':json.dumps(message_list)})
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
