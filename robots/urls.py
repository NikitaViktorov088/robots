from django.urls import path
from robots.views import RobotView


urlpatterns = [
    path('create/', RobotView.as_view(), name='robot-create')
]
