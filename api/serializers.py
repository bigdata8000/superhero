from rest_framework import serializers 
from hero_app.models import Hero


class HeroSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Hero
        fields = ('hero_name', 'full_name', 'universe')

