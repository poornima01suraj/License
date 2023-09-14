from rest_framework import serializers
from .models import License

class LicenseSerializer(serializers.ModelSerializer):
    validity_months = serializers.IntegerField(min_value=1, max_value=12, required=True)

    class Meta:
        model = License
        fields = ['start_date', 'validity_months', 'device_id', 'nmssecuritykey', 'mac_address', 'server_ip']
