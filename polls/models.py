from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

# Here, each model is represented by a class that subclasses django.db.models.Model.
# Each model has a number of class variables, each of which represents a database field in the model.

# Each field is represented by an instance of a Field class – e.g., CharField for character fields and DateTimeField for datetimes.
# This tells Django what type of data each field holds.

# MIGRATE
# The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according
# to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later).

# MAKEMIGRATIONS
# By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
# Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):  # toString() equivalent
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
