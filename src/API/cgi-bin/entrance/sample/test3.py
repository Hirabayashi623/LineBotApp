import codecs
import cgi

text_html = ''

fin  = codecs.open('./html/entrance/sample/test3.html','r', 'utf_8')

for line in fin:
    text_html += line

dict = {}
form=cgi.FieldStorage()

dict['text'] = form.getvalue("text","")

print("Content-type: text/html\n")
print(text_html % dict)