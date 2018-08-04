from django.db import models


class District(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Category(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Product(models.Model):
  name = models.CharField(max_length=100)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
    return self.name


class Organization(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  district = models.ManyToManyField(District)
  products = models.ManyToManyField(Product,
                                    through='PriceList',
                                    through_fields=('organization', 'product'))

  def __str__(self):
    return self.name


class PriceList(models.Model):
  product = models.ForeignKey(Product, related_name='price_list', on_delete=models.CASCADE)
  organization = models.ForeignKey(Organization, related_name='price_list', on_delete=models.CASCADE)
  price = models.FloatField()

  class Meta:
    unique_together = ('product', 'organization')

  def __str__(self):
    org = self.organization.name
    prod = self.product.name
    return "{}: {}".format(org, prod)
