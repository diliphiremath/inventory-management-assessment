from django.urls import path
from .views import SaveInventory, GetObject, SearchProperties

urlpatterns = [
    path('save/', SaveInventory.as_view(), name='save-inventory'),
    path('get_object/<str:object_id>/', GetObject.as_view(), name='get-object'),
    path('search/', SearchProperties.as_view(), name='serach-object'),
]