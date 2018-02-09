from django.shortcuts import render
from webapp.models import Caselog

def default(request):
    print('==='*30)
    print(request)
    print('==='*30)
    print(dir(request))
    print('==='*30)
    print(type(request))
    print('==='*30)
    queryset = request.GET.get('handleby')
    print(queryset)
    if queryset:
        caselog_list = Caselog.objects.filter(handleby=queryset)
    else:
        caselog_list = Caselog.objects.all()
    context = {
        'Caselog': caselog_list
    }
    return render(request, 'default.html', context)