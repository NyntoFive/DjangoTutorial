from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404

# from django.http import Http404
# from django.template import loader --- replaced in index()
# render(request_object, template_name, optional=context(dict_object)

from .models import Question

# comments replaced with render() shortcut
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


# Replaced try .get() /except with shortcut
def detail(request, question_id):
    # question = Question.objects.get(pk=question_id)
    return render(request, "polls/detail.html", {"question": question_id})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

