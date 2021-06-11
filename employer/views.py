from django.shortcuts import render

def personel(request):
    return render(request, 'employer/personel.html')

def active(request):
    return render(request, 'employer/active_personel.html')


def inactive(request):
    return render(request, 'employer/inactive_personel.html')