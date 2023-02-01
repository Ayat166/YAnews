from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('genral',views.genral,name='genral'),
    path('business',views.business,name='business'),
    path('sport',views.sport,name='sport'),
    path('technology',views.technology,name='technology'),
    path('entertainment',views.entertainment,name='entertainment'),
    path('search',views.search,name='search'),
    path('new/<str:new_id>',views.new,name='new'),
    path('business/new/<str:new_id>',views.newBusiness,name='newBusiness'),
    path('sport/new/<str:new_id>',views.newSport,name='newSport'),    
    path('technology/new/<str:new_id>',views.newTechnology,name='newTechnology'),    
    path('entertainment/new/<str:new_id>',views.newEntertainment,name='newEntertainment'),
    path('search/new/<str:name>/<str:new_id>',views.newSearch,name='newSearch'),        
    
]