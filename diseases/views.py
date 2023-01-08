from rest_framework import viewsets
from diseases.serializers import DiseaseSerializer
from diseases.serializers import ClinicSerializer
from diseases.serializers import UserSerializer
from diseases.serializers import StorySerializer
from diseases.models import Disease
from diseases.models import Clinic
from diseases.models import User
from diseases.models import Story
# Create your views here.
class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all().order_by('doctor')
    serializer_class = DiseaseSerializer

class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all().order_by('address')
    serializer_class = ClinicSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by('dateReceipt')
    serializer_class = StorySerializer
