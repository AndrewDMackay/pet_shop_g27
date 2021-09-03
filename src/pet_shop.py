# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash  

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, increase):
    pet_shop["admin"]["pets_sold"] += increase

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pet_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pet_list.append(pet)
    return pet_list

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    x = 0
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].pop(x)
        x += 1

# Or..

# def remove_pet_by_name(pet_shop, name):
#   for pet in pet_shop["name"]:
#       if pet["name"] == name:
#           shop["pets"].pop(shop["pets"].index(pet))

def add_pet_to_stock(pet_shop, old_pet):
    pet_shop["pets"].append(old_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

# Extensions..

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

# def sell_pet_to_customer(pet_shop, pet, customer):
#     find_pet_by_name(pet_shop, pet["name"])
#     remove_customer_cash(customer, pet["price"])
#     add_or_remove_cash(pet_shop, pet["price"])
#     add_pet_to_customer(customer, pet_shop)
#     remove_pet_by_name(pet_shop, pet["name"])
#     increase_pets_sold(pet_shop, 1)

def sell_pet_to_customer(pet_shop, pet, customer):
    if customer_can_afford_pet(customer, pet)
        find_pet_by_name(pet_shop, pet["name"])
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        add_pet_to_customer(customer, pet_shop)
        remove_pet_by_name(pet_shop, pet["name"])
        increase_pets_sold(pet_shop, 1)

#  # These are 'integration' tests so we want multiple asserts.
#     # If one fails the entire test should fail 
#     # Advanced Extensions
#     # @unittest.skip("delete this line to run the test")
#     def test_sell_pet_to_customer__pet_found(self):
#         customer = self.customers[0]
#         pet = find_pet_by_name(self.cc_pet_shop,"Arthur")

#         sell_pet_to_customer(self.cc_pet_shop, pet, customer)

#         self.assertEqual(1, get_customer_pet_count(customer))
#         self.assertEqual(1, get_pets_sold(self.cc_pet_shop))
#         self.assertEqual(100, get_customer_cash(customer))
#         self.assertEqual(1900, get_total_cash(self.cc_pet_shop))

#     # @unittest.skip("delete this line to run the test")
#     def test_sell_pet_to_customer__pet_not_found(self):
#         customer = self.customers[0]
#         pet = find_pet_by_name(self.cc_pet_shop,"Dave")

#         sell_pet_to_customer(self.cc_pet_shop, pet, customer)

#         self.assertEqual(0, get_customer_pet_count(customer))
#         self.assertEqual(0, get_pets_sold(self.cc_pet_shop))
#         self.assertEqual(1000, get_customer_cash(customer))
#         self.assertEqual(1000, get_total_cash(self.cc_pet_shop))

#     # @unittest.skip("delete this line to run the test")
#     def test_sell_pet_to_customer__insufficient_funds(self):
#         customer = self.customers[1]
#         pet = find_pet_by_name(self.cc_pet_shop,"Arthur")

#         sell_pet_to_customer(self.cc_pet_shop, pet, customer)

#         self.assertEqual(0, get_customer_pet_count(customer))
#         self.assertEqual(0, get_pets_sold(self.cc_pet_shop))
#         self.assertEqual(50, get_customer_cash(customer))
#         self.assertEqual(1000, get_total_cash(self.cc_pet_shop))
