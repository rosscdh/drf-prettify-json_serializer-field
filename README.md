# drf-prettify-json-serializer

*You got ugly json, we got a serializer that can massage that data into something useful*

Sometimes you get "*json*", that you have NO control over and the json is ugly. I mean really Ugly and Inconsistant. 

So, being the control-freak that you are you decide to bring order to the chaos, but for some reason DRF does not allow data massaging. Which is a pity as its a a damned fine presenter pattern implementation but lacks this tiny bit of functionality.

so if source is defined it will read that from the provided json data.

**NB** this field class is for serialization of json data only.

For example:

```
{
    "customerID": "123",                     # lowercase uppercase
    "CustomerUID": "abc456",                 # CamelUpper
    "CustomerEmail": "bob@example.com",      # CamelCase
    "KundenKarteNr": "Ad0ek344",             # This is not a number and its not english
    "CardType": 1,                           # this one is ok, but CamelCase
    "Filial": "3",                           # not english and ugly
}
```

is brought under control like so:

```
from drf_prettify_json_serializer.fields import (Charfield,
                                                 EmailField,
                                                 DecimalField,
                                                 IntegerField)


class CustomerSerializer(serializers.Serializer):
    customer_id = IntegerField(source='customerID')
    customer_uid = CharField(source='CustomerUID', allow_null=True)
    email = EmailField(source='CustomerEmail', allow_null=True)
    card = CharField(source='KundenKarteNr')
    card_type = IntegerField(source='CardType')
    store = IntegerField(source='Filial')


{
    "customer_id": 123,
    "customer_uid": "abc456",
    "email": "bob@example.com",
    "card": "Ad0ek344",
    "card_type": 1,
    "store": 3,
}
```

And to add fields you simply

```
class ExistingField(PrettifyDataFromJsonField, serializers.ExistingField):
    pass
```
