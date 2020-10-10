from django.urls import path
from fresher.views import home, registration, loginPage, resume, editResume, viewResume, deleteResume, logOut, \
    listResume, contact

urlpatterns = [

    path("", home, name="home"),
    path("register", registration, name="register"),
    path("login", loginPage, name="loginPage"),
    path("resume", resume, name="resume"),
    path('editresume/<int:pk>', editResume, name="editresume"),
    path('viewresume/<int:pk>', viewResume, name="viewresume"),
    path('deleteresume/<int:pk>', deleteResume, name="deleteresume"),
    path("listresume", listResume, name="listresume"),
    path("logOut", logOut, name="logoutPage"),
    path("contact", contact, name="contact"),

]
