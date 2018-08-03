from django.db import models


class District(models.Model):
  name = models.CharField(max_length=100)


class Category(models.Model):
  name = models.CharField(max_length=100)


class Organization(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  district_id = models.ManyToManyField(District)

  def __str__(self):
    return self.name


class Product(models.Model):
  name = models.CharField(max_length=100)
  category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


class PriceList(models.Model):
  product_id = models.ManyToManyField(Product)
  organization_id = models.ManyToManyField(Organization)
  price = models.FloatField()
