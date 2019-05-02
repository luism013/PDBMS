class Schema:
    def __init__(self, sname):
        self.name = sname
        self.entities = []

    def __repr__(self):
        return self.name

    def add_entity(self, entity):
        if self.get_entity(entity):
            print("Entity " + entity + " already exists in schema " + self.name + ".")
        else:
            self.entities.append(Entity(entity))


    def get_entity(self, eName):
        for e in self.entities:
            if getattr(e, 'entityName') == eName:
                return e

    def get_entities(self):
        return self.entities

    def remove_entity(self, eName):
        for a in self.entities:
            print("iterating")
            if getattr(a, 'entityName') == eName:
                self.entities.remove(a)
                print("Entity " + eName + " has been removed")
                return
        print("Entity " + eName + " does not exist in schema " + self.name + ".")



    def update_entity(self, old, new):
        for a in self.entities:
            if a == old:
                y = self.entities.index(a)
                self.entities.remove(a)
                self.entities.insert(y, new)

    def rename_entity(self, oldName, newName):
        for a in self.entities:
            if getattr(a, 'entityName') == oldName:
                setattr(a, 'entityName', newName)



class Entity:
    def __init__(self, name: str):
        self.entityName:str = name
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
        for a in self.attribute:
            if a.get_name() == aName:
                self.attribute.remove(a)

    def update_attribute(self, old, new):
        for a in self.attribute:
            if getattr(a, 'columnName') == old:
                y = self.attribute.index(a)
                self.attribute.remove(a)
                self.attribute.insert(y, Columns(new))
                break

    # insert record into all columns. Must make sure that the order of arguments is the correct one
    def mass_insert(self, args):
        n = 0
        for a in self.attribute:
            a.add_record(args[n])
            n += 1

    #delete record from all columns
    def mass_delete(self, index):
        print(len(self.attribute))
        for a in self.attribute:
            a.remove_record_by_index(index)



    def select_row(self, nRow):
        row = []
        for a in self.attribute:
            row.append(a.select_record_by_index(nRow))

        print(row)


    def show_all(self):
        row = [self.attribute]
        temp = []
        for i in range(len(self.attribute)-1):
            for a in self.attribute:
                temp.append(a.select_record_by_index(i))
            row.append(temp)
            temp = []


        dash = '-' * 40

        for i in range(len(row)):
            if i == 0:
                print(dash)
                print('{:<10}{:>4}{:>12}'.format(str(row[i][0]), str(row[i][1]), str(row[i][2])))
                print(dash)
            else:
                print('{:<10}{:>4}{:>20}'.format(str(row[i][0]), str(row[i][1]), str(row[i][2])))

        return row


class Columns:
    def __init__(self, cname: str):
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

    def select_record_by_index(self, index):
        return self.records[index]

    def remove_record_by_index(self, index):
        self.records.pop(index)


# tests that the entity class still works
x = Schema("StudentClass")
# # print(x)
x.add_entity("Student")
# print(x.entities)
# x.remove_entity("Student")
# print(x.entities)


# print(x.entities.__contains__("Student"))
# x.add_entity("Student")
# print (x.get_entity("Student"))
# x.remove_entity("Student")
# print(x.get_entity("Student"))
x.get_entity("Student").add_attribute("Grades")
x.get_entity("Student").add_attribute("Classes")
x.get_entity("Student").add_attribute("Professor")
x.get_entity("Student").update_attribute("Grades", "Notas")
print(x.get_entity("Student").get_attributes())
x.get_entity("Student").get_attribute("Notas").add_record("A")
x.get_entity("Student").get_attribute("Classes").add_record("PL")
x.get_entity("Student").get_attribute("Professor").add_record("Wilson Rivera")
# print(x.get_entity("Student").get_attribute("Grades").get_records())
# print(x.get_entity("Student").get_attributes())
# print(x.get_entity("Student"))
x.get_entity("Student").mass_insert("W", "Data", "Pedro Rivera")

# x.get_entity("Student").mass_delete(0)
x.get_entity("Student").get_attribute("Notas").update_record("A", "B")
x.get_entity("Student").show_all()
# print(x.get_entity("Student").get_attribute("Grades").get_records())
# print(x.get_entity("Student").get_attribute("Professor").get_records())
# print(x.get_entity("Student").get_attribute("Classes").get_records())
# x.get_entity("Student").show_all()
# print("Before remove")
# print(x.entities)
# x.remove_entity("Student")
# print("After remove")
# print(x.entities)
# x.get_entity("Student").mass_delete(0)
# print(x.get_entity("Student").get_attribute("Grades").get_records())
# print(x.get_entity("Student").get_attribute("Professor").get_records())
# print(x.get_entity("Student").get_attribute("Classes").get_records())

