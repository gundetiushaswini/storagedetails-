from django.urls import path
from storage import views

urlpatterns = [
    path('a', views.storagelistcreateview.as_view()),
    path('b/<int:pk>', views.storagedetailsviews.as_view()),

]
