from rest_framework.test import APITestCase


class OrganizationTestCase(APITestCase):
  fixtures = ['fixtures.json']

  def test_organizations_by_district(self):
    response = self.client.get('/organizations/8', format='json')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 2)


class ProductTestCase(APITestCase):
  fixtures = ['fixtures.json']

  def test_products_filtering_by_organization(self):
    response = self.client.get('/products', {'organization': 9}, format='json')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.data), 2)

  def test_products_filtering_by_price(self):
    response = self.client.get('/products', {'min_price': 100, 'max_price': 150}, format='json')

    self.assertEqual(len(response.data), 2)

  def test_products_by_category(self):
    response = self.client.get('/products', {'category': 2, 'organization': 1}, format='json')

    self.assertEqual(len(response.data), 0)
