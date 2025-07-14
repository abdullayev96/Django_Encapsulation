# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer
from .services import CustomerService






class CustomerCreateAPIView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            customer = CustomerService.create_customer(**data)
            return Response(CustomerSerializer(customer).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CustomerUpdateAPIView(APIView):
    def put(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'detail': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            data = serializer.validated_data
            updated_customer = CustomerService.update_customer(customer, **data)
            return Response(CustomerSerializer(updated_customer).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

