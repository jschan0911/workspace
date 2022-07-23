
from django import forms
from .models import myPost, myUser

class PostForm(forms.ModelForm):
    title = forms.CharField(label='', max_length=20,
        widget=forms.Textarea(attrs={'rows':'1', 'cols': '50', 'style':'font-size:35px; padding: 2%;'}))
    body = forms.CharField(label='', max_length=2000, 
        widget=forms.Textarea(attrs={'rows':'40', 'cols': '55', 'style':'font-size:35px; padding: 2%;'}))
    enddate = forms.DateField(required=False, label='',
        # widget=forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
        widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date', 'style':'font-size:35px; padding: 2%;'})
    )

    # enddate = forms.DateField(label='마감일(2022-01-01)', widget=forms.DateInput(attrs={'style':'font-size:15px'}))

    # enddate = forms.DateField(required=False, label='마감일(2022-01-01)')
    class Meta:
        model = myPost
        fields = '__all__'

class UserForm(forms.ModelForm):
    name = forms.CharField(label='이름', max_length=20,
        widget=forms.Textarea(attrs={'rows':'1', 'cols': '30', 'style':'font-size:15px; padding: 2%;'}))
    birthday = forms.DateField(required=False, label='생일',
        widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date', 'style':'font-size:15px; padding: 2%;'})
    )
    phone = forms.CharField(required=False, label='전화번호', max_length=20,
        widget=forms.Textarea(attrs={'rows':'1', 'cols': '30', 'style':'font-size:15px; padding: 2%;'}))

    age = forms.IntegerField(label='나이',
        widget=forms.NumberInput(attrs={'rows':'1', 'cols': '30', 'style':'font-size:15px; padding: 2%;'}))
    class Meta:
        model = myUser
        fields = '__all__'