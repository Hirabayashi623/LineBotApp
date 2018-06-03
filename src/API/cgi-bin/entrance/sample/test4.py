import codecs
import cgi

text_html = ''

fin  = codecs.open('./html/entrance/sample/test4.html','r', 'utf_8')

for line in fin:
    text_html += line

dict = {}
form=cgi.FieldStorage()

dict['first'] = form.getfirst("check","not found")
dict['list'] = form.getlist("check")

print("Content-type: text/html\n")
print(text_html % dict)