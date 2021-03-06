from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from firstproject.polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("you're looking at question %s" % question_id)


def results(request, question_id):
    response = "you're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("you're voting on question %s" % question_id)


def sol(request, test_str):
    str = "test value %s"
    return HttpResponse(str % test_str)
