from rest_framework import serializers
from .models import Student, Module


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["id", "module_name", "module_duration"]
        depth = 1


class StudentSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True)

    class Meta:
        model = Student
        fields = ["name", "age", "grade", "modules"]
