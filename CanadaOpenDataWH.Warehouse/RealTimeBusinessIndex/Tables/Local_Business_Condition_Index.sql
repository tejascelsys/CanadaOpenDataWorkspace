CREATE TABLE [RealTimeBusinessIndex].[Local_Business_Condition_Index] (

	[REF_DATE (date)] date NULL, 
	[GEO] varchar(8000) NULL, 
	[DGUID] varchar(8000) NULL, 
	[UOM] varchar(8000) NULL, 
	[UOM_ID] bigint NULL, 
	[SCALAR_FACTOR] varchar(8000) NULL, 
	[SCALAR_ID] bigint NULL, 
	[VECTOR] varchar(8000) NULL, 
	[COORDINATE] bigint NULL, 
	[VALUE] float NULL, 
	[STATUS] varchar(8000) NULL, 
	[SYMBOL] varchar(8000) NULL, 
	[TERMINATED] varchar(8000) NULL, 
	[DECIMALS] bigint NULL
);