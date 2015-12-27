from django import forms


from core.models import *



class GoalForm(forms.ModelForm):
    """ Creates a Form for the generic top-level assets """
    name = forms.CharField(label="Name")
    desc = forms.CharField(widget=forms.Textarea
                                ,label="Desc") 

    class Meta:
        model = Goal
        fields = ('short_name', 'long_desc','is_private')




class EntryForm(forms.ModelForm):
    """ Creates a Form for the generic top-level assets """
    date = forms.DateTimeField(label="Date of entry")
    number = forms.IntegerField(label="Number")
    count = forms.FloatField(label="Number")
    text = forms.CharField(widget=forms.Textarea
                                ,label="Text") 

    class Meta:
        model = Entry
        fields = ('pub_date', 'int_entry','float_entry','text_entry')



class UserForm(forms.ModelForm):
    """ 
    Creates a Form for the User/UserProfile model 
    Also has required confirm fields with supporting clean/error methods
    """

    confirm_email = forms.EmailField(
        label="Confirm Email",
        required=True,
    )
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Confirm Password",
        required=True,
    )
    
    class Meta:
        """ Overrides Meta property to user User model and defines and orders fields  """
        model = User
        fields = ('username','first_name' ,'last_name', 'email', 'confirm_email', 'password', 'confirm_password' )
        
    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email'] = email
            password = kwargs['instance'].password
            kwargs.setdefault('initial', {})['confirm_password'] = password

        return super(UserForm, self).__init__(*args, **kwargs)
    
    def clean(self):
        """ Overrides cleam method to support confirm fields """
        valid_text = ""
        if (self.cleaned_data.get('email') !=
            self.cleaned_data.get('confirm_email')):
            self._errors['email'] = "Email addresses must match."
            self._errors['confirm_email'] = "Email addresses must match."
            valid_text += " Email addresses must match. "
        if (self.cleaned_data.get('password') !=
            self.cleaned_data.get('confirm_password')):
            self._errors['password'] = "Passwords must match."
            self._errors['confirm_password'] = "Passwords must match."
            valid_text += " Passwords must match. "
        if valid_text != "":
            raise ValidationError(valid_text)
        return self.cleaned_data