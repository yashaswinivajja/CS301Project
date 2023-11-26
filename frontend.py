import mysql.connector
myconnector=mysql.connector.connect(host='localhost', user='root', password='password', database='shopping')
mycursor=myconnector.cursor()
def check():
  qry='select cust_id from customer;'
  mycursor.execute(qry)
  d=mycursor.fetchall()
  list=[]
  for ids in d:
  list.append(ids[0])
  return list
def cust_ac():
  while(i):
  custid = int(input('Enter your customer id...   '))
  if custid in list_of_ids
  i=true
  print('This Customer Id already exists....\Create a new one')
  else i=false
  c_det = ()
  cnam = input('First Name : ')
  clnam = input('Last Name : ')
  cphno = input('Phone Number : ')
  cadrs = input('Your Address : ')
  c_det = (custid, cnam, clnam, cphno, cadrs)
  qry = 'insert into customer values(%s,%s,%s,%s,%s,NULL);'
  val=c_det
  mycursor.execute(qry,val)
  myconnector.commit()
  print('Customer details entered')
def sign_in():
def emp_sign_in():
def AddProduct():
def DelProduct():
def EditProduct():
def ViewProduct():
def ViewCart(cust_id):
  qry = 'select  from  where cust_id=%s;'
  mycursor.execute(qry, (cust_id,))
  bp = mycursor.fetchone()
  cart_pro = bp[0]
    return cart_pro
def PurchaseProduct():
def ViewPurchase():
def ViewStock():
def SaleProduct():
def ViewSales():
def MenuSet():
