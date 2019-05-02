import ply.lex as lex


reserved = {
    'create': 'CREATE',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'select': 'SELECT',
    'table': 'TABLE',
    'insert': 'INSERT',
    'values': 'VALUES',
    'into': 'INTO',
    'column': 'COLUMN',
    'where': 'WHERE',
    'record': 'RECORD',
    'all': 'ALL',
    'from': 'FROM',
    'show': 'SHOW',
    'entities': 'ENTITIES',
    'rename': 'RENAME',
    'entity': 'Entity',
    'tables': 'TABLES',
    'with': 'WITH',
    'at': 'AT',
    'to': 'TO',
    'row': 'ROW'
}

tokens = ['WORDS', 'NUMBER', 'LPAR', 'RPAR', 'COLON', 'EQUALS'] + list(reserved.values())


t_LPAR = r'\('

t_RPAR = r'\)'

t_COLON = r'\:'

t_EQUALS = r'\='


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