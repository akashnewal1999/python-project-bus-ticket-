import cx_Oracle
def ak():
    con=cx_Oracle.connect("sureshsir/dipti@localhost/xe")
    cur=con.cursor()
    cut="insert  into  bus1 values(141,'ngp to hyd',1000,50)"
    cur.execute(cut)
    #con.commit()
    cur.execute("select * from bus")
    print("*"*50)
    print("busno\tbusname\tticket seat")
    print("*"*50)
    for dt in cur:
        for data in dt:
            print(data, end='\t')
        print()

