class Schema:
    def __init__(self, sname):
        self.name = sname
        self.entities = []

    def __repr__(self):
        return self.name

    def add_entity(self, entity):
        if not self.entities.__contains__(entity):
            self.entities.append(Entity(entity))
        else:
            print("Entity " + entity.get_name() + " already exists in schema " + self.name + ".")

    def get_entity(self, eName):
        for e in self.entities:
            if e.get_name() == eName:
                return e

    def remove_entity(self, eName):
        if self.entities.__contains__(eName):
            self.entities.remove(eName)
        else:
            print("Entity " + eName.get_name() + " does not exist in schema " + self.name + ".")

    def update_entity(self, old, new):
        for a in self.entities:
            if a == old:
                y = self.entities.index(a)
                self.entities.remove(a)
                self.entities.insert(y, new)


class Entity:
    def __init__(self, name):
        self.entityName = name
        self.attribute = []
        self.relationships = {}

    def __repr__(self):
        return self.entityName

    def get_name(self):
        return self.entityName

    def add_attribute(self, aName):
        if not self.attribute.__contains__(aName):
            self.attribute.append(Columns(aName))

    def get_attributes(self):
        return self.attribute

    def get_column(self, aName):
        for a in self.attribute:
            if a.get_name() == aName:
                return a.get_records()

    def get_attribute(self, aName):
        for a in self.attribute:
            if a.get_name() == aName:
                return a

    def remove_attribute(self, aName):
        if self.attribute.__contains__(aName):
            self.attribute.remove(aName)

    def update_attribute(self, old, new):
        for a in self.attribute:
            if a == old:
                y = self.attribute.index(a)
                self.attribute.remove(a)
                self.attribute.insert(y, new)

    def add_relationship(self, name, cardinality):
        self.relationships[name] = {'Entity': name, 'Cardinality': cardinality}

    def get_relationship(self):
        return self.relationships.keys()

    # insert record into all columns
    def mass_insert(self, index, *args):
        for a in args:
            self.get_attribute(index)

    #delete record from all columns
    def mass_delete(self, index):
        for a in self.attribute:
            self.get_attribute(a).re


class Columns:
    def __init__(self, cname):
        self.columnName = cname
        self.records = []

    def __repr__(self):
        return self.columnName

    def get_name(self):
        return self.columnName

    def get_records(self):
        # for a in self.columns:
        return self.records

    def add_record(self, record):
        if self.records.__contains__(record):
            print("Record " + record + " already exists in column " + self.columnName + ".")
        else:
            self.records.append(record)

    def remove_record(self, record):
        if self.records.__contains__(record):
            self.records.remove(record)
        else:
            print("Record " + record + " does not exists in column " + self.columnName + ".")

    def update_record(self, old, new):
        for a in self.records:
            if a == old:
                y = self.records.index(a)
                self.records.remove(a)
                self.records.insert(y, new)

    # Schema.entity_class = Entity
    # Entity.column_class = Columns


x = Schema("StudentClass")
print(x)
x.add_entity("Student")
x.get_entity("Student").add_attribute("Grades")
x.get_entity("Student").add_attribute("Classes")
x.get_entity("Student").add_attribute("Professor")
x.get_entity("Student").get_attribute("Grades").add_record("A")
print(x.get_entity("Student").get_attribute("Grades").get_records())
print(x.get_entity("Student").get_attributes())
print(x.get_entity("Student").get_attribute("Grades"))
print(x.get_entity("Student"))