from rest_framework import serializers
from .models import Invoice


class Invcserializer(serializers.ModelSerializer):
    class Meta: # nested class to provide meta data
        model = Invoice
        fields = ('id', 'name', 'desciption', 'total', 'paid')
