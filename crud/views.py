from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt,datetime

# Create your views here.
class Overview(APIView):
    def get(self,request):

        api_urls = {
            'current_user': '/user/',
            'create-user':'/register/',
            'login':'/login/',
            'logout':'/logout/',
            'update-user':'/update-user/<int:pk>',
            'delete-user':'/delete-user/<int:pk>',

        }

        return Response(api_urls)

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self,request):  
        username = request.data['username']  
        password = request.data['password']  
        user = User.objects.filter(username = username).first()

        if  user is None:
            raise AuthenticationFailed('user not found!')
        if not user.check_password(password):  
            raise AuthenticationFailed('Incorrect password!')

            # CREATE TOKEN

        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes = 60),
            'iat':datetime.datetime.utcnow()
        }    
        token = jwt.encode(payload,'secret',algorithm='HS256')

        # CREATE COOKIE
        
        response = Response()
        response.set_cookie(key = 'jwt',value = token , httponly = True)
        response.data = {
            'message':'Logged in successfully!',
            'token':token

        }
        return response
        
class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id = payload['id']).first() 
        serializer = UserSerializer(user)   

        return Response(serializer.data)
class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'Logged out successfully!'
        }
        return response
  



