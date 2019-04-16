#dummy class for now
import PDBMSParser

while True:
    try:
        s = input('DBMS-> ')
        s.lower()
    except EOFError:
        break
    if not s: continue
    result = PDBMSParser.parser.parse(s)
    print(result)

