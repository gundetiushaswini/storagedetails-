from rest_framework import serializers
from .models import storage



class storgeserializers(serializers.ModelSerializer):
    class Meta:
        model=storage
        fields = '__all__'
