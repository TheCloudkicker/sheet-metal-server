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


class PurchaseOrdersListAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        response = "post"

        return Response(response, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        response = "get"

        return Response(response, status=status.HTTP_200_OK)


class PurchaseOrdersDetailAPI(APIView):
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
