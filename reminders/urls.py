from django.urls import path
from .views import ReminderCreateView

urlpatterns = [
    path('', ReminderCreateView.as_view(), name='create-reminder'),
]