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

from ..models.job import Job


class JobsListAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        response = "post"

        return Response(response, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        response = []
        for job in Job.objects.all():
            response.append(
                {
                    "id": job.id,
                    "key": job.id,
                    "name": job.name,
                    "start_date": "1-1-2023",
                    "end_date": "12-31-2023",
                    "percent_complete": 70,
                    "target_margin": 35,
                    "current_margin": 40,
                    "num_issues": 2,
                }
            )

        return Response(response, status=status.HTTP_200_OK)


class JobsDetailAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, pk, *args, **kwargs):
        response = f"post {pk}"

        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        response = f"delete {pk}"

        return Response(response, status=status.HTTP_200_OK)

    def get(self, request, pk, *args, **kwargs):
        response = f"get {pk}"

        return Response(response, status=status.HTTP_200_OK)
