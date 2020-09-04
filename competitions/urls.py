from django.urls import path,include
from . import views
from competitions.views import LombaCreate, LombaUpdate, LombaDelete
from django.views.generic import TemplateView

urlpatterns = [
    path('detail/<int:pk>-<slug:slug>', views.detaillomba, name='detail_lomba'),
    path('bookmark/<int:pk>-<slug:slug>', views.bookmark, name='bookmark'),
    path('submit/', LombaCreate.as_view(), name='author-add'),
    path('detail/<int:pk>-<slug:slug>/update/', LombaUpdate.as_view(), name='author-update'),
    path('detail/<int:pk>-<slug:slug>/delete/', LombaDelete.as_view(), name='author-delete'),
    
]

app_name='competitions'