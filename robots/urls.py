from django.urls import path
from robots.views import RobotView, DownloadReportView


urlpatterns = [
    path('create/', RobotView.as_view(), name='robot-create'),
    path('download_report/', DownloadReportView.as_view(), name='download-report')
]
