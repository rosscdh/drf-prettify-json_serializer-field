# drf-prettify-json-serializer

*You got ugly json, we got a serializer that can massage that data into something useful*

Sometimes you get "*json*", that you have NO control over and the json is ugly. I mean really Ugly and Inconsistant. 

So, being the control-freak that you are you decide to bring order to the chaos, but for some reason DRF does not allow data massaging. Which is a pity as its a a damned fine presenter pattern implementation but lacks this tiny bit of functionality.

so if source is defined it will read that from the provided json data.

**NB** this field class is for serialization of json data only.

## Installation

```sh
pip install drf-prettify-json-serializer-field
```

## About

For example:

```
#
# argh! my eyes... dear lord! are we enterprise or what?
#
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
import drf_prettify_json_serializer_field.fields  as json_source_fields


class CustomerSerializer(serializers.Serializer):
    customer_id = json_source_fields.IntegerField(source='customerID')
    customer_uid = json_source_fields.CharField(source='CustomerUID', allow_null=True)
    email = json_source_fields.EmailField(source='CustomerEmail', allow_null=True)
    card = json_source_fields.CharField(source='KundenKarteNr')
    card_type = json_source_fields.IntegerField(source='CardType')
    store = json_source_fields.IntegerField(source='Sill.Seperator.Deepnested.Filial')

#
# ahh better
#
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

## TODO

1. tests
2. ~deep nested key references (dot seperated)~
