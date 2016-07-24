from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField()
    gender_options = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender = forms.ChoiceField(label='Gender', widget=forms.Select, choices=gender_options)
    mobile = forms.CharField(max_length=20)
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput)
    dob = forms.DateField(label='date of birth', widget=forms.SelectDateWidget)