# views.py
from django.shortcuts import render
from . import models


def choice_predictor_display(request):
    if request.method == 'POST':
        rank = float(request.POST.get('rank'))
        category = request.POST.get('category')
        round_num = float(request.POST.get('round'))
        year = float(request.POST.get('year'))
        gender = request.POST.get('gender')

        df = models.data.objects.filter(
            round=round_num,
            year=year,
            Gender=gender,
            Opening_rank__lte=rank,
            Closing_rank__gte=rank,
            Category=category
        )

        context = {'df': df}

        return render(request, 'choice_predictor_display.html', context)
    else:
        return render(request, 'choice_predictor_display.html')


def menu_page(request):
    return render(request, 'menu_page.html')


def choice_predictor(request):
    return render(request, 'choice_predictor.html')


def branch_wise_trends(request):
    return render(request, 'branch_wise_trends.html')


def institute_wise_trends(request):
    return render(request, 'institute_wise_trends.html')


def home_page(request):
    return render(request, 'home_page.html')


def institute_wise_trends_display(request):
    category = str(request.POST.get("category"))
    gender = str(request.POST.get("gender"))
    branch = str(request.POST.get("branch"))
    df1 = models.data.objects.filter(
        Branch__icontains=branch.strip(),
        round=6,
        Gender=gender,
        Category=category
    ).exclude(Branch__icontains='Dual Degree').order_by('year')

    df2 = models.data.objects.filter(
        Branch__icontains=branch.strip(),
        round=6,
        Gender=gender,
        Category=category,
        year=2021
    ).exclude(Branch__icontains='Dual Degree').order_by('year')

    context = {
        'df1': df1,
        'df2': df2
    }

    return render(request, 'institute_wise_trends_display.html', context)


def branch_wise_trends_display(request):
    category = str(request.POST.get("category"))
    gender = str(request.POST.get("gender"))
    iit = str(request.POST.get("iit"))
    df1 = models.data.objects.filter(
        round=6,
        Gender=gender,
        Category=category,
        institute=iit
    ).order_by('year')
    df2 = models.data.objects.filter(
        round=6,
        Gender=gender,
        Category=category,
        institute=iit,
        year=2022
    ).order_by('year')
    context = {
        'df1': df1,
        'df2': df2
    }

    return render(request, 'branch_wise_trends_display.html', context)
