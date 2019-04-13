# this is just a carbon copy of the Entity class found in a previous project. Need to modify or find a more creative
# way of doing this in order to avoid plagiarism.

class Entity:
    def __init__(self, name):
        self.eName = name
        self.attributes = []
        # Relationships nameoftherelationship = {cardinality=, modality =}
        self.relationships = {}

    def add_relationship(self, eName, rName, cardinality, modality):
        self.relationships[rName] = {'entity': eName, 'cardinality': cardinality, 'modality': modality}

    def get_relationships(self):
        return self.relationships.keys()

    def __iter__(self):
        return iter(self.relationships.items())

        # We coulld add primary key and other type of attributes as keys in a dictionary instead of a list.

    def add_attribute(self, aName):
        for attribute in aName:
            if attribute not in self.attributes:
                self.attributes.extend(aName)

    def get_attributes(self):
        return self.attributes

    def get_name(self):
        return self.eName