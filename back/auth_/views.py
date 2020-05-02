import json
import logging

from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, mixins, permissions, status

from auth_.models import Author
from auth_.serializers import AuthorSerializer

logger = logging.getLogger(__name__)


@csrf_exempt
def register(request):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')
    first_name = body.get('first_name')
    is_moderator = body.get('is_moderator')

    user = Author.objects.create_user(username=username)
    user.set_password(password)
    user.first_name = first_name
    user.is_moderator = is_moderator
    user.save()
    logger.info(f'Author with username {user.username} created')

    return JsonResponse({'message': f'Author with username {user.username} created'}, status=status.HTTP_201_CREATED)


@csrf_exempt
def logout(request):
    user = auth.logout(request)
    logger.info('Logged out')
    return JsonResponse({'message': 'Logged out'}, status=status.HTTP_200_OK)


class AuthorsListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
