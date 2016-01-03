"""EU_tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from tourism import views
#from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'^tourismlist/', views.tourismlist, 
#        name = 'tourismlist'),
    url(r'^menu/$', views.view, {"template_name" : 'menu.html'}),#, { 'document_root': settings.STATIC_ROOT } )
#        { 'document_root': settings.STATIC_ROOT }
#        ),
    url(r'^aboutUs/$', views.view, {"template_name" : 'aboutUs.html'}),
    url(r'^personalTailor/$', views.personalTailor, name = 'personalTailor'),
    url(r'^routeDetails/(.*)$', views.routeDetails, name = 'routeDetails')
#    url(r'^personalTailor/$', views.view, {"template_name" : 'personalTailor.html'})
]
