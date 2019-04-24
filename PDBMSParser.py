import ply.lex as lex
import ply.yacc as yacc
import Entity

reserved = {
    'create': 'CREATE',
    'table': 'TABLE'
}

tokens = ['WORDS', 'NUMBER', 'LPAR', 'RPAR', 'COLON'] + list(reserved.values())


t_LPAR = r'\('


t_RPAR = r'\)'

t_COLON = r'\:'


t_ignore = '\t \n'

def t_WORDS(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


def t_NUMBER(t):
    r'\d+'
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


# lexer.input("hi name is cuck")
#
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)

# def splitcolums(string):
#     result =
#     return result


def p_statement(p):
    'Exp : CREATE TABLE WORDS LPAR def RPAR'
    x = Entity.Schema("temp")
    x.add_entity(p[3])
    string = p[5]
    for r in string.split(":"):
        x.get_entity(p[3]).add_attribute(r)

    p[0]= "Created table " + p[3] + ",bitch"


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

# def p_error(p):
#     print("Syntax error at '%s'" % repr(p)) #p.value)


yacc = yacc.yacc()

result = yacc.parse("create table yike ( hello:123:hello )")
print(result)