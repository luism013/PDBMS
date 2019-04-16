import ply.lex as lex
import decimal


# Reserved Words
reserved = {
    'from': 'FROM',
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
    'name': 'NAME'
}


tokens = ['LPAR', 'RPAR', 'COMMA', 'SCOLON', 'DIGITS', 'WORDS', 'GTHAN', 'LTHAN', 'GETHAN', 'LETHAN', 'ETO', 'PLUS',
          'MINUS', 'DIV', 'MOD', 'MULT', 'COMMA', 'NLINE', 'WS'] \
         + list(reserved.values())


reserved_words_map = {}
for r in reserved:
    reserved_words_map[r.lower()] = r


def WORDS(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Checking the reserved words
    token.type = reserved.get(token.value, 'IDENTIFIER')
    return token


def DIGITS(token):
    r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
    token.value = decimal.Decimal(token.value)
    return token


def LPAR(t):
    r'\('
    return t


def RPAR(t):
    r'\)'
    return t


def GTHAN(t):
    r'\>)'
    return t


def LTHAN(t):
    r'/<'
    return t


def GETHAN(t):
    r'>='
    return t


def LETHAN(t):
    r'<='
    return t


def ETO(t):
    r'=='
    return t


def PLUS(t):
    r'\+'
    return t


def MINUS(t):
    r'\-'
    return t


def MULT(t):
    r'\*'
    return t


def DIV(t):
    r'\/'
    return t


def MOD(t):
    r'\%'
    return t


def COMMA(t):
    r'\,'
    return t

def SCOLON(t):
    r'\;'
    return t


def NLINE(token):
    r'\n+'
    token.lexer.lineno += len(token.value)
    return token


def WS(t):
    r' [ ]+ '


lexer = lex.lex()
