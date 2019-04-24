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

    # insert record into all columns. Must make sure that the order of arguments is the correct one
    def mass_insert(self, *args):
        n = 0
        for a in self.attribute:
            a.add_record(args[n])
            n += 1

    #delete record from all columns
    def mass_delete(self, index):
        for a in self.attribute:
            a.remove_record_by_index(index)

    # def show_all(self):
    #     list = [self.attribute]
    #     list_row = self.mass_select()
    #     list.append(list_row)
    #     print(list)

    # def mass_select(self):
    #     row = []
    #     for a in self.attribute:
    #         y = a.get_length()
    #         break
    #
    #     for i in range(y):
    #         for a in self.attribute:
    #             row.append(a.select_record_by_index(i))
    #     return row


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


# tests that the entity class still works
# x = Schema("StudentClass")
# print(x)
# x.add_entity("Student")
# x.get_entity("Student").add_attribute("Grades")
# x.get_entity("Student").add_attribute("Classes")
# x.get_entity("Student").add_attribute("Professor")
# x.get_entity("Student").get_attribute("Grades").add_record("A")
# x.get_entity("Student").get_attribute("Classes").add_record("PL")
# x.get_entity("Student").get_attribute("Professor").add_record("Wilson Rivera")
# print(x.get_entity("Student").get_attribute("Grades").get_records())
# print(x.get_entity("Student").get_attributes())
# print(x.get_entity("Student"))
# x.get_entity("Student").mass_insert("W", "Data", "Pedro Rivera")
# print(x.get_entity("Student").get_attribute("Grades").get_records())
# print(x.get_entity("Student").get_attribute("Professor").get_records())
# print(x.get_entity("Student").get_attribute("Classes").get_records())
# x.get_entity("Student").show_all()
# x.get_entity("Student").mass_delete(0)
# print(x.get_entity("Student").get_attribute("Grades").get_records())
# print(x.get_entity("Student").get_attribute("Professor").get_records())
# print(x.get_entity("Student").get_attribute("Classes").get_records())

