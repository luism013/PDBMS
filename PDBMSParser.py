import ply.yacc as yacc
from PDBMS import Entity
from PDBMSlexer import tokens

x = []
# ENTITIES --------------------------------------------------------------------------------
# works
def p_create(p): #create table tName (values)
    'Exp : CREATE TABLE WORDS LPAR def RPAR'
    # x.add_entity(p[3])
    y = Entity(p[3])
    string = p[5]
    for r in string.split(":"):
        y.add_attribute(r)
    x.append(y)
    p[0] = "Created table " + p[3]


def p_delete(p): #delete table tName
    'Exp : DELETE TABLE WORDS'
    # y = Entity(p[3])
    # if x.remove(y):
    #     p[0] = "Deleted table "+p[3]
    for a in x:
        if a.entityName is p[3]:
            x.remove(a)
            break
    # if x.__contains__()


# works
def p_selectAll(p): #show all entities
    'Exp : SHOW ALL ENTITIES'
    # print ('Schema :'+x.name)
    print(x)


def p_selectEntity(p): # show entity tName
    'Exp : SHOW ENTITY WORDS'
#     to be impemented with show all from entity


#update certain attribute but completely removes previous records from deleted attribute
def updateEntity(p):
    'Exp : UPDATE COLUMN LPAR def RPAR FROM WORDS'


# RECORDS --------------------------------------------------------------------------------------------

def p_insertIntoEntity(p): # insert (values) into tName
    'Exp : INSERT LPAR def RPAR INTO WORDS'


# def p_update(p):
#     'Exp : UPDATE TABLE WORDS COLUMN WORDS WHERE RECORD EQUALS WORDS '
#     x.get_entity(p[3]).get_attribute(p[5]).


def p_selectAllRecords(p): #show all from tName
    'Exp : SHOW ALL FROM WORDS'
    x.get_entity(p[4]).show_all()

# PARSER METHODS -------------------------------------------------------------------------------------

def p_def_r(p):
    'def : defRec'
    p[0] = p[1]


def p_def(p):
    'def : term'
    p[0] = p[1]


def p_def_rec(p):
    'defRec : def COLON def'
    p[0] = p[1]+ p[2] +p[3]


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