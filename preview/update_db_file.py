from make_db_file import load_dbase, store_dbase

db = load_dbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
store_dbase(db)