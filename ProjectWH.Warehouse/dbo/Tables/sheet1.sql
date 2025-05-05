CREATE TABLE [dbo].[sheet1] (

	[ProductID] bigint NULL, 
	[ProductName] varchar(8000) NULL, 
	[SupplierID] bigint NULL, 
	[CategoryID] bigint NULL, 
	[QuantityPerUnit] varchar(8000) NULL, 
	[UnitPrice] float NULL, 
	[UnitsInStock] bigint NULL, 
	[UnitsOnOrder] bigint NULL, 
	[ReorderLevel] bigint NULL, 
	[Discontinued] bit NULL
);