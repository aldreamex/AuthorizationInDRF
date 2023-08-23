from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from demo.models import Adv
from demo.serializers import AdvSerializer
from rest_framework.permissions import IsAuthenticated
from demo.permissions import IsOwnerOrReadOnly
from rest_framework.throttling import AnonRateThrottle

class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    permission_classes = [IsOwnerOrReadOnly]  # разделение доступа в DRF (IsAuthenticated - проверка чтобы польз был аутенцифицирован
    throttle_classes = [AnonRateThrottle]                      # IsOwner - проверка на владельца коментария над которым производятся действия)
                                                               #(кто с чем может работать - в данном случае польщователи могут работать только со своими обьявлениями)

    #методы
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) #сохраняем обьект в БД (конкретный юзер в данном случае)
