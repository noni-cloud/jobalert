from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('post-job/', views.post_job, name='post_job'),
    path('subscribe/', views.subscribe_alert, name='subscribe_alert'),
    path('nearby/', views.nearby_jobs, name='nearby_jobs'),
    path('send-alerts/', views.send_alerts, name='send_alerts'),
]

