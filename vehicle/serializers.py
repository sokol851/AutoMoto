from rest_framework import serializers

from vehicle.models import Car, Moto, Milage


class CarSerializer(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source='milage_set.all.first.milage')

    class Meta:
        model = Car
        fields = '__all__'


class MotoSerializer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    @staticmethod
    def get_last_milage(instance):
        milage = instance.milage_set.all().first()
        if not milage:
            return 0
        return milage.milage


class MilageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = '__all__'
