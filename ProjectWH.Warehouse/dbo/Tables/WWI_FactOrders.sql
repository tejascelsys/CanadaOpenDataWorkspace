CREATE TABLE [dbo].[WWI_FactOrders] (

	[OrderID] bigint NULL, 
	[CustomerID] varchar(8000) NULL, 
	[EmployeeID] bigint NULL, 
	[OrderDate] varchar(8000) NULL, 
	[RequiredDate] varchar(8000) NULL, 
	[ShippedDate] varchar(8000) NULL, 
	[ShipVia] bigint NULL, 
	[Freight] float NULL, 
	[ShipName] varchar(8000) NULL, 
	[ShipAddress] varchar(8000) NULL, 
	[ShipCity] varchar(8000) NULL, 
	[ShipRegion] varchar(8000) NULL, 
	[ShipPostalCode] varchar(8000) NULL, 
	[ShipCountry] varchar(8000) NULL, 
	[Column1] varchar(8000) NULL
);