import mysql.connector
from datetime import datetime 
mycon=mysql.connector.conect(host='localhost', user='root', password='password', database='shopping')
mycur=mycon.cursor

def check():
	qry='SELECT CustomerID from Customer;'
	mycur.execute(qry)
	d=mycur.fetchall()
	cids = [ids[0] for ids in d]
	mycon.commit()
	return cids
def custAcc(opt,custoID):
	if opt == 0:
		list_of_ids = check()
		i = True
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
				sdob= input('Enter Date of Birth DD/MM/YYYY: ')
				try:
					cdob = datetime.strptime(sdob, "%d/%m/%Y")
				except ValueError:
					print("Invalid date format. Please use DD/MM/YYYY")
				cphone= int(input('Enter Phone number*: '))
				cage= int(input('Enter Age: '))
				cdetails=(custid, cfname, cmname, clname, cmail, cdob, cphone, cage)
				qry = 'INSERT into Customer values(%d,%s,%s,%s,%s,%s,%d,%d);'
				mycur.execute(qry,cdetails)
				mycon.commit()
				print('Customer details entered')
				i=False
	if opt == 1:
		qry = 'SELECT * from Customer where customerID = %d;'
		mycur.execute(qry,(custoID,))
		d = mycur.fetchall()
		d[0] = custoID
		print('1)First Name\n2) Middle Name\n3) Last Name\n4) MailID\n5) Date of Birth\n6)Phone number\n7)Age\n8)No edit')
		p = int(input('Enter number of details to edit: '))
		for i in range(p):
			ch = input('Enter the detail number to edit: ')
			if ch == 1:
				d[1] = input('Enter First name: ')
			if ch == 2:
				d[2] = input('Enter Middle name: ')	
			if ch == 3:
				d[3] = input('Enter Last Name: ')
			if ch == 4:
				d[4] = input('Enter MailID: ')
			if ch == 5:
				dob = input('Enter Date of Birth DD/MM/YYYY: ')
				try:
					d[5] = datetime.strptime(sdob, "%d/%m/%Y")
				except ValueError:
					print("Invalid date format. Please use DD/MM/YYYY")
			if ch == 6:
				d[6] = int(input('Enter Phone number: '))
			if ch == 7:
				d[7] = int(input('Enter Age: '))
			if ch == 8:
				break
			else:
				print('Enter correct choice')
			if (ch<9 & ch>0):
				qry = 'DELETE from Customer where CustomerID = %d;'
				mycur.execute(qry,(custoID,))
				qry = 'INSERT into Customer values(%d,%s,%s,%s,%s,%d,%d);'
				mycur.execute(qry,d)
				mycon.commit()
		print('Edit details completed')
			
def custSignIn():
	try:
		ask = int(input('Enter customer ID to sign in : '))
		list_of_ids = check()
		if ask in list_of_ids:
			while True:
				ch = int(input('1) Products\n2) Cart\n3) My Orders\n4) Update Self Details\nEnter your column choice: '))
				if ch == 1:
					viewProduct()
					cc = input('Do you want to select any product(Y/N): ')
					if cc in yY:
						selectProduct(ask)
						ccc = int(input('1)Just View\n2)Add to cart\nEnter: '))
						if ccc == 2:
							cartOperations(1)
					else: 
						continue
				if ch == 2:
					cc = int(input("Enter your choice:\n1)Add a product\n2)Delete a product\n3)View the cart\n4)Buy now"))
						 cartOperations(cc)
				if ch == 3:
					myPurchase()
				if ch = 4:
					custAcc(1)
				if ch == 5:
					break
					
				
