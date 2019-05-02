import ply.yacc as yacc
from PDBMS import Entity
from PDBMS import Schema
from PDBMSlexer import tokens

x = Schema("Test")
# ENTITIES --------------------------------------------------------------------------------
# works


def p_create(p): #create table tName (values)
    'Exp : CREATE TABLE WORDS LPAR def RPAR'
    x.add_entity(p[3])
    string = p[5]
    for r in string.split(":"):
        x.get_entity(p[3]).add_attribute(r)
    p[0] = "Created table " + p[3]


# works
def p_delete(p):
    'Exp : DELETE TABLE WORDS'
    x.remove_entity(p[3])
    p[0] = ""


# works
def p_selectAll(p): # show all tables
    'Exp : SHOW ALL TABLES'
    print('Schema :'+x.name)
    print(x.get_entities())
    p[0] = ""


def p_selectEntity(p): # show table tName
    'Exp : SHOW TABLE WORDS'
#     to be impemented with show all from entity


# update certain attribute but completely removes previous records from deleted attribute
def p_updateEntity(p): # update column (att1:att2) from tName
    'Exp : UPDATE COLUMN LPAR def RPAR FROM WORDS'
    x.update_entity(p[7], p[4])


# just changes name, leaves all attributes and records intact
def p_renameEntity(p): #rename table tName to tName2
    'Exp : RENAME TABLE WORDS TO WORDS'
    x.rename_entity(p[3], p[5])
    p[0] = "Table " + p[3] + " has been changed to " + p[5]


def p_addColumnToEntity(p): #update tName where record = value with (values)
    'Exp : INSERT COLUMN term INTO WORDS'
    x.get_entity(p[5]).add_attribute(p[3])
    p[0] = "Inserted attribute "+p[3]+" into "+p[5]


# RECORDS --------------------------------------------------------------------------------------------


def p_insertIntoEntity(p): # insert (values) into tName
    'Exp : INSERT LPAR def RPAR INTO WORDS'
    y = x.get_entity(p[6])
    y.mass_insert(p[3].split(':'))
    p[0] = "Inserted records into table "+p[6]


def p_selectAllRecords(p): #show all from tName
    'Exp : SHOW ALL FROM WORDS'
    index = int(p[3])
    y = x.get_entity(p[5])
    y.select_row(index)


def p_selectRecord(p): #show rName from tName
    'Exp : SHOW WORDS FROM WORDS'


def p_deleteRecord(p): #delete from tname where record = value
    'Exp : DELETE FROM WORDS AT NUMBER'
    x.get_entity(p[3]).mass_delete(p[5])
    p[0] = 'Deleted records from table '+p[3]


def p_updateRecord(p): #update tName where record = value with (values)
    'Exp : UPDATE WORDS AT NUMBER WITH LPAR def RPAR'
    x.get_entity(p[3]).mass_delete(p[2])
    string = p[7]
    x.get_entity().mass_insert(string.split(":"))
    p[0] = "Updated records in table "+p[2]


# PARSER METHODS -------------------------------------------------------------------------------------

def p_def_r(p):
    'def : defRec'
    p[0] = p[1]


def p_def(p):
    'def : term'
    p[0] = p[1]


def p_def_rec(p):
    'defRec : def COLON def'
    p[0] = p[1] + p[2] + p[3]


def p_term_words(p):
    'term : WORDS'
    p[0] = p[1]


def p_term_number(p):
    'term : NUMBER'
    p[0] = p[1]


def p_error(p):
    print("Syntax error at '%s'" % repr(p)) #p.value)


yacc = yacc.yacc()

# result = yacc.parse("create table yes (name:lasttname:age)")
# print(result)

while True:
    try:
        s = input('DBMS-> ')
        s.lower()
    except EOFError:
        break
    if not s:
        continue
    result = yacc.parse(s)
    print(result)