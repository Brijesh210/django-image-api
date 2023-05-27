from rest_framework import serializers

from ..models import Image, SizedTier, Tier, User, SizedImage


class SizedTierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SizedTier
        fields = '__all__ '
        depth = 2


class SizedImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SizedImage
        fields = '__all__'
        depth = 2


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    # image200 = serializers.CharField(source='sizedImages')
    class Meta:
        model = Image
        fields = ['title', 'image', 'sizedImages']
        depth = 2


class TierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tier
        fields = '__all__'
        depth = 2


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'tier']
