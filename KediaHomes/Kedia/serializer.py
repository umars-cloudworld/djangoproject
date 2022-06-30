from rest_framework import serializers
from .models import *


class PricingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pricing
        fields = ('title', 'description', 'is_active')


class ProjectsSerializer(serializers.ModelSerializer):
    projects_details = PricingSerializer(many=True)

    class Meta:
        model = Projects
        fields = "__all__"


class MapSerializer(serializers.ModelSerializer):

    class Meta:
        model = Map
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = "__all__"


class NewsLetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsLetter
        fields = "__all__"
