import uuid

class Item:

    def __init__(self, id=None, condition=0):
        if id is None:
            self.id =uuid.uuid4().int
        else:
            self.id=id

        self.condition = condition

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        if self.condition <= 1:
          return "really bad"
        elif self.condition <= 2:
            return "not great"
        elif self.condition <= 3:
            return "ok"
        elif self.condition <= 4:
            return "nice"
        else:
            return "perfect"
