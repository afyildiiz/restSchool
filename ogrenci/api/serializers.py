from ogrenci.models import Ogrenci
from rest_framework import serializers


class OgrenciSerializer(serializers.Serializer):
    # öğrenci modeli için Django modelini JSON formatına dönüştürmek (serialize etmek) ve tersine dönüştürmek (deserialize etmek) için
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    surname=serializers.CharField()
    tel=serializers.CharField()
    mail=serializers.CharField()
    register_date=serializers.DateTimeField(read_only=True)
    average=serializers.IntegerField()
    status=serializers.CharField(read_only=True)
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
        instance.status=validated_data.get("status",instance.status)
        instance.still_student=validated_data.get('still_student', instance.still_student)
        instance.save()
        return instance
    
    def validate(self,data):
        if data['name']==data['surname']:
            raise serializers.ValidationError('name and surname cannot be same!')
        return data
    
    def validate_name(self,value):
        if len(value)<=2:
            raise serializers.ValidationError(f"isim karakter sayisi {len(value)}'den fazla olmalidir.")
        return value