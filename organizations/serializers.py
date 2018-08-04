from rest_framework import serializers

from organizations.models import Organization, Product, PriceList


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
  district = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

  class Meta:
    model = Organization
    fields = ('url', 'id', 'name', 'description', 'district')


class PriceListSerializer(serializers.ModelSerializer):
  class Meta:
    model = PriceList
    fields = ('price', 'organization')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
  organization = serializers.SlugRelatedField(read_only=True, slug_field='name')
  price_list = serializers.SerializerMethodField()

  class Meta:
    model = Product
    fields = ('url', 'id', 'name', 'organization', 'price_list')

  def get_price_list(self, obj):
    org_id = self.context['request'].query_params.get('organization')
    product = self.price_list.get(organization=org_id)
    print(product)
