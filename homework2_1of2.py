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
import uuid


class VatService:
    def __init__(self, vatValue=0.23):
        self.vatValue = vatValue

    def getGrossPriceForDefaultVat(self, product) -> float:
        return self.getGrossPrice(product.getNetPrice(), self.vatValue)

    def getGrossPrice(self, netPrice, vatValue):
        if vatValue > 1:
            raise ValueError

        return netPrice * (1 + vatValue)


class Product:
    def __init__(self, id, netPrice):
        self.id = id
        self.netPrice = netPrice

    def getNetPrice(self):
        return self.netPrice


