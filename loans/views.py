from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import HomePage, Loan_Company, LoanType, Faqs
from django.views import generic
from django.http import Http404
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'loans/index.html'
    context_object_name = 'loan_comp'   
   
    def get_queryset(self):
        """Return the published companies."""
        return Loan_Company.objects.order_by('-company_name')


class DetailView(generic.DetailView):

    model = Loan_Company
    template_name = 'loans/detail.html'

def quickloans(request):
    latest_loans_list = Loan_Company.objects.order_by('-loan_type')
    template = loader.get_template('loans/quickloans.html')
    context = {
        'latest_loans_list': latest_loans_list,
    }
    return HttpResponse(template.render(context, request))

def loantypes(request):
    latest_loans_list = LoanType.objects.order_by('-loan_name')[:5]
    template = loader.get_template('loans/loantypes.html')
    context = {
        'latest_loans_list': latest_loans_list,
    }
    return HttpResponse(template.render(context, request))

def faqs(request):
    faqs_list = Faqs.objects.order_by('-pub_date')[:5]
    template = loader.get_template('loans/faqs.html')
    context = {
        'faqs_list': faqs_list,
    }
    return HttpResponse(template.render(context, request))
