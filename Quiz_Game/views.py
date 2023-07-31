from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user':current_user}
        return render(request, 'base.html', param)
    else:
        return redirect('login')
    return render(request, 'Login.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        if User.objects.filter(username=uname).count()>0:
            return HttpResponse('Username already exist.')
        else:
            user = User(username=uname, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')
    
def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('home')
        else:
            return HttpResponse('Please enter valid Username or Password.')
    return render(request, 'login.html')
    
def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')

def quiz(request):
    results= Question.objects.all()
    return render(request, 'index.html', {'Question':results})
    
def result(request):
    results=Question.objects.all()
    wrong=0
    correct=0
    total=0
    for result in results:
        total+=1
        print(request.POST.get(result.question_text))
        print(result.ans)
        print()
        if result.ans ==  request.POST.get(result.question_text):
            correct+=1
        else:
            wrong+=1
    context = {
        'correct':correct,
        'wrong':wrong,
        'total':total
    }
    return render(request,'result.html',context)
    
def listing(request):
    quiz_list = Question.objects.all()
    paginator = Paginator(quiz_list, 3)

    pageNumber = request.GET.get('page')
    try:
        quizs = paginator.page(pageNumber)
    except PageNotAnInteger:
        quizs = paginator.page(1)
    except EmptyPage:
        quizs = paginator.page(paginator.num_pages)
    
    return render(request, 'index.html', {'Question':quizs})