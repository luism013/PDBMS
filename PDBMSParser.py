import ply.yacc as yacc
import PDBMS
from PDBMSlexer import tokens

x = PDBMS.Schema("Test")

# works
def p_create(p):
    'Exp : CREATE TABLE WORDS LPAR def RPAR'
    x.add_entity(p[3])
    string = p[5]
    for r in string.split(":"):
        x.get_entity(p[3]).add_attribute(r)
    p[0] = "Created table " + p[3]


def p_insert(p):
    'Exp : INSERT INTO WORDS VALUES LPAR def RPAR'
    string = p[6]
    x.get_entity(p[3]).mass_insert(string.split(":"))


# def p_update(p):
#     'Exp : UPDATE TABLE WORDS COLUMN WORDS WHERE RECORD EQUALS WORDS '
#     x.get_entity(p[3]).get_attribute(p[5]).


def p_delete(p):
    'Exp : DELETE TABLE WORDS'
    y = p[3]
    if x.remove_entity(p[3]):
        p[0] = "Deleted table "+p[3]


def p_selectAllEntity(p):
    'Exp : SHOW ALL FROM WORDS'
    x.get_entity(p[4]).show_all()

# works
def p_selectAllSchema(p):
    'Exp : SHOW ALL ENTITIES'
    print ('Schema :'+x.name)
    print (x.get_entities())


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