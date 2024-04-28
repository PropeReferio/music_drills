from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Category, Drill
import random


def index(request):
    categories = Category.objects.order_by("cat_name")
    template = loader.get_template("getdrills/choose_parameters.html")

    # 1st submit button should send user to "drills/<int:num_drills>"
    context = {
        "categories": categories,
    }
    return HttpResponse(template.render(context, request))

def all_drills(request):
    drills = Drill.objects.order_by("category")
    template = loader.get_template("getdrills/drills.html")
    context = {
        "drills": drills,
    }
    return HttpResponse(template.render(context, request))


def random_drills_by_int(request):
    num_drills = request.GET.get("num_drills")
    result = []
    drills = Drill.objects.order_by("category")
    list_of_drills = [x for x in drills]
    random.shuffle(list_of_drills)
    result.extend(list_of_drills[:int(num_drills)])
    template = loader.get_template("getdrills/drills.html")
    context = {
        "drills": result,
    }
    return HttpResponse(template.render(context, request))


def random_drills_by_int_and_category(request):
    result = []
    # TODO validate that requested drills do not exceed how many exist in category
    #  (here and above) currently it doesn't throw an error, it just returns the whole
    #  category
    for cat_id, num_requested in request.GET.items():
        if not num_requested:
            continue
        drills = Drill.objects.filter(category_id=cat_id).all()
        list_of_drills = [x for x in drills]
        random.shuffle(list_of_drills)
        result.extend(list_of_drills[:int(num_requested)])
    template = loader.get_template("getdrills/drills.html")
    context = {
        "drills": result,
    }
    return HttpResponse(template.render(context, request))
