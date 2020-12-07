from django.contrib import admin

from .models import Question, Choice

# Register your models here so they can be modifiable from the admin console
admin.site.register(Question)
admin.site.register(Choice)
