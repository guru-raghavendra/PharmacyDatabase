# importing module 
import sqlite3 

# connecting to the database
connection = sqlite3.connect("pharmacy.db") 

 
crsr = connection.cursor()

cont=1
while(cont):
    print("1: view table\n2: enter Prescription\n3: Purchase New Drugs from supplier\n")
    choice=int(input("enter your choice"))
    if(choice==1):
        print("1: Customer\n2: Doctor\n3: Drug_Supplier\n4: Drug\n")
        c=int(input("enter your choice"))
        if(c==1):
            crsr.execute("SELECT * FROM Customer")
            print("\tCUSTOMER TABLE\n(Customer_ID,First_Name,Middle_Name,Last_Name,Phone_Number)")
            ans = crsr.fetchall()
            for i in ans:
                print(i) 
        elif(c==2):
            crsr.execute("SELECT * FROM Doctor")
            print("\tDOCTOR TABLE\n(Medical_License_Number,First_Name,Middle_Name,Last_Name,Speciality,Phone_Number)")
            ans = crsr.fetchall()
            for i in ans:
                print(i) 
        elif(c==3):
            crsr.execute("SELECT * FROM Drug_Supplier")
            print("\tDRUG SUPPLIER TABLE\n(Supplier_ID,First_Name,Middle_Name,Last_Name,Phone_Number)")
            ans = crsr.fetchall()
            for i in ans:
                print(i) 
        elif(c==4):
            crsr.execute("SELECT * FROM Drug")
            print("\tDRUG TABLE\n(Drug Name,Supplier_ID,Quantity,Price)")
            ans = crsr.fetchall()
            for i in ans:
                print(i)
        elif(c==5):
            crsr.execute("SELECT * FROM Prescription")
            print("\tPrescription\n(Drug Name,Supplier_ID,Quantity,Price)")
            ans = crsr.fetchall()
            for i in ans:
                print(i)
        elif(c==6):
            crsr.execute("SELECT * FROM Zero")
            print("\tZero TABLE\nDrug Name\n")
            ans = crsr.fetchall()
            for i in ans:
                print(i)
    elif(choice==2):
        i=1
        total=0
        crsr.execute("SELECT datetime('now','localtime')")
        pdate=(crsr.fetchall()[0][0]).split()[0]
        p="""\n\nCUSTOMER ID: """
        con=1
        sql_command="""INSERT INTO Prescription Values("""
        sql_command+='\''
        x=input("Enter the customer id: ")
        p+=x
        p+='\nMEDICAL LICENCE NUMBER: '
        sql_command+=x;
        sql_command+='\','
        
        sql_command+='\''
        sql_command+=pdate
        sql_command+='\','
        
        sql_command+='\''
        x=input("Enter the medical licence number of the doctor: ")
        p+=x
        p+='\n\nyour purchace is\nDRUG NAME\tQUANTITY\tAMOUNT\n'
        sql_command+=x;
        sql_command+='\','

        while(i<=5 and con):  
            sql_command+='\''
            x=input("Enter the drug name"+str(i)+": ")
            y=x
            crsr.execute("SELECT Price,Quantity FROM Drug where Drug_Name='"+x+"';")
            ans = crsr.fetchall()
            print(ans)
            for z in ans:
                cc,qq=z
            
            sql_command+=x;
            sql_command+='\','
            p+=x
            p+='\t\t'
            x=input("Enter the quantity of drug"+str(i)+": ")
            

            p+=x
            p+='\t\t'
            if(qq>int(x)):
                crsr.execute("UPDATE Drug SET Quantity ="+str(qq-int(x))+" where Drug_Name='"+y+"';")
                p+=str(cc*int(x))
                total+=cc*int(x)
                sql_command+=x;
            else:
                crsr.execute("UPDATE Drug SET Quantity =0 where Drug_Name='"+y+"';")
                sql_command+='0'

                p+=str(cc*qq)
                total+=cc*qq
            p+='\n'
            if (i <5) :
                sql_command+=','
                con=int(input("to enter more press 1   else press 0:"))
            i=i+1
            
        while(i<=5):  
            sql_command+='NULL,'
            sql_command+='0'    
            if (i <=5) :
                sql_command+=','   
            i=i+1
        sql_command+=str(total)
        sql_command+=');'
        p+=('\nYOUR TOTAL AMOUNT IS: \t')
        p+=str(total)
        print(p)
        crsr.execute(sql_command)

        
    elif(choice==3):
        y=1
        total=0
        sid=input("enter the supplier id: ")
        bill="""\n\nSUPPLIER ID: """
        bill+=sid
        bill+='\nDRUG NAME\tQUANTITY\tPRICE\tTOTAL\n'
        while(y):
            print("1: purchase new drug\n2: purchase existing drug\n")
            c=int(input("enter your choice"))
            if(c==1):
                sql_command = """INSERT INTO Drug Values(\'"""
                n=input("enter the drug name: ")
                bill+=n
                bill+='\t\t'
                sql_command+=n
                sql_command+='\',\''
                sql_command+=sid
                sql_command+='\','
                q=input("enter the quantity: ")
                bill+=q
                bill+='\t\t'
                sql_command+=q
                sql_command+=','
                p=input("enter the price: ")
                bill+=p
                bill+='\t'
                bill+=str(int(q)*int(p))
                bill+='\n'
                sql_command+=p
                sql_command+=');'
               # 'AA','20000',12,14);
                crsr.execute(sql_command)
                total+=int(q)*int(p)
            elif(c==2):
                n=input("enter the drug name: ")
                q=input("enter the quantity: ")
                p=input("enter the price: ")
                bill+=n
                bill+='\t\t'
                bill+=q
                bill+='\t\t'
                bill+=p
                bill+='\t\t'
                bill+=str(int(q)*int(p))
                bill+='\n'
                total+=int(q)*int(p)
                crsr.execute("SELECT Quantity FROM Drug where Drug_Name='"+n+"';")
                ans = crsr.fetchall()
                print(ans)
                for i in ans:
                    qq=i
                ans=qq
                for i in ans:
                    qq=i
                crsr.execute("UPDATE Drug SET Quantity ="+str(int(q)+qq)+",Price ="+p+" where Drug_Name='"+n+"';")
            y=int(input("to do purchase more  press 1   else press 0: "))
            if(y==0):
                bill+=('\nYOUR TOTAL AMOUNT IS: \t')
                bill+=str(total)
                print(bill)
    cont=int(input("to do more operations press 1   else press 0: "))   





