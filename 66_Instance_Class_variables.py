
class goods:
    countryname = "India"
    no0fgoods = 0
    def __init__(self, goods_name):
        self.goods_name = goods_name
        self.tax_percent = "5%"
        goods.no0fgoods +=1
        
    def info(self):
        print(f"{self.goods_name} purchased from {self.countryname} had a tax of {self.tax_percent}")
    
obj1 = goods("Apple")
obj1.info()


obj2 = goods("Avacado")
obj2.countryname = "Africa"
goods.countryname = "Africa"
obj2.tax_percent = "7%"
obj2.info()

print(obj2.no0fgoods)