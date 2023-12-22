from ogrenci.models import Ogrenci
from rest_framework import serializers


class OgrenciSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    surname=serializers.CharField()
    tel=serializers.CharField()
    mail=serializers.CharField()
    register_date=serializers.DateTimeField(read_only=True)
    average=serializers.IntegerField()
    still_student=serializers.BooleanField()
    
    def create(self,validated_data):
        print(validated_data)
        return Ogrenci.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.surname=validated_data.get('surname', instance.surname)
        instance.tel=validated_data.get('tel', instance.tel)
        instance.mail=validated_data.get('mail', instance.mail)
        instance.register_date=validated_data.get('register_date', instance.register_date)
        instance.average=validated_data.get('average', instance.average)
        instance.still_student=validated_data.get('still_student', instance.still_student)
        instance.save()
        return instance