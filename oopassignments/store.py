class store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        if product in self.products: self.products.remove(product)
        return self

    def inventory(self):
        inventory_list = 'Products in store:'
        for x in self.products:
            inventory_list += ' ' + x + ','
        print inventory_list
        print 'Address:', self.location
        print 'Owner:', self.owner
        return self

store1 = store(['guitar','drums','bass','pedals','picks','cables','drum_sticks','strings'], '1119 E Wellington', 'Steve Compare')

store1.add_product('synthesizer').remove_product('picks').remove_product('strings').inventory()
        