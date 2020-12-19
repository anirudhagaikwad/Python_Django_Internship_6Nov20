from django import forms


GEN=(('','Choose'),('Male','Male'),('Female','Female'),('Other','Other'))


class MyForm(forms.Form):
    fname=forms.CharField(widget=forms.TextInput(attrs={'title': "Enter employee first name",'placeholder': "employee first Name"}),label="First Name",max_length=10,min_length=4,empty_value=False,required=True)     
    lname=forms.CharField(widget=forms.TextInput(attrs={'title': "Enter employee lastname name",'placeholder': "employee lastname Name"}),label="Last Name",max_length=10,min_length=4,empty_value=False,required=True)     
    address=forms.CharField(widget=forms.TextInput(attrs={'title': "Enter employee first name",'placeholder': "employee Address"}),label="Address",max_length=10,min_length=4,empty_value=False,required=True)     
    mobile=forms.CharField(widget=forms.TextInput(attrs={'title': "Enter employee first name",'placeholder': "employee mobile"}),label="Mobile",max_length=10,min_length=4,empty_value=False,required=True)     

class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'title':"Enter Your Name",'placeholder':"Your Name"}),label="Name",empty_value=False,required=True,max_length=10,min_length=4)   
    gender=forms.ChoiceField(widget=forms.Select(attrs={'title':"Enter Your Gender",'placeholder':"Your Gender"}),label="Gender",choices=GEN,required=True)   
    email=forms.CharField(widget=forms.EmailInput(attrs={'title':"Enter Your Email",'placeholder':"Your Email"}),label="Email",empty_value=False,required=True) 
    mobile=forms.CharField(widget=forms.NumberInput(attrs={'title':"Enter Your Mobile",'placeholder':"Your Mobile"}),label="Mobile",empty_value=False,required=True)  
    message=forms.CharField(widget=forms.Textarea(attrs={'title':"Enter Your Message",'placeholder':"Your Message"}),label="Message",empty_value=False,required=True)   