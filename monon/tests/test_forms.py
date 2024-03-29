from decimal import Decimal

from django.test import TestCase

from pymonon import Money, CURRENCIES

from .dummyapp.forms import MoneyForm, MoneyModelForm
from .dummyapp.models import ModelWithVanillaMoneyField


class MoneyFormTestCase(TestCase):
    
    def testRender(self):
        
        form = MoneyForm()
        expected = """<tr><th><label for="id_money">Money:</label></th><td><input type="text" name="money" /><select name="money_currency">
<option value="a">a</option>
</select></td></tr>"""
        
        self.assertEquals(str(form), expected)
        
    def testValidate(self):
        form = MoneyForm({"money":"10", "money_currency":"CLP"})
        
        self.assertTrue(form.is_valid())
        
        result = form.cleaned_data['money']
        self.assertTrue(isinstance(result, Money))
        
        self.assertEquals(result.amount, Decimal("10"))
        self.assertEquals(result.currency, CURRENCIES["CLP"])
        
    def testNonExistantCurrency(self):
        form = MoneyForm({"money":"10", "money_currency":"_XX!123_"})
        
        self.assertFalse(form.is_valid())
        
        
class MoneyModelFormTestCase(TestCase):
    
    def testSave(self):
        form = MoneyModelForm({"money":"10", "money_currency":"CLP"})
        
        self.assertTrue(form.is_valid())
        model = form.save()
        
        retrieved = ModelWithVanillaMoneyField.objects.get(pk=model.pk)
        
        self.assertEqual(Money(10, "CLP"), retrieved.money)
