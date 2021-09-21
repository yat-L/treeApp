from rest_framework import serializers
from .models import Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('id','nid','name' ,'description', 'read_only', 'parent')
