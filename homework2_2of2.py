class VatService:
    def __init__(self, vat_provider):
        self.vat_provider = vat_provider

    def get_gross_price_for_default_vat(self, product) -> float:
        return self.calculate_gross_price(product.get_net_price(), self.vat_provider.get_default_vat())

    def get_gross_price(self, net_price, product_type) -> float:
        vat_value = self.vat_provider.get_vat_for_type(product_type)
        return self.calculate_gross_price(net_price, vat_value)

    @staticmethod
    def calculate_gross_price(net_price, vat_value) -> float:
        if type(vat_value) is str:
            raise TypeError("Vat can't be string")
        if vat_value > 1:
            raise ValueError("Vat can't be bigger than one")
        if vat_value < 0:
            raise ValueError("Vat can't be negative")
        return round(net_price * (1 + vat_value), 4)


class Product:
    def __init__(self, product_id, net_price, product_type):
        self.id = product_id
        self.net_price = net_price
        self.product_type = product_type

    def get_net_price(self):
        return self.net_price

    def get_product_type(self):
        return self.product_type
