from django.conf.urls import url
from meiduo_mall.apps.users import views

urlpatterns =[
    url('^register/$', views.RegisterView.as_view()),
    url('^usernames/(?p<username>[^[a-zA-Z0-9_-]{5,20}$])/count/$', views.UsernameCountView.as_view()),
    url('^mobiles/(?p<mobile>)[^1[3456789]\d{9}$]/count/$', views.MobileCountView.as_view()),

]