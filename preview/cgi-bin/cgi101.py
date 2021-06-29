#!C:/Users/charl/AppData/Local/Programs/Python/Python39/python.exe
import cgi, html                    # cgi.escape() is deprecated, use html.escape()
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print(f"<h1>Hello <i>{html.escape(form['user'].value)}</i></h1>")