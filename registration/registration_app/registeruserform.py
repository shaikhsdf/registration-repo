from django.forms import ModelForm
from registration_app.models import newUser

class registeruserform(ModelForm):
    class Meta:
        model = newUser
        fields = '__all__'