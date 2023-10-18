from django import forms
from .models import Ticket, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect,
        label='Note'
    )

    class Meta:
        model = Review
        fields = ['rating', 'headline', 'body', 'images']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, required=True, widget=forms.EmailInput()
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
