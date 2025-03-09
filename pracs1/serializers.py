from rest_framework import serializers
from pracs1.models import Student

# Creating our serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"