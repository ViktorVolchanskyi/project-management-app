from rest_framework import serializers

from apps.customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "name", "created_at")
        read_only_fields = ("id", "created_at")
