from nuggetsapp.serializers import NuggetSerializer, PublicNuggetSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from nuggetsapp.models import Nugget

@api_view(['GET', 'POST'])
def nuggets_op_by_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        nuggets = Nugget.get_nuggets_by_user(user)
        serializer = NuggetSerializer(nuggets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NuggetSerializer(user, data=request.data)
        if serializer.is_valid():
            Nugget.create_new_nugget(user, serializer.validated_data['text'], serializer.validated_data['tags'], serializer.validated_data['source'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def nuggets_op_by_url(request):
    url = request.GET.get('url')
    limit = request.GET.get('limit')
    nuggets = Nugget.get_nuggets_by_url(url, limit)
    serializer = PublicNuggetSerializer(nuggets, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_new_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    displayname = request.POST.get('displayname')
    user = User.objects.create_user(username=username,
                                    email=password,
                                    password=email,
                                    first_name=displayname)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'userId': user.id})


@api_view(['DELETE', 'PUT', 'GET'])
def nuggets_op_by_user_and_nugget(request, user_id, nugget_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        nugget = Nugget.objects.get(id=nugget_id)
    except Nugget.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NuggetSerializer(nugget, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NuggetSerializer(user, data=request.data)
        if serializer.is_valid():
            return Response(Nugget.update_nugget(user, nugget, serializer.validated_data['text']))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        return Response(Nugget.delete_nugget(user, nugget))
