from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class GebruikerRegistratieForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(GebruikerRegistratieForm, self).__init__(*args,**kwargs)
        for fieldname in ['username', 'password1','password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-klasse'})
        self.fields['username'].label = "Gebruikersnaam"
        self.fields['password1'].label = "Wachtwoord"
        self.fields['password2'].label = "Bevestig wachtwoord"

class GebruikersAuthenticatieForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(GebruikersAuthenticatieForm, self).__init__(*args,**kwargs)
        self.fields['username'].label = "Gebruikersnaam"
        self.fields['password'].label = "Wachtwoord"
