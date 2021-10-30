from django import forms
class f1(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    #mobile=forms.CharField()


class f2(forms.Form):
    Address=forms.CharField(max_length=122)
    Street_name=forms.CharField(max_length=122)
    Near_location=forms.CharField(max_length=122)
   # image=forms.ImageField(max_length=122)
    
    #mobile=forms.CharField(max_length=122)