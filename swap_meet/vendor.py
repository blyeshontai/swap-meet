
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

    def swap_first_item(self, other_vendor):
        if not self.inventory:
            return False

        if not other_vendor.inventory:
            return False

        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_item, their_item)

    #get by category
    def get_by_category(self, category):
        matching_items = []
        #loop through inventory for matches
        for item in self.inventory:
            if item.get_category() == category:
                matching_items.append(item)
        return matching_items

    #get by best category
    def get_best_by_category(self, category):
        #get matching items
        matching_items = self.get_by_category(category)
        #what to do if no matching items
        if not matching_items:
            return None

        best_item = matching_items[0]

        for item in matching_items[1:]:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)

        if my_item is None or their_item is None:
            return False
        else:
            return self.swap_items(other_vendor, my_item, their_item)
