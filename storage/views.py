from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
from .models import storage
from.serializers import storgeserializers 
from rest_framework.pagination import PageNumberPagination

class customer_Pagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'limit'
    max_page_size = 100

class storagelistcreateview(generics.ListCreateAPIView):
    serializer_class = storgeserializers
    pagination_class = customer_Pagination
    
   
    def get_queryset(self):
        queryset = storage.objects.all()
        name = self.request.query_params.get('name', None)
        sort = self.request.query_params.get('sort', None)

        if name:
            queryset = queryset.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if sort:
            queryset = queryset.order_by(sort)
        return queryset

class storagedetailsviews(generics.RetrieveUpdateDestroyAPIView):
    queryset = storage.objects.all()
    serializer_class = storgeserializers