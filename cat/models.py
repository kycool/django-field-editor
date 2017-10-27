# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Cat(models.Model):
    """cat"""
    name = models.CharField('name', max_length=50, blank=True, default='')
    extend = JSONField('extend data', default={})

    def __str__(self):
        return self.name
