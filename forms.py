from django import forms

import validators


class SerializedJSONField(forms.CharField):
    empty_values = list(validators.EMPTY_SERIALIZED_JSON_VALUES)

