from django.db import router
from django.urls import path, include

from .views import AuthViews, CallBackViews, LinkedInCallBackView

urlpatterns = [
    path('auth/', AuthViews.as_view()),
    path('auth-callback/', CallBackViews.as_view()),
    path('signin-linkedin/', LinkedInCallBackView.as_view()),
]