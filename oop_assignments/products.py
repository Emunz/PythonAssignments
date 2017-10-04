class products(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'For Sale'

    def sell(self):
        self.status = 'Sold'
        return self
    
    def add_tax(self, tax):
        self.price *= tax
        return self

    def return_item(self, reason):
        if(reason == 'defective'):
            self.status = 'Defective'
            self.price = 0
        if(reason == 'returned in the box, like new'):
            self.status = 'For Sale'
        if(reason == 'box has been opened'):
            discount = self.price * 0.2
            self.status = 'Used'
            self.price -= discount
        return self

    def display_info(self):
        print 'Price:', self.price
        print 'Item:', self.item_name
        print 'Weight:', self.weight
        print 'Brand:', self.brand
        print 'Cost:', self.cost
        print 'Status:', self.status

product1 = products(40, 'Lamp', '20lbs', 'Kinsley Glassworks', 30)

product1.add_tax(1.08).sell().return_item('box has been opened').display_info()

product1.return_item('defective').display_info()
