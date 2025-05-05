CREATE TABLE [CanadaOpenDataWH].[central1].[Configuration]
(
	[BankID] [int] NOT NULL,
	[BankName] [VARCHAR](30)  NOT NULL,
	[BlobContainerName] [VARCHAR] (50)  NOT NULL,
	[IndexName] [VARCHAR](30)  NOT NULL,
	[NetIncomeTrends] [VARCHAR](30)  NOT NULL,
    [ProfitMargin] [VARCHAR](30)  NOT NULL,
    [ProductRevenue] [VARCHAR](30)  NOT NULL,
    [GrossMargin] [VARCHAR](30)  NOT NULL

)
GO

-- select * from [CanadaOpenDataWH].[central1].[Configuration]
-- drop table [CanadaOpenDataWH].[central1].[Configuration]
Insert into [CanadaOpenDataWH].[central1].[Configuration] values (1, 'CitiGroup','citigroup-input-documents','citigroup-rag-ai-index','CitiGroup_NetIncomeTrends','CitiGroup_ProfitMargin','CitiGroup_ProductRevenue','CitiGroup_GrossMargin')
Insert into [CanadaOpenDataWH].[central1].[Configuration] values (2, 'GoldmanSachs','goldmansachs-input-documents','goldmansachs-rag-ai-index','GoldmanSachs_NetIncomeTrends','GoldmanSachs_ProfitMargin','GoldmanSachs_ProductRevenue','GoldmanSachs_GrossMargin')
Insert into [CanadaOpenDataWH].[central1].[Configuration] values (3, 'JPMC','jpmc-input-documents','jpmc-rag-ai-index','JPMC_NetIncomeTrends','JPMC_ProfitMargin','JPMC_ProductRevenue','JPMC_GrossMargin')
Insert into [CanadaOpenDataWH].[central1].[Configuration] values (4, 'WellsFargo','wellsfargo-input-documents','wellsfargo-rag-ai-index','WellsFargo_NetIncomeTrends','WellsFargo_ProfitMargin','WellsFargo_ProductRevenue','WellsFargo_GrossMargin')