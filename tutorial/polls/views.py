from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["GET"])
def index(request):
    return HttpResponse("Hello Polls World! Your'e at the polls index page!")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
