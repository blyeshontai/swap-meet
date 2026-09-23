'''
### Wave 1

In Wave 1 we will create the `Vendor` class.

* There is a module (file) named `vendor.py` inside of the `swap_meet` package (folder)
* Inside this module, there is a class named `Vendor`
* Each `Vendor` will have an attribute named `inventory`, which is an empty list by default
* When we instantiate an instance of `Vendor`, we can optionally pass in a list with the keyword argument `inventory`


- Every instance of `Vendor` has an instance method named `add`, which takes in one item
- This method adds the item to the `inventory`
- This method returns the item that was added

- Similarly, every instance of `Vendor` has an instance method named `remove`, which takes in one item
- This method removes the matching item from the `inventory`
- This method returns the item that was removed
- If there is no matching item in the `inventory`, the method should return `None`
'''
class Vendor:

    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []

        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return None

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory:
            return False

        if their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True





"""
Instances of `Vendor` have an instance method named `swap_items`
- It takes 3 arguments:
- `swap_items` takes 3 arguments:
    1. an instance of another `Vendor` (`other_vendor`), representing the friend that the vendor is swapping with
    2. an instance of an `Item` (`my_item`), representing the item this `Vendor` instance plans to give
    3. an instance of an `Item` (`their_item`), representing the item the friend `Vendor` plans to give
  - The method removes `my_item` from this `Vendor`'s inventory, and adds it to the friend's inventory
  - The method removes `their_item` from the other `Vendor`'s inventory, and adds it to this `Vendor`'s inventory
  - The method returns `True`
  - If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item`, the method returns `False`

"""
