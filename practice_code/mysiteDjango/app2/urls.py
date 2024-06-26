from django.urls import path, re_path
from app2 import views

urlpatterns = [
    path('upload_file/', views.UploadFile.as_view()),
    re_path('book/(?P<year>[0-9]{2,4})/(?P<title>[a-zA-Z]{2})/$', views.book),

]