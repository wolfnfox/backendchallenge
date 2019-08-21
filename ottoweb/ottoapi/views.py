from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ottoapi.models import Branch, Car, Driver
from ottoapi.serializers import BranchSerializer, CarSerializer, DriverSerializer

# Create your views here.
class BranchList(APIView):
    def get(self,request,format=None):
        branches = Branch.objects.all()
        branch_serializer = BranchSerializer(branches,many=True)
        return Response(branch_serializer.data)

    def post(self,request,format=None):
        branch_serializer = BranchSerializer(data=request.data)
        if branch_serializer.is_valid():
            branch_serializer.save()
            return Response(branch_serializer.data,status=status.HTTP_201_CREATED)
        return Response(branch_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BranchDetail(APIView):
    def get(self,request,branch_id,format=None):
        branch = self.retrieve_branch(branch_id)
        branch_serializer = BranchSerializer(branch)
        return Response(branch_serializer.data)

    def put(self,request,branch_id,format=None):
        branch = self.retrieve_branch(branch_id)
        branch_serializer = BranchSerializer(branch,data=request.data)
        if branch_serializer.is_valid():
            branch_serializer.save()
            return Response(branch_serializer.data)
        return Response(branch_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve_branch(self,branch_id):
        try:
            return Branch.objects.get(pk=branch_id)
        except Branch.DoesNotExist:
            raise Http404

class CarList(APIView):
    def get(self,request,format=None):
        cars = Car.objects.all()
        car_serializer = CarSerializer(cars,many=True)
        return Response(car_serializer.data)

    def post(self,request,format=None):
        car_serializer = CarSerializer(data=request.data)
        if car_serializer.is_valid():
            car_serializer.save()
            return Response(car_serializer.data,status=status.HTTP_201_CREATED)
        return Response(car_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CarDetail(APIView):
    def get(self,request,car_id,format=None):
        car = self.retrieve_car(car_id)
        car_serializer = CarSerializer(car)
        return Response(car_serializer.data)

    def put(self,request,car_id,format=None):
        car = self.retrieve_car(car_id)
        car_serializer = CarSerializer(car,data=request.data)
        if car_serializer.is_valid():
            car_serializer.save()
            return Response(car_serializer.data)
        return Response(car_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve_car(self,car_id):
        try:
            return Car.objects.get(pk=car_id)
        except Car.DoesNotExist:
            raise Http404