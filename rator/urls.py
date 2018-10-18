from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home,name='home'),
    url('login/',views.login_user, name='login'),
    url('logout/',views.logout_user, name='logout'),
    url('register/',views.register_user, name='register'),
    url('edit_profile/',views.edit_profile, name='edit_profile'),
    url('change_password/',views.change_password, name='change_password'),
    url(r'^post/$', views.new_project, name='new_project'),
    url(r'^comments/(\d+)', views.comment, name='comments'),
    url( r'^edit/' , views.edit , name='edit' ),
    url( r'^profile/' , views.profile , name='profile' ),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
