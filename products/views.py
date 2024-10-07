from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import PermissionDenied


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        product = self.get_object()
        if product.user == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied ("You can only edit your own products.")
