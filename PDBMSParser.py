import ply.yacc as yacc
from PDBMSlexer import tokens


def p_create(p):
    'expression : CREATE TABLE NAME LPAR NAME TYPE COMMA NAME TYPE RPAR'


def p_insert(p):
    'expression : INSERT INTO NAME LPAR NAME RPAR COMMA LPAR VALUES RPAR'


def p_delete(p):
    'expression : DELETE FROM NAME WHERE LPAR VALUES ETO VALUES RPAR'


def p_select(p):
    'expression : SELECT NAME WHERE LPAR VALUES ETO VALUES RPAR'


def p_add(p):
    'expression : ADD FROM NAME LPAR VALUES PLUS VALUES RPAR'


def p_subtract(p):
    'expression : SUBTRACT FROM NAME LPAR VALUES MINUS VALUES RPAR'


def p_multiply(p):
    'expression : MULTIPLY FROM NAME LPAR VALUES MULT VALUES RPAR'


def p_division(p):
    'expression : MULTIPLY FROM NAME LPAR VALUES DIV VALUES RPAR'


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


