from django import forms
from monon.forms import MoneyField, CurrencySelectWidget
from models import ModelWithVanillaMoneyField


class MoneyForm(forms.Form):
    money = MoneyField(currency_widget=CurrencySelectWidget(choices=[("a", "a")]))


class MoneyModelForm(forms.ModelForm):

    class Meta:
        model = ModelWithVanillaMoneyField
