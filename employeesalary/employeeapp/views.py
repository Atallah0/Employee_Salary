from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializer import GradeSerializer, EmployeeSerializer
from .models import Grade, Employee

class Grades(APIView):
    permission_classes = (IsAdminUser,)

    def get_object(self, id):
        return Grade.objects.get(id=id)

    def get(self, request, id=None):
        if id:
            grade = self.get_object(id)
            serializer = GradeSerializer(grade)
        else:
            grades = Grade.objects.all()
            serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, id):
        grade = Grade.objects.get(id=id)
        serializer = GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, id):
        grade = Grade.objects.get(id=id)
        serializer = GradeSerializer(grade, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        grade = Grade.objects.get(id=id)
        grade.delete()
        return Response('Grade deleted successfully')

class Employees(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, id):
        return Employee.objects.get(id=id)

    def get(self, request, id=None):
        if id:
            employee = self.get_object(id)
            serializer = EmployeeSerializer(employee)
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, id):
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, id):
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        employee = Employee.objects.get(id=id)
        employee.delete()
        return Response('Employee deleted successfully')