from typing import Type

from django.db.models import QuerySet
from rest_framework import serializers, viewsets
from services.models import CloudServiceProvider


class CloudServiceProviderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializers define the API representation.
    """
    class Meta:
        model: Type[CloudServiceProvider] = CloudServiceProvider
        fields: str = '__all__'


class CloudServiceProviderViewSet(viewsets.ModelViewSet):
    """
    ViewSets define the view behavior
    Attributes:
        queryset (QuerySet):
        serializer_class (HyperlinkedModelSerializer):
    """
    queryset: QuerySet = CloudServiceProvider.objects
    serializer_class: serializers.HyperlinkedModelSerializer = CloudServiceProviderSerializer
