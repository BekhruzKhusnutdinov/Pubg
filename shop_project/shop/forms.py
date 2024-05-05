from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(forms.ModelForm):
    name = forms.CharField(label='Имя пользователя')  # Добавляем поле для имени пользователя
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    email = forms.EmailField(label='Электронная почта')
    number = forms.CharField(label='Номер')

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'password', 'number']  # Добавляем поле "name" в список полей

    def save(self, commit=True):
        user_profile = super(RegisterForm, self).save(commit=False)
        user = User.objects.create_user(username=self.cleaned_data['name'],
                                        # Используем поле "name" в качестве имени пользователя
                                        email=self.cleaned_data['email'],
                                        password=self.cleaned_data['password'])
        user_profile.user = user
        if commit:
            user_profile.save()
        return user_profile
