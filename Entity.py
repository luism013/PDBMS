# this is just a carbon copy of the Entity class found in a previous project. Need to modify or find a more creative
# way of doing this in order to avoid plagiarism.


class Schema:
    def __init__(self, sname):
        self.name = sname
        self.entities = []

    def add_entity(self, entity):
            if not self.entities.__contains__(entity):
                self.entities.append(entity)
            else:
                print("Entity "+entity+" already exists in table "+self.name+".")
                # break


class Entity:
    def __init__(self, name):
        self.entityName = name
        self.columns = []
        self.relationships = {}

    def get_name(self):
        return self.entityName

    def add_attribute(self, eName):
        for a in eName:
            if a not in self.columns:
                self.columns.append(eName)

    def get_attributes(self):
        return self.columns

    def add_relationship(self, name, cardinality):
        self.relationships[name] = {'Entity' : name, 'Cardinality' : cardinality}

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
