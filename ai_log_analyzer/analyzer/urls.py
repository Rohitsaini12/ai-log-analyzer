from django.urls import path
from .views import upload_log, log_summary

urlpatterns = [
    path('upload-log/', upload_log),
    path('log-summary/<int:log_id>/', log_summary),
]