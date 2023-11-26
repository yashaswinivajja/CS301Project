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
    mycur.execute(qry)
    d = mycur.fetchall()
    for row in d:
	  print(row)
  if cc=='2':
    c=input('Enter the Category: ')
    qry='SELECT CategoryID from Category where CategoryName= %s;'
    mycur.execute(qry,c)
    if (ccc=mycur.fetchall)!= NULL:
      qry= 'SELECT * from Product where CategoryID = %s group by category;'
      mycur.execute(qry,ccc)
      d=mycur.fetchall()
      for row in d:
	      print(row)
  if cc=='3':

def addProduct():
	n=int(input('Enter number of products to be inserted: '))
	for j in range(n):
		t=()
		proid = input('Product ID : ')
		prname = input("Product Name: ")
		prsell = int(input('SellerID: '))
		pprice = int(input('MRP : '))
		prcat = int(input('CategoryID: '))
		pstk = int(input('Stock : '))
		pbrand = input('Brand: ')
		t = (proid, prname, prsell, pprice, prcat, pstk, pbrand)
		qry = 'INSERT into Product values(%s,%s,%s,%s,%s,%s,%s);'
		mycur.execute(qry, t)
		mycon.commit()
		print("Product Added")
					
def delProduct():
	delete=input("Enter ID of product to be deleted")
	qry = 'delete from Product where ProductID=%s;'
	mycur.execute(qry, (delt,))
	mycon.commit()
	print("Product is deleted")

def emp_sign_in():
	try:
		ask = input('Enter ID to sign in to the account: ')
		qry = 'select emp_id from employee;'
		mycur.execute(qry)
		d = mycur.fetchall()
		lis = []
		for i in d:
			lis.append(i[0])
		if ask not in lis:
			print('Enter the correct id')
		else:
			while True:
				space()
				ccc = input("1. Update delivered records\n2. Add a New Product \n3. Delete a product \nEnter 'Back' to logout: ")
				if ccc == '1':

print('WELCOME !')
while True:
	print("Enter your role:\n(A). Customer\n(B). Employee\n(C). Employer\n(D). Seller\nenter e to exit")
	ch = input('Enter: ')
	try:
		if ch in 'aA':
			print(" 1. Create Account\n 2.Sign In into existing account")
			choice = input('enter- ')
			if choice == '1':
				newCustAcc()
			elif choice == '2':
				sign_in()
			else:
				print('Enter correct choice')
		if ch in 'bB':
			emp_sign_in()
		if ch in 'cC':
			employer()
		if ch in 'dD':
			seller()
		elif ch.lower() == "e":
			print("Thankyou for visiting !")
			break
	except Exception:
		print('Give the right input')
	space()
