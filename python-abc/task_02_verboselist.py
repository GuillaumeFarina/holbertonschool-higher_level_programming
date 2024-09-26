#!/usr/bin/env python3

class VerboseList(list):

    def append(self, item):
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, item):
        print("Extended the list with [{}] items.".format(len(item)))
        super().extend(item)

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        if self:
            pop_item = self[index]
            print("Popped [{}] from the list.".format(pop_item))
            return super().pop(index)
        else:
            raise ValueError("Cannot pop from an empty list.")
