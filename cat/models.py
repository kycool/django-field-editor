# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.postgres.fields import JSONField


class Cat(models.Model):
    """cat"""
    name = models.CharField('name', max_length=50, blank=True, default='')
    extend = JSONField('extend data', default={})

    def __str__(self):
        return self.name
