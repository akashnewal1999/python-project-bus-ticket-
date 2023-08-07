import cx_Oracle
con=cx_Oracle.connect("sureshsir/dipti@localhost/xe")
cur=con.cursor()
cur.execute("delete from bus where(busno=141)")
con.commit()
print("data is deleted")