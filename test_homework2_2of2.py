import pytest
import uuid
from unittest.mock import Mock
from assertpy import assert_that
from homework2_2of2 import VatService, Product


class TestClass:

    @pytest.fixture(autouse=True)
    def prepare_vat_service(self):
        self.vat_provider = Mock()
        self.vat_service = VatService(self.vat_provider)

    @staticmethod
    def get_product_with_price(net_price, product_type):
        return Product(uuid, net_price, product_type)

    def test_get_gross_price_for_default_vat(self):
        # Given
        product = self.get_product_with_price(20.00, 'book')
        self.vat_provider.get_default_vat.return_value = 0.23
        # When
        result = self.vat_service.get_gross_price_for_default_vat(product)
        # Then
        assert_that(result).is_equal_to(24.60)

    def test_get_gross_price(self):
        # Given
        product = self.get_product_with_price(10.00, 'book')
        self.vat_provider.get_default_vat.return_value = 0.08
        # When
        result = self.vat_service.get_gross_price_for_default_vat(product)
        # Then
        assert_that(result).is_equal_to(10.80)



