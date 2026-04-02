from .models import CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# це серіалізатор, який перетворює об’єкт користувача в JSON і навпаки
# він використовує модель CustomUser і прописані в моделі поля
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'image_small', 
            'image_medium',
            'image_large'
        ]
# кастомізація JWT логіну
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # створеня JWT токена
    @classmethod
    def get_token(cls, user):
        # створюємо стандартний токен
        token = super().get_token(user)

        # додаємо кастомні дані до токена
        token['id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        # token['phone'] = user.phone if user.phone else None
        token['image'] = user.image_small.url if user.image_small else None
        token['date_joined'] = user.date_joined.strftime('%Y-%m-%d %H:%M:%S')

        return token