#!/usr/bin/python
import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()

name = form.getvalue('name')
email = form.getvalue('email')

print ("Content-type:text/html\r\n\r\n")
print ("<HTML>")

print ("Registration Form")

print ("<table align=center datasrc='#xmlRegData' border=2>")
print ("<tr>")
print ("<td> Name:</td>")
print ("<td/>%s"% (name))
print ("</tr>")
print ("<tr>")
print ("<td>E-mail:</td>")
print ("<td/>%s"% (email))
print ("</tr>")
print ("</table>")

print ("Is this information correct ?")
print ("<form method=POST action=/cgi-bin/confirm.py>")

print ("<input type=submit value=Submit>")     
print ("<input type=reset value=Reset>")

print ("<input type=radio name='confirm' value='yes'> YES")   
print ("<input type=radio name='confirm' value='no' checked> NO")
print("<input type='hidden' name='name' value='%s'/>" % name)
print("<input type='hidden' name='email' value='%s'/>" % email)

print ("Insert into database ?")
print ("</font><input type=radio name='answer' value='yes'>YES") 
print ("<input type=radio name='answer' value='no' checked>NO <br>")

print ("</form>")
print ("</HTML>")
