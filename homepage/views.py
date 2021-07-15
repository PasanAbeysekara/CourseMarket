from django.shortcuts import render, redirect
from .forms import CreateCourse
from .models import Course


# Create your views here.
def home_view(request):
    courses = Course.objects.all()
    return render(request, 'homepage/home.html', {'courses': courses})


def django_view(request):
    # courses = [
    #     "Quora",
    #     "Food Store",
    #     "LMS",
    #     "School management system",
    #     "Bug Tracker"
    # ]
    courses = Course.objects.filter(category="Django")
    return render(request, 'homepage/django.html', {'courses': courses})


def angular_view(request):
    # courses = [
    #     "Facebook Clone",
    #     "Linkedin Clone"
    # ]
    courses = Course.objects.filter(category="Angular")
    return render(request, 'homepage/angular.html', {'courses': courses})


def asp_view(request):
    # courses = [
    #     "E-commerce",
    #     "LMS",
    #     "School Management System"
    # ]
    courses = Course.objects.filter(category="ASP.NET")
    return render(request, 'homepage/asp.html', {'courses': courses})


def createCourse_view(request):
    if request.method == "POST":
        form = CreateCourse(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage:home")
    else:
        form = CreateCourse()
    return render(request, 'homepage/createCourse.html', {'form': form})
