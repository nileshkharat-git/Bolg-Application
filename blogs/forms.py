from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(max_length=100, label='Title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    article = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
