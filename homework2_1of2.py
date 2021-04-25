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
        self.vatValue = vat_value

    def get_gross_price_for_default_vat(self, product) -> float:
        return self.get_gross_price(product.get_net_price(), self.vatValue)

    @staticmethod
    def get_gross_price(net_price, vat_value):
        if vat_value > 1:
            raise ValueError

        return net_price * (1 + vat_value)


class Product:
    def __init__(self, product_id, net_price):
        self.id = product_id
        self.netPrice = net_price

    def get_net_price(self):
        return self.netPrice
