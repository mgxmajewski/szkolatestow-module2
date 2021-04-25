from homework2_1of2 import VatService, Product
import uuid
from assertpy import assert_that


def test_get_gross_price_for_default_vat():
    # Given
    vatService = VatService()
    vatRate = 20.00
    product = Product(uuid, vatRate)
    # When
    result = vatService.getGrossPriceForDefaultVat(product)
    # Then
    assert_that(result).is_equal_to(24.60)


def test_get_gross_price():
    # Given
    vatService = VatService()
    vatRate = 10.00
    product = Product(uuid, vatRate)
    # When
    result = vatService.getGrossPrice(product.getNetPrice(), 0.08)
    # Then
    assert_that(result).is_equal_to(10.8)
