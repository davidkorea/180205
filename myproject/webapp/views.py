from django.shortcuts import render
from webapp.models import Caselog, Comment
from webapp.form import CommentForm

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

def detail(request):
    if request.method == 'GET':
        form = CommentForm #创建表单
    if request.method == 'POST':
        form = CommentForm(request.POST) #绑定表单，实现数据校验
        print('==='*30)
        print(form)
        print('==='*30)
    form = CommentForm
    context = {}
    comment_list = Comment.objects.all()
    context['comment_list'] = comment_list
    context['form'] = form
    return render(request, 'log_detail.html', context)