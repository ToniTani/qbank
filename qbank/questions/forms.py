from django.forms import ModelForm
from .models import Question

class CreateQuestion(ModelForm):
    class Meta:
        model = Question
        fields = ['questiontitle', 'answer', 'important']
