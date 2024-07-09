from django.http import JsonResponse
import json

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .User import create_user, get_user_by, update_user_by, delete_user_by

@method_decorator(csrf_exempt, name='dispatch')
class UserController(View):
    def post(self, request):
        body = json.loads(request.body)
        username = body['username']
        birth_date = body['birth_date']
        email = body['email']
        create_user(username, birth_date, email)
        return JsonResponse({'message': 'User created successfully'}, status=201)

    @csrf_exempt
    def get(self,request, id):
        user = get_user_by(id)
        user_information = {
            'username': user.username,
            'birth_date': user.birth_date.strftime('%Y-%m-%d'),
            'email': user.email
        }
        return JsonResponse(user_information, status=200)

    @csrf_exempt
    def delete(self,request, id):
        delete_user_by(id)
        return JsonResponse({'message': 'User deleted successfully'}, status=204)

    @csrf_exempt
    def put(self,request, id):
        body = json.loads(request.body)
        update_user_by(id, body['email'])
        return JsonResponse({'message': 'User created successfully'}, status=202)
