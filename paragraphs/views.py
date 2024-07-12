from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .models import CustomUser, Paragraph, WordIndex
from .serializers import CustomUserSerializer, ParagraphSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = []  # Ensure no authentication classes are applied
    permission_classes = [] 

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"message": "Invalid credentials"}, status=400)
    authentication_classes = []  # Ensure no authentication classes are applied
    permission_classes = [] 

class ParagraphListCreateView(generics.ListCreateAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class ParagraphSearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        word = request.query_params.get('word').lower()
        paragraph_ids = WordIndex.objects.filter(word=word).values_list('paragraph_id', flat=True)
        paragraphs = Paragraph.objects.filter(id__in=paragraph_ids)
        serializer = ParagraphSerializer(paragraphs, many=True)
        return Response(serializer.data)
