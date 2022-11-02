from rest_framework import views, response, status
from django.shortcuts import get_object_or_404
from api.serializers import StudentAddSerializer
from entry.models import Student
from rest_framework.decorators import api_view

@api_view(['GET', "POST"])
def student_add(request):

    if request.method == "POST":
        serializer = StudentAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            {
                'msg': "Student Added",
                'status': status.HTTP_201_CREATED
            },
        )

    stud_set = Student.objects.all().order_by('name')
    serialize = StudentAddSerializer(stud_set, many=True)
    return response.Response(serialize.data)

@api_view(['DELETE'])
def student_delete(request, pk):
    if request.method == "DELETE":
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return response.Response(
            {
                'msg': "record deleted"
            }
        )

@api_view(['PUT'])
def student_update(request, pk):
    if request.method == "PUT":
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentAddSerializer(student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            {
                'msg': "record updated",
             },
        )
