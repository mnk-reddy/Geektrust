from sys import argv


class Bill_Generator:
    PRODUCTS=['TSHIRT','JACKET','CAP','NOTEBOOK','PENS','MARKERS']
    ORIGINAL_PRICE=[1000,2000,500,200,300,500]
    PRODUCT_DISCOUNT=[0.10,0.05,0.20,0.20,0.10,0.05]
    CLOTHING=PRODUCTS[:3]
    STATIONARY=PRODUCTS[3:]
    BILL=0
    DISCOUNT=0
    MAX_CLOTHING=2
    MAX_STATIONARY=3

    def add_to_bill(self,product,quantity):
        x=self.PRODUCTS.index(product)
        self.BILL+=self.ORIGINAL_PRICE[x]*quantity
        self.DISCOUNT+=(self.ORIGINAL_PRICE[x]*quantity*self.PRODUCT_DISCOUNT[x])

    def Quantity_Exceeded(self,product,quantity):
        return (product in self.CLOTHING and quantity>self.MAX_CLOTHING) or (product in self.STATIONARY and quantity>self.MAX_STATIONARY)
    
    def check_quantity(self,product,quantity):
        quantity=int(quantity)
        # if (product in self.CLOTHING and quantity>self.MAX_CLOTHING) or (product in self.STATIONARY and quantity>self.MAX_STATIONARY):
        if (self.Quantity_Exceeded(product,quantity)):
            print('ERROR_QUANTITY_EXCEEDED')
        else:
            print('ITEM_ADDED')
            self.add_to_bill(product,quantity)

    def calculate_total(self):
    
        Min_bill_amt=1000
        Good_bill_amt=3000
        Extra_Discount=0.95
        # check if eligible for discount and extra 5% discount
        if self.BILL>=Good_bill_amt:
            TOTAL_BILL=(self.BILL-self.DISCOUNT)*Extra_Discount
            TOTAL_DISCOUNT=self.BILL-TOTAL_BILL
        elif self.BILL>=Min_bill_amt:
            TOTAL_BILL=self.BILL-self.DISCOUNT
            TOTAL_DISCOUNT=self.DISCOUNT
        else:
            TOTAL_BILL=self.BILL
            TOTAL_DISCOUNT=0
        return TOTAL_BILL,TOTAL_DISCOUNT

    def print_bill(self):

        # calculate Total bill and total discount
        TOTAL_BILL,TOTAL_DISCOUNT=self.calculate_total()

        #print Final BIll values
        print('TOTAL_DISCOUNT %.2f'%TOTAL_DISCOUNT)
        print('TOTAL_AMOUNT_TO_PAY %.2f'%(TOTAL_BILL*1.1))

def main():
    #read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()

    billing=Bill_Generator()
    for line in lines:
        # find command 
        command=line.split()
        if command[0]=='ADD_ITEM':
            billing.check_quantity(command[1],command[2])
        # Print Bill
        else:
            billing.print_bill()
    
if __name__ == "__main__":
    main()