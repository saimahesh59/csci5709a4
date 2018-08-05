from django.shortcuts import render, redirect
from .models import Company, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    reviews = Review.objects.all()
    companies = Company.objects.all()
    context = {'reviews': reviews, 'companies': companies}
    return render(request, 'companies/home.html', context=context)


@login_required
def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            query, created = Company.objects.get_or_create(
                company_name=form.cleaned_data['company']
            )
            print(query)
            print(created)
            # todo , add company first -> get_or_create()
            #company = Company()
            review = Review()
            print(query.id)
            #company.company_name = form.cleaned_data['company']
            review.employee_position = form.cleaned_data['employee_position']
            review.rating = form.cleaned_data['rating']
            #review.company = company
            review.review = form.cleaned_data['review']
            review.company_id = query.id
            #company.save()
            review.save()
            return redirect('/companies/')
    form = ReviewForm()
    context = {'form': form}
    return render(request, 'companies/add_review.html', context=context)


def search(request):
    if request.is_ajax():
        print("this is axax")
    print('not x')
    return render(request, 'companies/add_review.html',)


def company(request, *args, **kwargs,):
    print(kwargs)
    id = kwargs['id']
    company = Company.objects.get(id=id)
    reviews = Review.objects.filter(company=id)
    context={'company': company, 'reviews': reviews}
    return render(request, "companies/company_profile.html", context=context)
