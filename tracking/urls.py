from django.conf.urls import url

from . import api

app_name = 'api'

urlpatterns = [
    url(r'^task/$', api.TaskList.as_view()),
]
