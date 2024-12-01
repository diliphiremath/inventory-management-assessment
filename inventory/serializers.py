from rest_framework import serializers
from .models import Batch, Item, Properties

class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ['key', 'value']

class ItemSerializer(serializers.ModelSerializer):
    data = PropertiesSerializer(many=True)
    class Meta:
        model = Item
        fields = ['object_id', 'data']
    
    def create(self, validated_data):
        prop_list = validated_data.pop("data")
        if not prop_list:
            raise ValueError('Data is empty for object_id',validated_data.get("object_id"))
        try:
            item = Item.objects.get(object_id=validated_data.get("object_id"))
        except Item.DoesNotExist:
            item = None
        if not item:
            item = Item.objects.create(**validated_data)
        for prop in prop_list:
            Properties.objects.create(item=item, **prop)
        
        return item
            
       
class BatchSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Batch
        fields = ['batch_id', 'items']
    
    def create(self, validated_data):
        # import ipdb; ipdb.set_trace()
        items_data = validated_data.pop("items")
        try:
            batch = Batch.objects.get(batch_id=validated_data.get("batch_id"))
        except Batch.DoesNotExist:
            batch = None    
        if not batch:
            batch = Batch.objects.create(**validated_data)
        for item in items_data:
            item["batch"] = batch
            ItemSerializer().create(item)
        return batch




