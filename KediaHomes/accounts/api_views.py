from django.utils.decorators import decorator_from_middleware
from .middleware import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializer import AuthUserSerializer
from datetime import datetime
from rest_framework import status


@api_view(['POST'])
@decorator_from_middleware(UserLoginMiddleware)
def api_user_login_view(request, form):
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']
    user_obj = User.objects.get(email=email)
    if user_obj.check_password(password):
        serializer = TokenObtainPairSerializer(data=form.cleaned_data)
        token = serializer.validate({'email': email, 'password': password})['access']
        user_obj.token = token
        user_obj.last_login = datetime.now()
        user_obj.save()
        serializer = AuthUserSerializer(instance=user_obj, many=False)
        data = {'user': serializer.data}
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({"data": "Password is not Correct"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@decorator_from_middleware(APIRegisterMiddleware)
def api_register_view(request, form):
    serializer = AuthUserSerializer(data=form.cleaned_data)
    if serializer.is_valid():
        serializer.save()
        input_data = {'email': form.cleaned_data['email'], 'password': form.cleaned_data['password']}
        token_serializer = TokenObtainPairSerializer(data=input_data)
        token = token_serializer.validate(input_data)['access']
        update_serializer = AuthUserSerializer(
            instance=User.objects.get(email=form.cleaned_data['email']),
            data={"token": token, "last_login": datetime.now()},
            partial=True
        )
        if update_serializer.is_valid():
            update_serializer.save()
            return Response(data=update_serializer.data, status=200)
        else:
            return Response(data=update_serializer.errors, status=500)
    else:
        return Response(data=serializer.errors, status=500)


@api_view(['PUT', 'GET'])
@decorator_from_middleware(AuthenticationMiddleware)
@decorator_from_middleware(APIProfileMiddleware)
def api_profile_update_view(request, form=None):
    if request.method == "PUT":
        serializer = AuthUserSerializer(instance=request.user, data=form.cleaned_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=200)
        else:
            return Response(data=serializer.errors, status=500)
    else:
        serializer = AuthUserSerializer(instance=request.user, many=False)
        return Response(data=serializer.data, status=200)
