from homework2_1of2 import VatService, Product
import uuid
from assertpy import assert_that



def test_get_gross_price_for_default_vat():
    # Given
    vatService = VatService()
    # When
    product = Product(uuid, 20.00)
    result = vatService.getGrossPriceForDefaultVat(product)
    # Then
    assert_that(result).is_equal_to(24.60)


# def test_get_gross_price():
#     assert False
