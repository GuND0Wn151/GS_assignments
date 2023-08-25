class Restaurant:


    def __init__(self,customer_orders={},book_table={},menu_items=[]):
        self.menu_items=menu_items
        self.book_table=book_table
        self.customer_orders=customer_orders

    def add_item_to_menu(self,item_name):
        self.menu_items.append(item_name)
    
    def book_tables(self,no,customer_name):
        self.book_table[customer_name]=no

    def customer_order(self,customer_name,item_list):
        self.customer_orders[customer_name]=item_list

    def display_menu(self):
        print("The items in the restaurant are:-")
        for i in self.menu_items:
            print(i)
        print()

    def display_bookings(self):
        for i,j in self.book_table.items():
            print(i,j)
        print()

    def display_cutomer_orders(self,customer_name):
        print("The items ordered by "+customer_name+" are ",self.customer_orders[customer_name])

r1=Restaurant({},{},["pizzza","burger","Rice","Salad"])

r1.add_item_to_menu("Soup")

r1.display_menu()

r1.book_tables("Ram",1)

r1.customer_order("Ram",["pizza","salad"])

r1.display_menu()

r1.book_tables("Setha",2)
r1.book_tables("David",3)

print("The table Bookings are:-")
r1.display_bookings()

r1.display_cutomer_orders("Ram")

