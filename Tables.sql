create database Ecommerce;
use Ecommerce;

create table Category(
    CategoryID numeric(10),
    CategoryName varchar(50),
    Decsription varchar(100),
    primary key (CategoryID)
    );

 create table Seller(
    SellerID numeric(10),
    Name varchar(100),
    Phone numeric(10),
    ToatalSales numeric(10),
    primary key (SellerID)
    );

create table Customer(
    CustomerID numeric(10),
    FirstName varchar(50),
    MiddleName varchar(50),
    LastName varchar(50),
    Email varchar(100),
    DateOfBirth date,
    Phone numeric(10),
    Age numeric(3),
    primary key (CustomerID)
    );

create table Review(
    ReviewID numeric(10),
    Description varchar(200),
    Ratings numeric(2,2),
    ProductID numeric(10),
    CustomerID numeric(10),
    primary key (ReviewID),
    foreign key (CustomerID) references Customer (CustomerID) on delete set null
    );

create table Address(
    AddressID numeric(10),
    StreetName varchar(50),
    ApartmentNo varchar(50),
    City varchar(50),
    State varchar(50),
    Pincode numeric(10),
    CustomerId numeric(10),
    primary key (AddressID),
    foreign key (CustomerID) references Customer (CustomerID) on delete cascade
    );

create table Product(
    ProductID numeric(10),
    ProductName varchar(100),
    SellerID numeric(10),
    MRP numeric(10,2),
    CategoryID numeric(10),
    Stock varchar(10),
    Brand varchar(100),
    primary key (ProductID),
    foreign key (SellerID) references Seller (SellerID),
    foreign key (CategoryID) references Category (CategoryID) on delete cascade
    );

create table Cart(
    CartID numeric(10),
    CustomerID numeric(10),
    ProductID numeric(10),
    Quantity numeric(5),
    primary key (cartID, ProductID),
    foreign key (CustomerID) references Customer (CustomerID) on delete cascade,
    foreign key (ProductID) references Product (ProductID) on delete cascade
    );

create table Order_(
    OrderID numeric(10),
    OrderNo numeric(10),
    ShippingDate datetime(2),
    OrderDate datetime(2),
    OrderAmount numeric(5),
    CartID numeric(10),
    CustomerID numeric(10),
    OrderStatus varchar(10),
    PaymentID numeric(10),
    AddressID numeric(10),
    primary key (OrderID),
    foreign key (PaymentID) references Payment (PaymentID),
    foreign key (AddressID) references Address (AddressID),
    foreign key (CartID) references Cart (CartID) on delete cascade,
    foreign key (CustomerID) references Customer (CustomerID) on delete cascade
    );

create table OrderItem(
    OrderID numeric(10),
    ProductID numeric(10),
    MRP numeric(20,3),
    Quantity numeric(5),
    foreign key (OrderID) references Order_ (OrderID),
    foreign key (ProductID) references Product (ProductID)
    );

create table Payment(
    PaymentID numeric(10),
    PaymentMode varchar(50),
    CustomerID numeric(10),
    DateOfPayment datetime(2),
    primary key (PaymentID),
    foreign key (CustomerID) references Customer (CustomerID) on delete cascade
    );
