from django.forms import ModelForm #importing Modelform
from .models import Room #importing Room database table from models
from django.contrib.auth.models import User
#Here we create forms to create,update or delete elements in any database table from outside the admin-panel.
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' #It just includes every single information of any room in database table in the form. 
        exclude = ['host', 'participants'] #Excludes host and participants in the form of creating room.

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']