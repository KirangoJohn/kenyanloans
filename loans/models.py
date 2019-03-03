from django.db import models

class LoanType(models.Model):
    loan_name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    requiremets = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now=True)

class LoanBenefits(models.Model):
    description = models.TextField(max_length=1000)

class HomePage(models.Model):
    description = models.TextField(max_length=1000)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

class Faqs(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField(max_length=1000)
    pub_date = models.DateField(auto_now=True)

class Loan_Company(models.Model):
    company_name = models.CharField(max_length=200)
    loan_type = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=1000)
    interest_rate = models.CharField(max_length=50, default='Varies with the loan applied')
    website = models.TextField(max_length=200, default='www')
    email = models.EmailField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, default=0, blank=True)
    payment_period = models.DurationField(default=0, blank=True)
    pub_date = models.DateField(auto_now=True)
    how_to = models.TextField(max_length=1000, default="How to apply")
    merits = models.TextField(max_length=1000, default="Why apply for this loan")
    requirements = models.TextField(max_length=1000, default="Requirements")


class Asset_Financing(models.Model): 
    company_name = models.CharField(max_length=200)



    