from django.shortcuts import render, HttpResponseRedirect, redirect
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

def detail(request, page_num):
    if request.method == 'GET':
        form = CommentForm #创建表单
    if request.method == 'POST':
        form = CommentForm(request.POST) #绑定表单，实现数据校验
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            a= Caselog.objects.get(id=page_num)
            c = Comment(name = name, comment = comment, belong_to = a)
            c.save()
            return redirect(to='detail', page_num=page_num)
    context = {}
    # comment_list = Comment.objects.all()
    caselog = Caselog.objects.get(id=page_num)
    context['caselog'] = caselog
    # context['comment_list'] = comment_list
    context['form'] = form
    return render(request, 'log_detail.html', context)