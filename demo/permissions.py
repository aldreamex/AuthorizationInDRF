from rest_framework.permissions import BasePermission

#проверка - является ли владельцем обьявления наш пользователь или нет
class IsOwnerOrReadOnly(BasePermission):
    # def has_permission(self, request, view):
        # имеет ли право пользователь пользоваться ресурсом удаления обьявления

    def has_object_permission(self, request, view, obj): # пользователь из запроса совпадает с пользователем создавшим данное обьявление или нет
        if request.method == 'GET':
            return True
        return request.user == obj.user # сравнение юзера из запроса и из БД(тот кто создал обьявление)
