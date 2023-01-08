from diseases.models import Disease
from diseases.models import Clinic
from diseases.models import User
from diseases.models import Story
from rest_framework import serializers

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ["pk", "name", "doctor", "description"]

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ["pk", "address", "contact"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "name", "password"]

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ["pk", "dateReceipt", "dateDischarge", "status"]