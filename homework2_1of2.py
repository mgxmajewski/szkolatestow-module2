# class VatService {
#     double vatValue;
#
#     public VatService() {
#         this.vatValue = 0.23;
#     }
#
#     public double getGrossPriceForDefaultVat(Product product){
#
#         return getGrossPrice(product.getNetPrice(), vatValue);
#     }
#
#     public double getGrossPrice(double netPrice, double vatValue){
#         if(vatValue > 1){
#             throw Exception
#         }
#
#         return netPrice * (1 + vatValue)));
#     }
# }
#
# class Product {
#     string id;
#     double netPrice;
# }

class VatService:
    def __init__(self, vat_value=0.23):
        self.vat_value = vat_value

    def get_gross_price_for_default_vat(self, product):
        return self.get_gross_price(product.net_price, self.vat_value)

    def get_gross_price(self, net_price, vat_value):
        if vat_value > 1:
            raise ValueError("Vat can't exceed 1. " + vat_value + " is invalid")
        return net_price * (1 + vat_value)


class Product:
    def __init__(self, id, net_price):
        self.id = id
        self.net_price = net_price
