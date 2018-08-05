from django import forms


class ReviewForm(forms.Form):
    company = forms.CharField(label="Company Name", required=True, max_length=100,
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Company Name', 'class': 'form-control', }))
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Review', 'class': 'form-control', }))
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Rating',
                                                                'class': 'form-control', }))
    employee_position = forms.CharField(label="Position", max_length=50,
                                        widget=forms.TextInput(attrs={'placeholder': 'Position',
                                                                      'class': 'form-control', }))
