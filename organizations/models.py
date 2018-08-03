from django.db import models


class District(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Category(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Organization(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  district = models.ManyToManyField(District)

  def __str__(self):
    return self.name


class Product(models.Model):
  name = models.CharField(max_length=100)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
    return self.name


class PriceList(models.Model):
  product = models.ManyToManyField(Product)
  organization = models.ManyToManyField(Organization)
  price = models.FloatField()

  def __str__(self):
    org = self.organization.first().name
    prod = self.product.first().name
    return "{}: {}".format(org, prod)
