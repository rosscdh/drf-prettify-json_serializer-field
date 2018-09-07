from rest_framework import serializers

try:
    from functools import reduce
except:
    # pyton 2 has reduce builtin
    pass


class PrettifyDataFromJsonField(serializers.Field):
    """
    Instead of using the field_name, for the value rather use the source
    as then we can massage ugly json data
    """
    def get_value(self, dictionary):
        if self.source is not None:
            data_source = self.source
        else:
            data_source = self.field_name

        if data_source not in dictionary:
            if getattr(self.root, 'partial', False):
                return serializers.empty
        # We override the default field access in order to support
        # lists in HTML forms.
        if serializers.html.is_html_input(dictionary):
            return dictionary.getlist(data_source)
        # account for dot notation
        if '.' in data_source:
            return reduce(dict.get, data_source.split('.'), dictionary)
        return dictionary.get(data_source, serializers.empty)


class CharField(PrettifyDataFromJsonField, serializers.CharField):
    pass


class EmailField(PrettifyDataFromJsonField, serializers.EmailField):
    pass


class DecimalField(PrettifyDataFromJsonField, serializers.DecimalField):
    pass


class IntegerField(PrettifyDataFromJsonField, serializers.IntegerField):
    pass