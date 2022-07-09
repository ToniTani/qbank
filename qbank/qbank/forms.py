from django.form import modelForm
from .models import Question

class CreateQuestion(ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'answer', 'important']
