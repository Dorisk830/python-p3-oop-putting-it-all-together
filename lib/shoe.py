#!/usr/bin/env python3

class Shoe:
    def __init__(self, size, brand):
        self._size = size
        self.brand = brand

    def get_size(self):
        return self._size
    
    def set_size(self, new_size):
        if isinstance(new_size, int):
            self._size = new_size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")   
            
    size = property(get_size, set_size)
# Shoe instance
my_shoe = Shoe(size=9, brand='Adidas')

# print the size and brand
print(my_shoe.get_size())  # 9
print(my_shoe.brand)       # 'Adidas'
