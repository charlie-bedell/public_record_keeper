# interactive queries
import shelve
from person import Person
fieldnames = ('name', 'age', 'job', 'pay')

db = shelve.open('class-shelve')
while True:
    key = input('\nKey? => ')  # key or empty line, exc at eof
    if not key: break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input(f'\t[{field}]={currval}\n\t\tnew?=>')
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
db.close()
        