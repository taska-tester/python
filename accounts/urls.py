from django.conf.urls import url
from accounts import views
# from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^send_login_email$', views.send_login_email, name='send_login_email'),
]
