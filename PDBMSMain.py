#dummy class for now
import ply.lex as lex
import ply.yacc as yacc


# Reserved Words
reserved = {
    'from': 'FROM',
    'create': 'CREATE',
    'insert': 'INSERT',
    'add': 'ADD',
    'delete': 'DELETE',
    'get': 'GET',
    'display': 'DISPLAY',
    'as': 'AS',
    'join': 'JOIN',
    'where': 'WHERE',
    'update': 'UPDATE',
    'serial': 'SERIAL',
    'distinct': 'DISTINCT',
    'foreign': 'FOREIGN',
    'key': 'KEY',
    'cartesian': 'CARTESIAN',
    'product': 'PRODUCT',
    'selection': 'SELECTION',
    'projection': 'PROJECTION',
    'union': 'UNION',
    'intersection': 'INTERSECTION',
    'difference': 'DIFFERENCE'
}
