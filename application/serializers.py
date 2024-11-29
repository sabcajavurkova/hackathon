from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'mac_address', 'is_in_school', 'is_present']

    def update(self, instance, validated_data):
        if instance.mac_address == validated_data.get('mac_address') and instance.is_in_school == False:
            instance.is_in_school = True
            instance.save()
        elif instance.mac_address == validated_data.get('mac_address') and instance.is_in_school == True:
            instance.is_in_school = False
            instance.save()
        return instance
    
    def update2(self, instance, validated_data):
        if instance.mac_address == validated_data.get('mac_address'):
            instance.is_present = True
            instance.save()
        return instance
