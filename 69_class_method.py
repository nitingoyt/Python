# class method

class budget:
    companyname = "Iguru"
    def show(self):
        print(f"The budget of this year for {self.companyname} is: {self.budget}")
    
    # def changename(cls, changename):
    #     cls.companyname = changename
    
    @classmethod
    def changename1(cls, changename1):
        cls.companyname = changename1

a= budget()
a.budget = 25000000
a.show() 
# a.changename("jio")
# a.show()
# print(budget.companyname)
a.changename1("Apple")
a.show()
print(budget.companyname)