from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,**kwargs)

    class Meta:
        model = Review
        fields = ['tekst','opnieuwBekijken']
        labels = {'opnieuwBekijken': ('Opnieuw bekijken?')}
        widgets = {'tekst': Textarea(attrs={'rows': 8}),}