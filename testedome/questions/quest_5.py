"""
   A
 / |
B  C

'B, C'
"""


class CategoryTree:

    def __init__(self):
        self.root = {}
        self.all_categories = []

    def add_category(self, category, parent):
        if category in self.all_categories:
            raise KeyError(f"{category} exists")

        if parent is None:
            self.root[category] = set()

        if parent:
            if parent not in self.root:
                raise KeyError(f"{parent} invalid")
            self.root[category] = set()
            self.root[parent].add(category)

        self.all_categories.append(category)


    def get_children(self, parent):
        if parent and parent not in self.root:
            raise KeyError(f"{parent} invalid")
        return list(self.root[parent])


if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(','.join(c.get_children('A') or []))
    print(','.join(c.get_children('E') or []))
