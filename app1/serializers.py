from rest_framework import serializers
from app1.models import Details



class DetailsSerializers(serializers.Serializer):
    cname = serializers.CharField(max_length =10)
    dur =serializers.IntegerField(max_length =10)
    fee =serializers.IntegerField(max_length =10)





