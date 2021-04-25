import pytest
from homework2_1of2 import VatService, Product
import uuid
from assertpy import assert_that


class TestClass:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.vatService = VatService()

    @staticmethod
    def get_product_with_price(net_price):
        return Product(uuid, net_price)

    def test_get_gross_price_for_default_vat(self):
        # Given
        product = self.get_product_with_price(20.00)
        # When
        result = self.vatService.getGrossPriceForDefaultVat(product)
        # Then
        assert result == 24.60

    def test_get_gross_price(self):
        # Given
        product = self.get_product_with_price(10.00)
        # When
        result = self.vatService.getGrossPrice(product.getNetPrice(), 0.08)
        # Then
        assert result == 10.80
