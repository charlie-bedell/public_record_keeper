from make_db_file import load_dbase

db = load_dbase()
for key in db:
    print(key, '=>\n', db[key])