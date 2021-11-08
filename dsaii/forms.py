from django import forms

from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control' })
        }


class CF(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control' })
        }