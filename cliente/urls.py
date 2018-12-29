from django.urls import path
from .views import persons_list, person_create, person_update, person_delete


urlpatterns = [
    path('list/', persons_list, name='person_list'),
    path('new/', person_create, name='person_create'),
    path('update/<int:id>/', person_update, name='person_update'),
    path('delete/<int:id>/', person_delete, name='person_delete'),
]