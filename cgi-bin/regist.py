#!/usr/bin/python
import cgi, cgitb
cgitb.enable()

print ("Content-type:text/html\r\n\r\n")
print ("<HTML>")
print ("<HEAD>")
print ("<TITLE>Registration Form</TITLE>")
print ("</HEAD>")
print ("<form action='/cgi-bin/process.py' method=POST>")
print ("Nmae: <input type=text name=name value='' size=23>")
print ("<br>")
print ("Email: <input type=text name=email value='' size=23>")
print ("<input type=submit value=Submit name=B1>")        
print ("<input type=reset value=Reset name=B2>")
print ("</form>")
print ("</BODY>")
print ("</HTML>")