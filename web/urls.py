from django.conf.urls import url
from web.views import account

urlpatterns = [
    url(r'^register/$', account.register, name='register'),
]