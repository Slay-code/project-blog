from django import forms

from mysite.models import Game, CategoryGame


class AddPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=CategoryGame.objects.all())
    
    class Meta:
        model = Game
        fields = ('name', 'slug', 'description', 'category')