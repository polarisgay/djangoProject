from django.urls import path
from .views import HomePageView, AboutPageView, FeedbackPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('feedback/', FeedbackPageView.as_view(), name='feedback')
]
