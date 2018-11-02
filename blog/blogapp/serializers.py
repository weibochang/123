from rest_framework import serializers
from .models import Banner

# 类名固定为 表名称+Serializer
class BannerSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=50)
    # img = serializers.ImageField()
    # img_url = serializers.URLField(max_length=100)
    # index = serializers.IntegerField()
    # is_active = serializers.BooleanField(default=False)
    operator = serializers.ReadOnlyField(source='operator.username')
    class Meta:
        model = Banner
        fields = (
            'id',
            'title',
            'img',
            'img_url',
            'index',
            'is_active',
            'operator'
        )

    # def create(self,validated_data):
    #     return Banner.objects.create(**validated_data)
    # def update(self,instance,validated_data):
    #     instance.title = validated_data.get('title',instance.title)
    #     instance.img = validated_data.get('img',instance.img)
    #     instance.img_url = validated_data.get('img_url',instance.img_url)
    #     instance.index = validated_data.get('index',instance.index)
    #     instance.is_active = validated_data.get('is_active',instance.is_active)
    #     instance.save()
    #     return instance