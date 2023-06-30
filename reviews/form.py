from django import forms
from .models import ReviewData



# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name",max_length=100)
#     email = forms.EmailField()
#     review_text = forms.CharField(label="your feedback", widget=forms.Textarea , max_length=300)
#     rating = forms.IntegerField(label="your rating" , min_value=1,max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewData
        field = "__all__ "
        exclude = []



