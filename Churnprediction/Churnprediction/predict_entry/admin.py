from django.contrib import admin
from predict_entry.models import Predict,Churn,Nonchurn,UserProfile

admin.site.register(Predict)
admin.site.register(Churn)
admin.site.register(Nonchurn)
admin.site.register(UserProfile)
# Register your models here.