print("complex querries\n")
print("\nQuerry 1\n")
sql_command="""CREATE VIEW V1 AS SELECT Supplier_ID,First_Name,Middle_Name,Last_Name
            FROM Drug_Supplier AS ds WHERE ds.Supplier_ID  IN
            ( SELECT Supplier_ID FROM Drug_Supplier EXCEPT SELECT Supplier_ID FROM Drug);"""
crsr.execute(sql_command)

crsr.execute("SELECT * FROM V1")
ans = crsr.fetchall()
for i in ans:
    print(i)

crsr.execute("DROP VIEW V1")


print("\nQuerry 2\n")
sql_command="""SELECT DISTINCT Speciality
                FROM
            ( Doctor NATURAL JOIN Prescription )
            ;"""
crsr.execute(sql_command)
ans = crsr.fetchall()
#print(ans)
for i in ans:
    print(i)

print("\nQuerry 3\n")
sql_command=""" SELECT SUM(Total)
                FROM Prescription
                WHERE PDate="2020-05-28"
            ;"""
crsr.execute(sql_command)
ans = crsr.fetchall()
#print(ans)
for i in ans:
    print(i)


print("\nQuerry 4\n")
sql_command=""" SELECT Medical_License_Number , SUM(Total)
                FROM 
                (  Doctor NATURAL JOIN Prescription )
                GROUP BY Medical_License_Number
            ;"""
crsr.execute(sql_command)
ans = crsr.fetchall()
#print(ans)
for i in ans:
    print(i)


# To save the changes in the files. Never skip this. 
# If we skip this, nothing will be saved in the database. 
connection.commit() 




# close the connection 
connection.close() 
