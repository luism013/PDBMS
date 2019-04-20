import ply.lex as lex
from ply.lex import TOKEN
import decimal


# Reserved Words
reserved = {
    'from':'FROM',
    'create': 'CREATE',
    'insert': 'INSERT',
    'delete': 'DELETE',
    'as': 'AS',
    'join': 'JOIN',
    'where': 'WHERE',
    'update': 'UPDATE',
    'serial': 'SERIAL',
    # 'distinct': 'DISTINCT',
    # 'foreign': 'FOREIGN',
    'key': 'KEY',
    # 'cartesian': 'CARTESIAN',
    # 'product': 'PRODUCT',
    # 'selection': 'SELECTION',
    # 'projection': 'PROJECTION',
    # 'union': 'UNION',
    # 'intersection': 'INTERSECTION',
    # 'difference': 'DIFFERENCE'
    'into': 'INTO',
    'values': 'VALUES',
    'select': 'SELECT',
    'references': 'REFERENCES',
    'name': 'NAME',
    'table': 'TABLE',
    'show': 'SHOW',
    'type': 'TYPE',
    'add': 'ADD',
    'subtract': 'SUBTRACT',
    'multiply': 'MULTIPLY'
}


tokens = ['WORDS', 'DIGITS', 'LPAR', 'RPAR', 'GTHAN', 'LTHAN' , 'GETHAN', 'LETHAN', 'ETO', 'PLUS', 'MINUS', 'MULT' , 'DIV',
          'MOD', 'COMMA', 'SCOLON', 'NLINE', 'WS'] \
         + list(reserved.values())


# reserved_words_map = {}
# for r in reserved:
#     reserved_words_map[r.lower()] = r


def t_WORDS(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Checking the reserved words
    token.type = reserved.get(token.value, 'IDENTIFIER')
    return token


def t_DIGITS(token):
    r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
    token.value = decimal.Decimal(token.value)
    return token


def t_LPAR(t):
    r'\('
    return t


def t_RPAR(t):
    r'\)'
    return t


def t_GTHAN(t):
    r'\>'
    return t


def t_LTHAN(t):
    r'/<'
    return t


def t_GETHAN(t):
    r'>='
    return t


def t_LETHAN(t):
    r'<='
    return t


def t_ETO(t):
    r'=='
    return t


def t_PLUS(t):
    r'\+'
    return t


def t_MINUS(t):
    r'\-'
    return t


def t_MULT(t):
    r'\*'
    return t


def t_DIV(t):
    r'\/'
    return t


def t_MOD(t):
    r'\%'
    return t


def t_COMMA(t):
    r'\,'
    return t


def t_SCOLON(t):
    r'\;'
    return t


def t_NLINE(token):
    r'\n+'
    token.lexer.lineno += len(token.value)
    return token


def t_WS(t):
    r' [ ]+ '


def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)


lexer = lex.lex()
data = '''
 3 + 4 * 10
   + -20 *2
 '''
lexer.input(data)
while True:
     tok = lexer.token()
     if not tok:
         break      # No more input
     print(tok)
