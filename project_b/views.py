from django.shortcuts import render
from rest_framework.parsers import JSONParser,ParseError

# Create your views here.
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import License
from rest_framework import serializers
from django.core import serializers
from .serializers import LicenseSerializer
from datetime import datetime,timedelta
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.utils.decorators import method_decorator


# For register_license API
@swagger_auto_schema(
    method='post',
    request_body=LicenseSerializer,
    responses={201: 'License registered successfully', 400: 'Bad Request'}
)

### register into license using register_license##
@api_view(['POST'])
def register_license(request):## register first license
    serializer = LicenseSerializer(data=request.data)
    if serializer.is_valid():
        # Calculate the end date by adding the months to the start_date
        start_date = serializer.validated_data['start_date']
        validity_months = serializer.validated_data['validity_months']
        end_date = start_date + timedelta(days=validity_months * 30)  # Assuming 30 days in a month

        # Save the calculated validity (in days) to the model
        serializer.validated_data['validity'] = (end_date - start_date).days

        # Remove the 'validity' field from the data before saving the instance
        serializer.validated_data.pop('validity', None)

        # Save the instance to the database
        serializer.save()
        return Response({"message": "License registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  # For get_license API
@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('device_id', openapi.IN_PATH, description="Device ID", type=openapi.TYPE_INTEGER),
        openapi.Parameter('mac_address', openapi.IN_PATH, description="MAC Address", type=openapi.TYPE_STRING)
    ],
    responses={200: 'License data retrieved successfully', 404: 'Not Found'}
) 
 ## get_license with the help of server_ip address we can extract the data of whole license 
 # Process the results (e.g., get the first license, or summarize all licenses)
@api_view(['GET'])
def get_license(request, device_id, mac_address):
    try:
        licenses = License.objects.filter(device_id=device_id, mac_address=mac_address)
        if licenses.exists():
            license = licenses.first()
            data = {
                "nmssecuritykey": license.nmssecuritykey,
            }
            return Response(data)
        else:
            return Response({"error": "License not found"}, status=404)
    except License.DoesNotExist:
        return Response({"error": "License not found"}, status=404)




# For check_validity API
@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('device_id', openapi.IN_PATH, description="Device ID", type=openapi.TYPE_INTEGER),
        openapi.Parameter('mac_address', openapi.IN_PATH, description="MAC Address", type=openapi.TYPE_STRING)
    ],
    responses={200: 'License is valid or expired', 404:'Not Found'}
)




## checks the validity of the license if 0 then license is expired and if 1 license is valid##

@api_view(['GET'])
def check_validity(request, device_id, mac_address):
    try:
        licenses = License.objects.filter(mac_address=mac_address, device_id=device_id)
        if licenses.exists():
            license = licenses.first()

            # Calculate the end_date based on the start_date and validity_months
            start_date = license.start_date
            validity_months = license.validity_months

            # Calculate the end_date by adding the validity_months to the start_date
            end_date = start_date + timedelta(days=validity_months * 30)  # Assuming 30 days in a month

            # Check if the current date is before the end_date
            current_date = datetime.now().date()
            if current_date <= end_date:
                return Response({"valid": 1, "status": "valid"})
            else:
                return Response({"valid": 0, "status": "license expired"})
        else:
         return Response({"error": "Oops! License not found."}, status=404)
    except License.DoesNotExist:
            return Response({"error": "Oops! License not found."}, status=404)


