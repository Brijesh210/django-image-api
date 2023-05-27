from rest_framework import viewsets
from imageapp.api.permissions import ImageOwner
from imageapp.api.serializers import ImageSerializer, TierSerializer, UserSerializer, SizedTierSerializer, \
    SizedImageSerializer
from imageapp.models import Image, Tier, SizedTier, SizedImage, User


class SizedTierViewSet(viewsets.ModelViewSet):
    queryset = SizedTier.objects.all()
    serializer_class = SizedTierSerializer


class SizedImageViewSet(viewsets.ModelViewSet):
    queryset = SizedImage.objects.all()
    serializer_class = SizedImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [ImageOwner]
    queryset = Image.objects.all()

    def get_queryset(self):
        if not self.request.user.pk:
            return None

        user = self.request.user

        # print(Image.objects.all().filter(user_id = user.id).filter(user__tier__tier_name__contains = "Basic"))
        return Image.objects.all().filter(user_id=user.id)

    def perform_create(self, serializer):
        # user  = self.request.user._wrapped
        # print(user.username)
        # print(type(user))
        # tierSizes = user.tier
        # print(type(tierSizes))
        # intSize = tierSizes.values_list('size')
        # print("hello")
        # print(intSize)
        serializer.save(user=self.request.user)


class TierViewSet(viewsets.ModelViewSet):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
