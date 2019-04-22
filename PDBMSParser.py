import ply.yacc as yacc
from PDBMSlexer import tokens
from Entity import Schema, Entity, Columns


def p_create_table(p):
    'expression : CREATE TABLE NAME LPAR NAME TYPE COMMA NAME TYPE RPAR'


def p_insert_into_table(p):
    'expression : INSERT INTO NAME LPAR NAME RPAR COMMA LPAR VALUES RPAR'


def p_delete_from_table(p):
    'expression : DELETE FROM NAME WHERE LPAR VALUES ETO VALUES RPAR'


def p_select_from_table(p):
    'expression : SELECT FROM NAME WHERE LPAR VALUES ETO VALUES RPAR'

# def p_add_to_table(p):
#     'expression : ADD FROM NAME LPAR VALUES PLUS VALUES RPAR'

def p_update_table(p):
    'expression : ADD FROM NAME LPAR VALUES PLUS VALUES RPAR'


# def p_subtract(p):
#     'expression : SUBTRACT FROM NAME LPAR VALUES MINUS VALUES RPAR'
#
#
# def p_multiply(p):
#     'expression : MULTIPLY FROM NAME LPAR VALUES MULT VALUES RPAR'
#
#
# def p_division(p):
#     'expression : MULTIPLY FROM NAME LPAR VALUES DIV VALUES RPAR'


def p_show(p):
    'expression : SHOW NAME'


def p_error(p):
    print("Syntax error at '%s'" % p.value)


parser = yacc.yacc()

while True:
    try:
        s = input('DBMS-> ')
        s.lower()
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)


