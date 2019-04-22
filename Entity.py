class Schema:
    def __init__(self, sname):
        self.name = sname
        self.entities = []

    def add_entity(self, entity):
        if not self.entities.__contains__(entity):
            self.entities.append(Entity(entity))

        else:
            print("Entity " + entity.get_name() + " already exists in table " + self.name + ".")
            # break

    def get_entity(self, eName):
        for e in self.entities:
            if e.get_name() == eName:
                return e


class Entity:
    def __init__(self, name):
        self.entityName = name
        self.columns = []
        self.relationships = {}

    def get_name(self):
        return self.entityName

    def add_attribute(self, eName):
        # for a in self.columns:
        #     if a not in self.columns:
        if not self.columns.__contains__(eName):
            self.columns.append(Columns(eName))

    def get_attributes(self):
        return self.columns

    def get_column(self, aName):
        for a in self.columns:
            if a.get_name() == aName:
                return a.get_records()

    def get_attribute(self, aName):
        for a in self.columns:
            if a.get_name() == aName:
                return a

    def add_relationship(self, name, cardinality):
        self.relationships[name] = {'Entity': name, 'Cardinality': cardinality}

    def get_relationship(self):
        return self.relationships.keys()


class Columns:
    def __init__(self, cname):
        self.columnName = cname
        self.records = []

    def get_name(self):
        return self.columnName

    def get_records(self):
        # for a in self.columns:
        return self.records

    def add_record(self, record):
        # for a in self.records:
        if self.records.__contains__(record):
            # if a not in self.records:
            print("Record " + record + " already exists in column " + self.columnName + ".")
        else:
            self.records.append(record)
            # break

    def remove_record(self, record):
        for a in self.records:
            if a not in self.records:
                self.records.append(record)
            else:
                print("Record " + record + " already exists in column " + self.columnName + ".")
                break

    # Schema.entity_class = Entity
    # Entity.column_class = Columns

x = Schema("StudentClass")
x.add_entity("Student")
x.get_entity("Student").add_attribute("Grades")
x.get_entity("Student").add_attribute("Classes")
x.get_entity("Student").add_attribute("Professor")
x.get_entity("Student").get_attribute("Grades").add_record("A")
print(x.get_entity("Student").get_attributes())