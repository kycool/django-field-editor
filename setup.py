# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-json-editor',
    version='0.0.1',
    url='https://github.com/kycool/django-json-editor',
    author='kycool',
    author_email='kycoolcool@gmail.com',
    description='Django json field editor.',
    license='GPL',
    packages=['django_json_editor', 'django_json_editor.static'],
    include_package_data=True,
    zip_safe=False,
)
