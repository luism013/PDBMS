#dummy class for now
import PDBMSParser as parser

while True:
    try:
        s = input('DBMS-> ')
        s.lower()
    except EOFError:
        break
    if not s:
        continue
    result = parser.parser.parse(s)
    print(result)

