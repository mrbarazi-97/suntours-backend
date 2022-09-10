from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserRegisterSerializer



class UserRegister(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            User.objects.create_user(
                phone_number=ser_data.validated_data['phone_number'],
                email=ser_data.validated_data['email'],
                password=ser_data.validated_data['password'],
                full_name=ser_data.validated_data['full_name'],
            )

            return Response(ser_data.data)

        return Response(ser_data.errors)




# phone_number, email, full_name, password





