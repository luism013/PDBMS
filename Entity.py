# this is just a carbon copy of the Entity class found in a previous project. Need to modify or find a more creative
# way of doing this in order to avoid plagiarism.


class Schema:
    def __init__(self, sname):
        self.tables = {}
        self.name = sname

    def add_tables(self, table):
        for a in self.tables:
            if a not in self.tables:
                self.tables['table'] = table
            else:
                print("Table "+table+" already exists in schema "+self.name+".")
                break


class Tables:
    def __init__(self, tname):
        self.name = tname
        self.entities = []

    def add_entity(self, entity):
        for a in self.entities:
            if a not in self.entities:
                self.entities.extend(entity)
            else:
                print("Entity "+entity+" already exists in table "+self.name+".")
                break


class Entity:
    def __init__(self, name):
        self.entityName = name
        self.columns = []
        # Relationships nameoftherelationship = {cardinality=, modality =}
        self.relationships = {}


    def add_attribute(self, attribute):
        for a in attribute:
            if a not in self.attributes:
                self.attributes.extend(a)

    def get_attributes(self):
        return self.attributes


    # def get_records(self):
        # for


    def add_record(self, record):
        return record

    def get_name(self):
        return self.eName


# class Columns:


# Schema.tables_class = Tables
# Schema.entity_class = Entity
# Schema.column_class = Columns