# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.postgres.fields import JSONField


from cat.models import Cat
from django_field_editor.widgets import JsonEditorWidget
from django_field_editor.fields import DjangoPostgersJsonField


# Style 1
@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):

    formfield_overrides = {
        JSONField: {'widget': JsonEditorWidget},
    }


# Style 2
# class CatModelForm(forms.ModelForm):
#     extend = DjangoPostgersJsonField()

#     class Meta:
#         model = Cat
#         exclude = []


# @admin.register(Cat)
# class CatAdmin(admin.ModelAdmin):

#     form = CatModelForm
