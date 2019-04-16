from PDBMSlexer import tokens
import ply.yacc as yacc



def par_create(p):
    'expression : CREATE TABLE NAME LPAR NAME TYPE COMMA NAME TYPE RPAR'
    
def par_insert(p):
    'expression : INSERT INTO NAME LPAR NAME RPAR COMMA LPAR VALUES RPAR'

def par_delete(p):
    'expression : DELETE FROM NAME WHERE LPAR VALUES ETO VALUES RPAR'

def par_select(p):
    'expression : SELECT NAME WHERE LPAR VALUES ETO VALUES RPAR'

def par_add(p):
    'expression : ADD FROM NAME LPAR VALUES PLUS VALUES RPAR'

def par_subtract(p):
    'expression : SUBTRACT FROM NAME LPAR VALUES MINUS VALUES RPAR'

def par_multiply(p):
    'expression : MULTIPLY FROM NAME LPAR VALUES MULT VALUES RPAR'

def par_division(p):
    'expression : MULTIPLY FROM NAME LPAR VALUES DIV VALUES RPAR'

def par_show(p):
    'expression: SHOW NAME'





