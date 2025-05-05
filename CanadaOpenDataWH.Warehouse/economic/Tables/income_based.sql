CREATE TABLE [economic].[income_based] (

	[REF_DATE] bigint NULL, 
	[GEO] varchar(8000) NULL, 
	[DGUID] varchar(8000) NULL, 
	[Estimates] varchar(8000) NULL, 
	[UOM] varchar(8000) NULL, 
	[UOM_ID] bigint NULL, 
	[SCALAR_FACTOR] varchar(8000) NULL, 
	[SCALAR_ID] bigint NULL, 
	[VECTOR] varchar(8000) NULL, 
	[COORDINATE] float NULL, 
	[VALUE] float NULL, 
	[DECIMALS] bigint NULL
);