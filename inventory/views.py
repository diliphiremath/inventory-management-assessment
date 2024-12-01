from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import Item
from .serializers import BatchSerializer, ItemSerializer

class SaveInventory(APIView):
    def post(self, request):
        """
        Validate and save inventory JSON data
        input: JSON
        """
        try:
            data = request.data.copy()
            # renaming "objects" into "items" as its causing issue with serializers
            if "objects" in data:
                data["items"] = data.pop("objects")
            else:
                return Response("objects field is required", status=status.HTTP_400_BAD_REQUEST)
            serializer = BatchSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)           
        except Exception as e:
            return Response(
                {"errors":f"something went wrong: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class GetObject(RetrieveAPIView):
    """
    Retrieve a single object based on its object_id.
    input: object_id
    output: object json (item)
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "object_id"

class SearchProperties(ListAPIView):
    """
    List and filter properties based on data keys and/or values.
    input: key/value filter or null
    output: object json (item)
    """
    serializer_class = ItemSerializer

    def get_queryset(self):
        try:
            queryset = Item.objects.all()
            key = self.request.query_params.get('key')
            value = self.request.query_params.get('value')

            if key or value:
                queryset = queryset.filter(
                    Q(data__key=key) | Q(data__value=value)
                ).distinct()

            return queryset
        except Exception as e:
            return Response(
                {"errors":f"something went wrong: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )