from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def cookie(request):
    print(request.COOKIES)
    resp=HttpResponse('HAI JOKEY')
    resp.set_cookie('zap', 42)
    resp.set_cookie('dj4e_cookie','edea2984',max_age=1000)
    return resp
def sessfun(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    return HttpResponse('view count='+str(num_visits))