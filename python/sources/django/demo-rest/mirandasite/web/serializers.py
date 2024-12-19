import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from web.models import Car


# class CarModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class CarSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_created = serializers.DateTimeField(read_only=True)
    time_updated = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_updated = validated_data.get('time_updated', instance.time_updated)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance

# def encode():
#     model = CarModel('Hond', 'Honda Motors')
#     model_sr = CarSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title": "Hond", "content": "Honda Motors"}')
#     data = JSONParser().parse(stream)
#     serializer = CarSerializer(data = data)
#     serializer.is_valid()
#     print(serializer.validated_data)