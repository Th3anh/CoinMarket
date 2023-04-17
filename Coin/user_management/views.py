from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from user_management.models import Web3User
from user_management.serializers import Web3UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import *


class UserMeView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        content = {}
        serializer = Web3UserSerializer(Web3User.objects.get(pk = request.user.id))
        content["data"] = serializer.data
        content["message"] = "successfully fetched!"
        return Response(content, status = status.HTTP_200_OK)


class TokenView(generics.UpdateAPIView):
    serializer_class = TokenSerializer
    permission_classes = (IsAuthenticated,)

    def patch(self,request, pk, web3_address):
        try:
            users = Web3User.objects.get(web3_address=web3_address)
        except Web3User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        model = BNB.objects.get(id=pk)
        model.click_link.add(users)
        serializer = TokenSerializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get(self,request, web3_address):
        current_url = request.build_absolute_uri()
        new_url = current_url + '?ref=' + web3_address
        content = {'data': new_url}
        return Response(content, status = status.HTTP_200_OK)

        
    
class UserView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TokenSerializer
    queryset = BNB.objects.all()
