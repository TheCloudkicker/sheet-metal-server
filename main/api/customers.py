import json

# DJANGO IMPORTS

from django.apps import apps
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect, reverse

# DJANGO REST IMPORTS
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status, generics, permissions
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..models.customer import Customer
from ..models.job import Job


class CustomersListAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        response = "post"

        return Response(response, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        response = []
        for customer in Customer.objects.all():
            response.append(
                {
                    "id": customer.id,
                    "key": customer.id,
                    "name": customer.name,
                    "num_jobs_in_progress": Job.objects.filter(
                        customer=customer
                    ).count(),
                }
            )

        return Response(response, status=status.HTTP_200_OK)


class CustomersDetailAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, pk, *args, **kwargs):
        response = f"post {pk}"

        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        response = f"delete {pk}"

        return Response(response, status=status.HTTP_200_OK)

    def get(self, request, pk, *args, **kwargs):
        customer = Customer.objects.get(pk=pk)
        response = {
            "id": customer.id,
            "key": customer.id,
            "name": customer.name,
            "num_jobs_in_progress": Job.objects.filter(customer=customer).count(),
        }

        return Response(response, status=status.HTTP_200_OK)
