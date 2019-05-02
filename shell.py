import PDBMSParser as parser

while True:
    try:
        s = input('DBMS-> ')
        s.lower()
    except EOFError:
        break
    if not s:
        continue
    result = parser.yacc.parse(s)
    print(result)

