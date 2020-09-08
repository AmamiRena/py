from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView,ListView)
from .models import Question,Answer
from .forms import QuestionForm,AnswerForm

# Create your views here.

class CreateQuestionView(CreateView):
    model=Question
    form_class=QuestionForm
    template_name='questions/ask_question.html'

    def form_valid(self,form):
        question=form.save(commit=False)
        question.user=self.request.user
        question.save()
        messages.success(self.request,'The question was created with success!')
        return redirect('questions:question_detail',question.pk)

class QuestionListView(ListView):
    model=Question
    ordering=('update_date')
    context_object_name='questions'
    template_name='questions/questions_list.html'
    queryset=Question.objects.all()
    paginate_by=10

class QuestionDetailView(CreateView):
    model=Answer
    form_class=AnswerForm
    template_name='questions/question_detail.html'

    def get_context_data(self,**kwargs):
        question_id=self.kwargs.get('pk')
        question=Question.objects.get(pk=question_id)
        kwargs['question']=question
        if Answer.objects.filter(question=question):
            kwargs['answers']=Answer.objects.filter(question=question)
        context=super().get_context_data(**kwargs)
        return context

def create_answer(request,pk):
    if request.method=='POST':
        form=AnswerForm(request.POST)
        if form.is_valid():
            answer=Answer()
            answer.user=request.user
            answer.question=Question.objects.get(pk=pk)
            answer.description=form.cleaned_data.get('description')
            answer.save()

            messages.success(request,'The answer was created with success!')

            return redirect('questions:question_detail',answer.question.pk)
    return redirect('questions:question_detail',pk)
