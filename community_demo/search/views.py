from django.shortcuts import render,redirect
from django.db.models import Q
from questions.models import Question

# Create your views here.

def search(request):
    if 'q' not in request.GET:
        return redirect('')
    querystring=request.GET.get('q').strip()
    if len(querystring)==0:
        return redirect('home')
    results={'questions':Question.objects.filter(Q(title__icontains=querystring)|Q(description__icontains=querystring))}
    count={'questions':results['questions'].count()}
    context={'hide_search':True,'querystring':querystring,'count':count['questions'],'results':results['questions']}
    return render(request,'search/results.html',context)
