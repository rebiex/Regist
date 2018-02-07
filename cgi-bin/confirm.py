#!/usr/bin/python
import pymysql,cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()

confirm = form.getvalue('confirm')
answer = form.getvalue('answer')
name = form.getvalue('name')
email = form.getvalue('email')

sql = 'SELECT email from regist_tbl'

if confirm == 'no':
	print ("Content-type:text/html\r\n\r\n")

	print ("<HTML>")
	print ("<TABLE ALIGN=ABSLEFT BORDER=1 CELLSPACING=1 CELLPADDING=1 >")
	print ("<TR VALIGN=TOP>")
	print ("<TD>")
	print ("<pre>")
	print ("So, The Information Is Incorrect.")

	print ("<a href='/cgi-bin/regist.py'>Please Registration Again</a>")

	print ("<a href='/regist.html'>Back To Top</a>")
	print ("</pre>")
	print ("</TD>")
	print ("</TR>")

	print ("</TABLE>")

	print ("</HTML>")

else:
	print ("Content-type:text/html\r\n\r\n")
	print ("<HTML>")
	print ("<TABLE ALIGN=ABSLEFT BORDER=1 CELLSPACING=1 CELLPADDING=1 >")
	print ("<TR VALIGN=TOP>")
	print ("<TD>")
	print ("<pre>")
	print ("Registration Successful")

	print ("Thanks")
	print ("</pre>")
	print ("</TD>")
	print ("</TR>")

	print ("</TABLE>")
	print ("</HTML>")

	if answer == 'yes':
		db = pymysql.connect("localhost","scanNskip","scanNskippass","Regist")
		cursor = db.cursor()
		try:
			print("Prepare to insert")
			cursor.execute("""INSERT INTO regist_tbl VALUES('%s', '%s')""" %(name, email))
			db.commit()
			print("Data inserted")
		except:
			print("Exception detected")
			db.rollback()
		db.close()


