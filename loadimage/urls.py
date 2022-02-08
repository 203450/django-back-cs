from django.urls import path, re_path
from django.conf.urls import include

#Importacion de las vistas

from loadimage.views import LoadFilesTable,LoadFilesTableDetail

urlpatterns = [
    re_path(r'^form/$', LoadFilesTable.as_view()),
    re_path(r'^form/(?P<pk>\d+)$', LoadFilesTableDetail.as_view()),    
] 