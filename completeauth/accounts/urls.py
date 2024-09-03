# from django.urls import path
# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model
# from .views import LoginAPI

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(email=username)
#         except UserModel.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user
#         return None

# urlpatterns = [
#     path('login/', LoginAPI.as_view(), name='login'),
# ]
