from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

from UserProfile.views import TableProfileList, TableProfileDetail, DataProfileDetail

#Urls hijas

urlpatterns = [
    re_path(r'^profile$', TableProfileList.as_view()),
    re_path(r'^profile/(?P<pk>\d+)$', TableProfileDetail.as_view()),
    re_path(r'^config/(?P<pk>\d+)$', DataProfileDetail.as_view()),
]