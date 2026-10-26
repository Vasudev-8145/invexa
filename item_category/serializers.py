

from rest_framework import serializers

from item_category.models import ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField()

    class Meta:

        model = ProductCategory

        fields = "__all__"

        read_only_fields = ["id","owner","created_at","updated_at"]