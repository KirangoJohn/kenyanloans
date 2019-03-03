from django.contrib import admin

from .models import Loan_Company, LoanType, LoanBenefits, HomePage, Faqs

admin.site.register(Loan_Company)
admin.site.register(LoanType)
admin.site.register(LoanBenefits)
admin.site.register(HomePage)
admin.site.register(Faqs)



