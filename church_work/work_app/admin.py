from django.contrib import admin
from .models import myPost, myUser
from django.db import models
from django.forms import Textarea, TextInput

admin.site.register(myUser)
admin.site.register(myPost)