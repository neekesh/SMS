from rest_framework import serializers
from entry.models import Student


class StudentAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'age',
            'address',
            "grade",
            'major'
        ]

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

