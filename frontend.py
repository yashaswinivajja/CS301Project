import mysql.connector
mycon=mysql.connector.conect(host='localhost', user='root', password='password', database='shopping')
mycur=mycon.cursor

def space():
  for i in range(1):
    print()

def check():
  qry='SELECT CustomerID from Customer;'
  mycur.execute(qry)
  d=mycur.fetchall()
  listOfIDs=[]
  for ids in d:
    listOfIDs.append(d[0])
  mycon.commit()
  return listOfIDs

def newCustAcc():
  list_of_ids = check()
  i=True
  while i:
    custid = int(input('Enter your Customer id: '))
    if custid in list_of_ids:
      print('Customer ID already exists. Please choose another')
    else:
      print('* indicates mmandatory')
      cdetails=()
      cfname= input('Enter First Name*: ')
      cmname= input('Enter Middle Name: ')
      clname= input('Enter Last Name: ')
      cmail= input('Enter MailID: ')
      cdob= input('Enter Date of Birth: ')
      cphone= input('Enter Phone number*: ')
      cage= input('Enter Age: ')
      cdetails=(cfname, cmname, clname, cmail, cdob, cphone, cage)
      qry = 'INSERT into Customer values(%s,%s,%s,%s,%s,%s,%s,%s);'
      mycur.execute(qry,cdetails)
      mycon.commit()
      print('Customer details entered')
      i=False

def viewProducts():
  print('''
  1) all products
  2) By Category
  3) By price
  4) By search
  ''')
  cc= int(input('Enter your view: '))
  if cc=='1':
    qry= 'SELECT * from Product;'
  if cc=='2':
    c=input('Enter the Category: ')
    qry='SELECT CategoryID from Category where CategoryName= %s;'
    mycur.execute(qry,c)
    if mycur.fetchall!= NULL:
      qry= 'SELECT * from Product where CategoryID = %s group by category;'
  mycur.execute(qry)
	d = mycur.fetchall()
	for row in d:
		print(row)
	mycon.commit()
