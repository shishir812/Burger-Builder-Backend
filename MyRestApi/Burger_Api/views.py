from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, Order
from .serializers import UserProfileSerilizer, OrderSerializer

# Create your views here.

class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerilizer
    queryset = UserProfile.objects.all()

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [
        IsAuthenticated,
    ]


    def get_queryset(self):
        queryset = Order.objects.all()
        id = self.request.query_params.get('id', None)

        if id is not None:
            queryset = queryset.filter(user__id=id)
        return queryset