import cx_Oracle
def tic():
    con=cx_Oracle.connect("sureshsir/dipti@localhost/xe")
    cur=con.cursor()
    qry="create table bus1(busno number(10)primary key,busname varchar(20)not null,ticket number(10)not null,seat number(20)not null)"

    cur.execute(qry)
    print("table is created")
tic()