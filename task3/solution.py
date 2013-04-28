people = []


class Person:
    def __init__(self, name, gender, birth_year, father=None,
                 mother=None):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.father = father
        self.mother = mother
        people.append(self)

    def __setattr__(self, name, value):
        if (name in ["mother", "father"] and value != None and
            value.birth_year > self.birth_year - 18):
                raise AttributeError("{} is too young!".format(name))
        super().__setattr__(name, value)

    def __str__(self):
        return "{}, {}, born in {}".format(self.name,
                                           self.gender,
                                           self.birth_year)

    def get_siblings(self, gender='both'):
        siblings = []
        for person in people:
            if ((person != self) and
                (gender == 'both' or
                gender == person.gender) and
                ((person.mother == self.mother) or
                (person.father == self.father))):
                    siblings.append(person)
        return siblings

    def get_brothers(self):
        return self.get_siblings('M')

    def get_sisters(self):
        return self.get_siblings('F')

    def children(self, gender='both'):
        children = []
        for person in people:
            if ((gender == 'both' or
                gender == person.gender) and
                ((self == person.mother) or
                (self == person.father))):
                    children.append(person)
        return children

    def successor(self):
        for child in self.children():
            yield child
            for grandchild in child.successor():
                yield grandchild

    def is_successor(self, other):
        return other in self.successor()

    def is_direct_successor(self, child):
        return child in self.children()