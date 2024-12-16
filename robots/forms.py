from django import forms
from robots.models import Robot
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from datetime import datetime


class RobotForm(ModelForm):
    class Meta:
        model = Robot
        fields = '__all__'

    def check_model(self):
        model = self.cleaned_data.get('model')
        if len(model) <= 1:
            raise ValidationError('Модель должна быть длиной не меньше 2 символа.')
        return model

    def check_version(self):
        version = self.cleaned_data.get('version')
        if len(version) <= 1:
            raise ValidationError('Версия должна быть длиной не меньше 2 символа.')
        return version

    def clean_created(self):
        created = self.cleaned_data.get('created')
        try:
            datetime.strptime(created, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise ValidationError('Неверный формат даты, должен быть YYYY-MM-DD HH:MM:SS.')
        return created