def myPurchase():
	print("1)View purchases\n2)Cancel Purchase\n3)Reorder\n4)track purchase\n5)Exit")
	while True:
	ch = int(input(Enter your choice: ))
	if ch==1:
		qry = 'SELECT * from Order, Orderitem where Order.OrderID = Orderitem.OrderID;'
		mycur.execute(qry)
		d = mycur.fetchall()
		for row in d:
			print(row)
	if ch == 2:
		p = int(input('Enter the Order ID of the order you want to cancel purchase: '))
		qry = 'DELETE from Order where OrderID = %d;'
		mycur.execute(qry,(p,))
		print('Purchase cancelled!! Transaction will be done to your account in max two working days')
	if ch == 3:
	if ch == 4:
		p = int(input('Enter the Order ID of the order you want to track purchase: ')
		qry = 'SELECT Orderstatus from Order where OrderID = %d;'
		mycur.execute(qry,(p,))
		d = mycur.fetchall()
		for row in d:
			print(row)
	if ch == 5:
		break
		
def selectProduct(custID):
	pid = int(input('Enter the ProductID of the product selected: '))
	return pid
	
def review():
	ch = int(input('1) View reviews for a product\n2) Write review for a product\nEnter you choice: ')
	if ch == 1:
		p = int(input("Enter the productID for which view reviews: "))
		qry = 'SELECT * from Review where ProductID = %d group by ProductID;'
		mycur.execute(qry,(p,))
		d = mycur.fetchall()
		for row in d:
			print(row)
	if ch == 2:
		pid = selectProduct(cid)
		p = input('Enter your Review description: ')
		q = int(input('Enter your Ratings: '))
		tuple = (rid, p, q, pid, cid)
		qry = 'INSERT into Review values(%d,%s,%d,%d,%d);'
		mycur.execute(qry,tuple)

def cartOperations(ch,iD):
	if ch == 1:
		addProduct(2,iD)
	if ch == 2:
		delProduct(2,iD)
	if ch == 3:
		cartid=int(str(iD)[::-1])
		qry = 'SELECT * from Cart where CartID= %d;'
		mycur.execute(qry,(cartid,))
		d = mycur.fetchall()
		mycon.commit()
		for row in d:
			print(row)
	if ch == 4:
		tuple=
		qry = 'INSERT into Order values(%d,%d,%,%,%d,%d,%d,%s,%d,%d);'
		mycur.execute(qry,tuple)
def viewProduct():
	while 1:
	print('''
	1) all products
	2) By Category
	3) By price
	4) By search
 	5) By Recommendation
 	6) Exit
	''')
	cc= int(input('Enter your view: '))
	if cc == 1:
		qry= 'SELECT * from Product;'
    		mycur.execute(qry)
    		d = mycur.fetchall()
    		for row in d:
	  		print(row)
  	if cc == 2:
    		c=input('Enter the Category: ')
    		qry='SELECT CategoryID from Category where CategoryName= %s;'
   		mycur.execute(qry,c)
    		if (ccc=mycur.fetchall)!= NULL:
      			qry= 'SELECT * from Product where CategoryID = %s group by category;'
      			mycur.execute(qry,ccc)
      			d=mycur.fetchall()
      			for row in d:
	      			print(row)
  	if cc == 3:
		c= int(input('Enter Max price: '))
		qry = 'SELECT * from Product where MRP <= %d;'
		mycur.execute(qry,(c,))
		d=mycur.fetchall()
		for row in d:
			print(row)
	if cc == 4:
		c=input('Enter Product Name: ')
      		qry= 'SELECT * from Product where Product name = %s group by product name;'		
   		mycur.execute(qry,c)
		d=mycur.fetchall()
      		for row in d:
	      		print(row)
	if cc == 5:
	if cc == 6:
		break

def addProduct(choice,ID):
	if choice == 1:
		n=int(input('Enter number of products to be inserted: '))
		for j in range(n):
			t=()
			proid = int(input('Product ID : '))
			prname = input("Product Name: ")
			prsell = ask
			print("SellerID: %d" %ID))
			pprice = int(input('MRP : '))
			prcat = int(input('CategoryID: '))
			pstk = input('Stock : ')
			pbrand = input('Brand: ')
			t = (proid, prname, prsell, pprice, prcat, pstk, pbrand)
			qry = 'INSERT into Product values(%d,%s,%d,%d,%d,%s,%s);'
			mycur.execute(qry, t)
			mycon.commit()
			print("Product Added")
	if choice == 2:
		tuple=()
		cid = ID
		pid = selectProduct(ID)
		cartid=int(str(ID)[::-1])
		qry = 'SELECT Quantity form Order where ProductID = %d;'
		mycur.execute(qry,(pid,))
		nump = mycur.fetchall()
		if len(nump) == 0:
			nump = nump[0]+1
			tuple = (cartid, pid, cid, nump)
			qry = 'INSERT into Cart values(%d,%d,%d,%d);'
			mycur.execute(qry, tuple)
			mycon.commit()
		else:
			nump= nump[0]+1
			qry  = 'update Order set Quantity = %d where ProductID = %d;'
			mycur.execute(qry,(nump,pid))
			mycon.commit()
		print('Product added to cart by one unit')
		
def delProduct(choice,ID):
	if choice == 1:
		delete=int(input("Enter ID of product to be deleted"))
		qry = 'DELETE from Product where ProductID = %d;'
		mycur.execute(qry, (delt,))
		mycon.commit()
		print("Product is deleted by Seller: %d" %ID)
	if choice == 2: 
		tuple= ()
		pid = selectProduct(ID)
		cartid=int(str(ID)[::-1])
		qry = 'SELECT Quantity form Order where ProductID = %d;'
		mycur.execute(qry,(pid,))
		nump = mycur.fetchall()
		nump--
		if nump>0:
			qry = 'update Cart set Quantity = %d where ProductID = %d;'
			mycur.execute(qry,(nump, pid))
			mycon.connect()
		else:
			qry = 'delete from Order where ProductID = %d;'
			mycur(qry,(pid,))
			mycon.commit()
		print('Product deleted from cart by one unit')

def addSeller(): 
	n=int(input('Enter number of sellers to add: '))
	for i in range(n):
		tuple=()
		sid = int(input('Enter SellerID: '))
		name = input('Enter Seller Name: ')
		phno = int(input('Enter phone number: '))
		tots = int(input('Enter total sales: ')
		tuple = (sid, name, phno, tots)
		qry = 'INSERT into Seller values(%d,%s,%d,%d);'
		mycur.execute(qry,tuple)
		mycon.commit()
		print("Seller added")
	
def sellerSignIn():
	try:
	        ask = int(input('Enter ID to sign in to the account: '))
		qry = 'SELECT SellerID from Seller;'
		mycur.execute(qry)
		d = mycur.fetchall()
		lis = []
		for i in d:
			lis.append(i[0])
		if ask not in lis:
			print('Enter the correct id')
		else:
			while True:
				ccc = input("1. Add a New Product \n2. Delete a product\n3. View stock\n4. Collection\nEnter 'Back' to logout: ")
				if ccc=='1':
					addProduct(1,ask)
				if ccc='2':
					deleteProduct(1,ask)
				if ccc='3':
					pid = int(input('Enter ProductID to view stock: '))
					qry='SELECT stock from Product where ProductID = %d;'
					mycur.execute(qry,pid)
					stk = mycur.fetchall()
					print('Stock of the product with  productID:%d = %s' %pid, %stk)
					
				elif ccc.lower() == 'back':
					print("Successfully logged out ")
					break
	except Exception:
		print('Give the correct input')	


print('WELCOME !')
while True:
	print("Choose your role: Customer\SellerSales\SellerFinance")
	ch = input('Enter: ')
	try:
		if ch.lower() == "Customer":
			print(" 1. Create Account\n2. Sign In into existing account")
			choice = int(input('enter: '))
			if choice == '1':
				custAcc(0,0)
			elif choice == '2':
				custSignIn()
			else:
				print('Enter correct choice')
		if ch.lower() == "Seller"
			
		elif ch.lower() == "e":
			print("Thankyou for visiting !")
			break
	except Exception:
		print('Give the right input')
