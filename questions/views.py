from lib2to3.fixes.fix_input import context
from tempfile import template

from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .forms import QuestionForm, QuestForm
from .models import Questions
from django.core.paginator import Paginator

def index(request):
    templ = 'questions/index.html'
    objs = Questions.objects.select_related('category')
    paginator = Paginator(objs,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj }
    return render(request, templ, context)


def seek(request):
    form = QuestForm(request.GET or None)
    templ = 'questions/quest.html'
    context = {'form': form}
    if form.is_valid():
        templ = 'questions/index.html'
        value = request.GET['quest'].strip()
        objs = Questions.objects.filter(questions__contains=value.strip())
        context = {'page_obj': objs}
        return render(request, templ, context )
    return render(request, templ, context)


def question(request, pk=None):
    if pk is not None:
        instance = get_object_or_404(Questions, id=pk)
    else:
        instance = None

    form = QuestionForm(request.POST or None, instance=instance)
    templ = 'questions/question.html'
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, templ, context)


def detail(request, pk):
    answer_disp = request.GET.get('answer')
    answer_correct = Questions.objects.get(id=pk)
    print(answer_correct)
    if answer_disp.strip() == answer_correct:
        print('TRUE')
    templ = 'questions/detail.html'
    context = {'correct': answer_correct,
               'answer_disp': answer_disp}
    return render(request, templ, context)