import cgi

print("Content-type: text/html\n")

form=cgi.FieldStorage()

print("form: ", form, "<br>")
print("form[value]: ", form["value"], "<br>")
print("form[value].value: ", form["value"].value, "<br>")

# getvalueメソッド　→　基本的には値の取得。なかったらデフォルト値（第2引数を返す）
print("form.getvalue: ", form.getvalue("value", "not found"), "<br>")
print("form.getvalue: ", form.getvalue("abc", "not found"), "<br>")
