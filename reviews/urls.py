from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReviewView.as_view()),
    path("thank-you", views.ThankyouView.as_view()),
    path("review", views.AllReviewView.as_view()),
    path("review/<int:pk>", views.SingleReviewView.as_view())   
]
   