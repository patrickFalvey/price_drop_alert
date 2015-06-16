from django import forms


class price_drop_alert_form(forms.Form):
    Desired_Price = forms.FloatField()
    
