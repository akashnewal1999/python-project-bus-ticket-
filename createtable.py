import cx_Oracle
def jay():

    con=cx_Oracle.connect("sureshsir/dipti@localhost/xe")
    print("file is connected")
    cur=con.cursor()
    cur.execute("create table bus(busno number(10)primary key,busname varchar2(20)not null,ticket number(7)not null,seats number(7)not null)")
    print("table is created")

jay()