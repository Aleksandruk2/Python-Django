import random
from rest_framework import viewsets, parsers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserSerializer


# Create your views here.
# заготовки для генерації випадкових користувачів
FIRST_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
LAST_NAMES = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Lee"]
DOMAINS = ["example.com", "test.com", "mail.com"]

# функція створеня випадкових користувачів
def generate_random_users(n=5):
    created_users = []

    # створеня в циклі зазначеної кількісті користувачів
    for _ in range(n):
        while True:
            # генерація унікального ім'я для крористувача
            username = f"user{random.randint(1000, 9999)}"
            if not CustomUser.objects.filter(username=username).exists():
                break
        
        # вибір випадкового ім'я та прізвища із заготовок вказаних вище по коду
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        # електрона пошта створюється на основі уже вибраних раніше ім'я та прізвища, такош вибирається випадковий DOMAIN
        email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(DOMAINS)}"

        # створеня користувача на основі згенерованих вище даних та додаваня його в бд
        user = CustomUser.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        created_users.append(user)

    return created_users

# вюшка для читаня, наприклад: GET /users/
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # отримуємо усіх користувачів
    queryset = CustomUser.objects.all()
    # сереалізуємо дані
    serializer_class = UserSerializer
    # дозволяємо приймати файли
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    # створюємо новий endpoint: POST /users/generate/
    @action(detail=False, methods=["post"])
    def generate(self, request):
        # генеруємо користувачів
        users = generate_random_users(5)
        # перетворяємо список у JSON та повертаємо дані
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

# кастомний login через JWT
class LoginView(TokenObtainPairView):
    # використовуємо наш серіалайзер та получаємо токен
    serializer_class = CustomTokenObtainPairSerializer

    # обробляє login запит
    def post(self, request, *args, **kwargs):
        # print('-------working login--------')
        # беремо дані користувача із запиту
        serializer = self.get_serializer(data=request.data)
        # print("-----data server------", serializer)
        try:
            # валідуємо дані
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"detail": "Invalid credentials"}, status=401)

        # якщо відповідь успішна повертає refresh та access токени 
        return Response(serializer.validated_data, status=status.HTTP_200_OK)