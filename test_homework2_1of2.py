import pytest

from homework2_1of2 import VatService, Product
import uuid
from assertpy import assert_that

class TestClass:

    vatService = None

    def get_product_with_price(self):
        return Product(uuid, self.vatRate)

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.vatService = VatService()

    def test_get_gross_price_for_default_vat(self):
        # Given
        # self.set_up()
        self.vatRate = 20.00
        product = self.get_product_with_price()
        # When
        result = self.vatService.getGrossPriceForDefaultVat(product)
        # Then
        assert result == 24.60

    def test_get_gross_price(self):
        # Given
        # self.set_up()
        self.vatRate = 10.00
        product = self.get_product_with_price()
        # When
        result = self.vatService.getGrossPrice(product.getNetPrice(), 0.08)
        # Then
        assert result == 10.80
