CREATE TABLE [MunicipalFinances].[mf_ea1_assessment] (

	[YEAR] bigint NULL, 
	[STATUS] varchar(8000) NULL, 
	[CODE] bigint NULL, 
	[MUNICIPALITY] varchar(8000) NULL, 
	[GRAND_TOTAL] bigint NULL, 
	[Linear_Subtotal] bigint NULL, 
	[Mach_&_Equip_Subtotal] float NULL, 
	[Non_Residential_Subtotal] float NULL, 
	[Residential_Subtotal] bigint NULL, 
	[Farmland] float NULL, 
	[Non_Residential_Railway] float NULL, 
	[NR__Res._Co-generating_M&E] float NULL
);