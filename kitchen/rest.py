from typing import Type, Iterable

from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User, UserManager
from rest_framework.routers import SimpleRouter

from services.rest import CloudServiceProviderViewSet


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Type[User] = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset: UserManager = User.objects
    serializer_class: Type[UserSerializer] = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
rest_router: SimpleRouter = routers.SimpleRouter()
rest_router.register(r'user', UserViewSet)
# Routers provide an easy way of automatically determining the URL conf.
rest_router.register(r'cloud_service', CloudServiceProviderViewSet)
