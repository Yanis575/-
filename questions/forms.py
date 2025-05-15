from django import forms
from .models import Questions


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'


class QuestForm(forms.Form):
    quest = forms.CharField(label='Вопрос',max_length=100)

