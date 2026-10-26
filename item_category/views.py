from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions

from item_category.models import ProductCategory
from item_category.serializers import ProductCategorySerializer

class ProductCategoryListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

class ProductCategoryCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    serializer_class = ProductCategorySerializer

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)

class ProductCategoryRetrieveView(RetrieveAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

class ProductCategoryUpdateDeleteView(UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

    