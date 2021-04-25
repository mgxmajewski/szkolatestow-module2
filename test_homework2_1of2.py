import pytest
from homework2_1of2 import VatService, Product
import uuid
from assertpy import assert_that


class TestClass:

    @pytest.fixture(autouse=True)
    def prepare_vat_service(self):
        self.vat_service = VatService()

    @staticmethod
    def get_product_with_price(net_price):
        return Product(uuid, net_price)

    def test_get_gross_price_for_default_vat(self):
        # Given
        product = self.get_product_with_price(20.00)
        # When
        result = self.vat_service.get_gross_price_for_default_vat(product)
        # Then
        assert_that(result).is_equal_to(24.60)

    def test_get_gross_price(self):
        # Given
        product = self.get_product_with_price(10.00)
        vat_rate = 0.08
        # When
        result = self.vat_service.get_gross_price(product.get_net_price(), vat_rate)
        # Then
        assert_that(result).is_equal_to(10.80)

    def test_exception_when_vat_too_high(self):
        # Given
        product = self.get_product_with_price(10.00)
        vat_rate = 1.1
        # then
        assert_that(self.vat_service.get_gross_price).raises(Exception).when_called_with(product, vat_rate)
