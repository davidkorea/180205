from django.shortcuts import render
from webapp.models import Caselog

def default(request):
    context = {
        'Caselog':Caselog.objects.all()
    }
    return render(request, 'default.html', context)