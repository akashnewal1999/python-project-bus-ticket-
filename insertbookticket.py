import cx_Oracle
def ticket():
    con=cx_Oracle.connect("sureshsir/dipti@localhost/xe")
    cur = con.cursor()
    var="insert into bus1 values(12,'nag to ban',100,48)"
    cur.execute(var)
    cur.execute("select * from bus1")
    print("\t\t------------------------------------------------------")
    print("\t\tbusno\tbusname\t\tticket\t\tseat")
    print("\t\t------------------------------------------------------")
    for val in cur:
        for tic in val:
            print("\t\t",tic,end="")
    print()
