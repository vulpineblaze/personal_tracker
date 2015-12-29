
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


from . import views


urlpatterns = patterns('',
  # url(r'^$', views.home, name='home'),
	url(r'^$', views.all_entries, name='all_entries'),
    url(r'^goals/$', views.goal_index, name='goal_index'), # ADD NEW PATTERN!
    url(r'^index/$', views.index, name='index'), # ADD NEW PATTERN!
    url(r'^goal/(?P<goal_id>\d+)/$', views.entry_index, name='entry_index'), # ADD NEW PATTERN!
    url(r'^new_entry/(?P<goal_id>\d+)/$', views.new_entry, name='new_entry'), # ADD NEW PATTERN!
    url(r'^all_entries/$', views.all_entries, name='all_entries'), # ADD NEW PATTERN!


    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!

    # url(r'^(?P<node_id>\d+)/$', views.detail, name='detail'),

    

)

urlpatterns += patterns('',
  	# url(
   #      r'^login/$',
   #      'django.contrib.auth.views.login',
   #      name='login',
   #      kwargs={'template_name': 'core/login.html'}
   #  ),
   #  url(
   #      r'^logout/$',
   #      'django.contrib.auth.views.logout',
   #      name='logout',
   #      kwargs={'next_page': '/'}
   #  ),
    url(
        r'^password_change$',
        'django.contrib.auth.views.password_change',
        name='password_change',
        kwargs={
               'template_name': 'core/password_change_form.html',
               'post_change_redirect':'password_change_done',
               }
    ),
    url(
        r'^password_change_done$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done',
        kwargs={'template_name': 'core/password_change_done.html'}
    ),
)