from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),        
    path('dialog/', views.dialog, name='dialog'),
    path('result/', views.ResultListView.as_view(), name='result'),
    path('tablet_detail/<pk>', views.TabletDetailView.as_view(), name='tablet_detail'),
    path('tablet_list/', views.TabletListView.as_view(), name='tablet_list'),
]
