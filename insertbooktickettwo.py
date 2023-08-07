import cx_Oracle
def tic():
    con=cx_Oracle.connect("sureshsir/dipti@localhost/xe")
    cur=con.cursor()
    var="insert into bus1 values(13,'nag to ban',100,50)"
    cur.execute(var)
    cur.execute("select * from bus1")
    print("-" * 50)
    print("busno\t\tbusname\t\tticket\tseat")
    print("-"*50)
    for dt in cur:
        for jk in dt:
            print(jk,end="\t\t")
    print()
#tic()