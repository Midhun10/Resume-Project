from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from fresher.forms import RegistrationForm, ResumeForm
from fresher.models import Resume


# Create your views here.
def home(request):
    return render(request, "fresher/home.html")


def registration(request):
    form = RegistrationForm()
    context = {"form": form}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginPage")
        else:
            form = RegistrationForm(request.POST)
            context = {'form': form}
            return render(request, "fresher/register.html", context)
    return render(request, "fresher/register.html", context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("loginPage")

    return render(request, "fresher/login.html")


def logOut(request):
    logout(request)
    return redirect("home")


@login_required(login_url="loginPage")
def resume(request):
    form = ResumeForm(initial={"user": request.user})
    context = {"form": form}
    obj = Resume.objects.all()
    context["obj"] = obj
    if request.method == 'POST':
        form = ResumeForm(initial={"user": request.user}, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("resume")
    return render(request, "fresher/resumecreate.html", context)


@login_required(login_url="loginPage")
def editResume(request, pk):
    obj = Resume.objects.get(id=pk)
    form = ResumeForm(instance=obj)
    context = {"edit": form}
    if request.method == 'POST':
        obj = Resume.objects.get(id=pk)
        form = ResumeForm(instance=obj, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("resume")
    return render(request, "fresher/resumeedit.html", context)


@login_required(login_url="loginPage")
def viewResume(request, pk):
    obj = Resume.objects.filter(user=request.user, id=pk)
    context = {"form": obj}
    return render(request, "fresher/resumeview.html", context)


@login_required(login_url="loginPage")
def deleteResume(request, pk):
    obj = Resume.objects.filter(user=request.user, id=pk)
    obj.delete()
    return redirect("resume")


def listResume(request):
    obj = Resume.objects.all()
    context = {"list": obj}
    return render(request, "fresher/listresume.html", context)
