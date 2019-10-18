from django.db import models
from django.contrib.auth.models import User

PHONE_CHOICES=[
    ('Yes','Yes'),
    ('No','No')
]

MULTIPLE_CHOICES=[
    ('Yes','Yes'),
    ('No','No'),
    ('No phone service','No phone service')
]

INTERNET_CHOICES=[
    ('DSL','DSL'),
    ('Fiber optic','Fiber optic'),
    ('No','No')
]

ONLINESEC_CHOICES=[
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('No internet service', 'No internet service')
]
ONLINEBAC_CHOICES=[
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('No internet service', 'No internet service')
]
STREAMOV_CHOICES=[
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('No internet service', 'No internet service')
]
STREAMTV_CHOICES=[
    ('Yes','Yes'),
    ('No','No'),
    ('No internet service','No internet service')
]
CONTRACT_CHOICES=[
    ('One year','One year'),
    ('Month-to-month','Month-to-month'),
    ('Two year','Two year')
]
PAYMENT_CHOICES=[
    ('Bank transfer (automatic)','Bank transfer (automatic)'),
    ('Credit card (automatic)','Credit card (automatic)'),
    ('Electronic check','Electronic check'),
    ('Mailed check','Mailed check')
]
TECH_CHOICES=[
    ('Yes','Yes'),
    ('No','No'),

]

GENDER_CHOICES = [
   ('Male', 'Male'),
   ('Female', 'Female'),

]



class Predict(models.Model):
    full_name=models.CharField(max_length=50,default=1)
    address=models.CharField(max_length=50,default=1)
    phone_no=models.IntegerField(default=1)
    email=models.CharField(max_length=50,default=1)
    gender=models.CharField(choices=GENDER_CHOICES,default=1,max_length=50)
    image=models.FileField(upload_to='inputimage',blank=True)
    internet_service = models.CharField(choices=INTERNET_CHOICES, max_length=50,default=1)
    tenure = models.IntegerField(default=1)
    phone_service=models.CharField(choices=PHONE_CHOICES,max_length=50,default=1)
    multiple_lines=models.CharField(choices=MULTIPLE_CHOICES,max_length=50,default=1)
    contract=models.CharField(choices=CONTRACT_CHOICES,max_length=50,default=1)
    payment=models.CharField(choices=PAYMENT_CHOICES,max_length=50,default=1)
    online_security=models.CharField(choices=ONLINESEC_CHOICES,max_length=50,default=1)
    online_backup=models.CharField(choices=ONLINEBAC_CHOICES,max_length=30,default=1)
    stream_tv=models.CharField(choices=STREAMTV_CHOICES,max_length=50,default=1)
    stream_mov=models.CharField(choices=STREAMOV_CHOICES,max_length=50,default=1)
    tech_support=models.CharField(choices=TECH_CHOICES,max_length=50,default=1)

    def __str__(self):
        return self.full_name

class Churn(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    internet_service = models.CharField(choices=INTERNET_CHOICES, max_length=50, default=1)
    contract = models.CharField(choices=CONTRACT_CHOICES, max_length=50, default=1)
    payment = models.CharField(choices=PAYMENT_CHOICES, max_length=50, default=1)


    def __str__(self):
        return self.name

class Nonchurn(models.Model):
    non_name=models.CharField(max_length=50)
    non_address=models.CharField(max_length=50)
    phone=models.IntegerField()
    noninternet_service = models.CharField(choices=INTERNET_CHOICES, max_length=50, default=1)
    noncontract = models.CharField(choices=CONTRACT_CHOICES, max_length=50, default=1)
    nonpayment = models.CharField(choices=PAYMENT_CHOICES, max_length=50, default=1)

    def __str__(self):
        return self.non_name


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_no = models.IntegerField()


def __unicode__(self):
    return self.user.username



