-- ################################# CitiGroup ##############################
-- DROP TABLE [CanadaOpenDataWH].[central1].[CitiGroup_NetIncomeTrends]
CREATE TABLE [CanadaOpenDataWH].[central1].[CitiGroup_NetIncomeTrends]
(
	[Year] [int]  NOT NULL,
	[Quarter] [int]  NOT NULL,
	[NetIncome] [float]  NULL
)
GO
-- DROP TABLE [CanadaOpenDataWH].[central1].[CitiGroup_ProfitMargin]
CREATE TABLE [CanadaOpenDataWH].[central1].[CitiGroup_ProfitMargin]
(
	[Year] [int]  NOT NULL,
	[NetIncome] [float]  NULL,
	[GrossRevenue] [float] NULL,
	[ProfitMargin] [float] NULL
)
GO
-- DROP TABLE [CanadaOpenDataWH].[central1].[CitiGroup_ProductRevenue]
CREATE TABLE [CanadaOpenDataWH].[central1].[CitiGroup_ProductRevenue]
(
	[ProductLine] [varchar](100)  NOT NULL,
	[Revenue] [float]  NOT NULL,
	[PercentageContribution] [float]  NOT NULL
)
GO
-- DROP TABLE [CanadaOpenDataWH].[central1].[CitiGroup_GrossMargin]
CREATE TABLE [CanadaOpenDataWH].[central1].[CitiGroup_GrossMargin]
(
	[Year] [int]  NOT NULL,
	[Quarter] [int]  NOT NULL,
	[TotalRevenue] [float]  NOT NULL,
	[COGS] [float]  NOT NULL,
	[GrossMargin] [float]  NOT NULL
)
GO
-- Drop table [CanadaOpenDataWH].[central1].[CitiGroup_NetRevenues]
CREATE TABLE [CanadaOpenDataWH].[central1].[CitiGroup_NetRevenues]
(
	[Year] [int]  NOT NULL,	
	[NetRevenue] [float]  NOT NULL,
	[NetInterestIncome] [float]  NOT NULL,
	[NonInterestRevenue] [float]  NOT NULL
)
GO
-- Drop table [CanadaOpenDataWH].[central1].[CitiGroup_Expenses_Losses_Claims]
CREATE TABLE [CanadaOpenDataWH].[central1].[CitiGroup_Expenses_Losses_Claims]
(
	[Year] [int]  NOT NULL,	
	[OperatingExpenses] [float]  NOT NULL,
	[ProvisionsForCreditLossesClaims] [float]  NOT NULL	
)
GO

-- ################################# GoldmanSachs ##############################--

-- DROP TABLE [CanadaOpenDataWH].[central1].[GoldmanSachs_NetIncomeTrends]
CREATE TABLE [CanadaOpenDataWH].[central1].[GoldmanSachs_NetIncomeTrends]
(
	[Year] [int]  NOT NULL,
	[Quarter] [int]  NOT NULL,
	[NetIncome] [float]  NOT NULL
)
GO
-- DROP TABLE [CanadaOpenDataWH].[central1].[GoldmanSachs_ProfitMargin]
CREATE TABLE [CanadaOpenDataWH].[central1].[GoldmanSachs_ProfitMargin]
(
	[Year] [int]  NOT NULL,
	[NetIncome] [float]  NOT NULL,
	[GrossRevenue] [float]  NOT NULL,
	[ProfitMargin] [float]  NOT NULL
)
GO
-- DROP TABLE [CanadaOpenDataWH].[central1].[GoldmanSachs_ProductRevenue]
CREATE TABLE [CanadaOpenDataWH].[central1].[GoldmanSachs_ProductRevenue]
(
	[ProductLine] [varchar](100)  NOT NULL,
	[Revenue] [float]  NOT NULL,
	[PercentageContribution] [float]  NOT NULL
)
GO
-- DROP TABLE [CanadaOpenDataWH].[central1].[GoldmanSachs_GrossMargin]
CREATE TABLE [CanadaOpenDataWH].[central1].[GoldmanSachs_GrossMargin]
(
	[Year] [int]  NOT NULL,
	[Quarter] [int]  NOT NULL,
	[TotalRevenue] [float]  NOT NULL,
	[COGS] [float]  NOT NULL,
	[GrossMargin] [float]  NOT NULL
)
GO
-- Drop table [CanadaOpenDataWH].[central1].[GoldmanSachs_NetRevenues]
CREATE TABLE [CanadaOpenDataWH].[central1].[GoldmanSachs_NetRevenues]
(
	[Year] [int]  NOT NULL,	
	[NetRevenue] [float]  NOT NULL,
	[NetInterestIncome] [float]  NOT NULL,
	[NonInterestRevenue] [float]  NOT NULL
)
GO
-- Drop table [CanadaOpenDataWH].[central1].[GoldmanSachs_Expenses_Losses_Claims]
CREATE TABLE [CanadaOpenDataWH].[central1].[GoldmanSachs_Expenses_Losses_Claims]
(
	[Year] [int]  NOT NULL,	
	[OperatingExpenses] [float]  NOT NULL,
	[ProvisionsForCreditLossesClaims] [float]  NOT NULL	
)
GO
-- ################################# JPMC ##############################
-- DROP TABLE [CanadaOpenDataWH].[central1].[JPMC_NetIncomeTrends]
CREATE TABLE [CanadaOpenDataWH].[central1].[JPMC_NetIncomeTrends]
(
	[Year] [int]  NOT NULL,
	[Quarter] [int]  NOT NULL,
	[NetIncome] [float]  NOT NULL
)
GO
-- DROP TABLE [CanadaOpenDataWH].[central1].[JPMC_ProfitMargin]
CREATE TABLE [CanadaOpenDataWH].[central1].[JPMC_ProfitMargin]
(
	[Year] [int]  NOT NULL,
	[NetIncome] [float]  NOT NULL,
	[GrossRevenue] [float]  NOT NULL,
	[ProfitMargin] [float]  NOT NULL
)
GO
-- DROP TABLE [CanadaOpenDataWH].[central1].[JPMC_ProductRevenue]
CREATE TABLE [CanadaOpenDataWH].[central1].[JPMC_ProductRevenue]
(
	[ProductLine] [varchar](100)  NOT NULL,
	[Revenue] [float]  NOT NULL,
	[PercentageContribution] [float]  NOT NULL
)
GO
-- DROP TABLE [CanadaOpenDataWH].[central1].[JPMC_GrossMargin]
CREATE TABLE [CanadaOpenDataWH].[central1].[JPMC_GrossMargin]
(
	[Year] [int]  NOT NULL,
	[Quarter] [int]  NOT NULL,
	[TotalRevenue] [float]  NOT NULL,
	[COGS] [float]  NOT NULL,
	[GrossMargin] [float]  NOT NULL
)
GO
-- Drop table [CanadaOpenDataWH].[central1].[JPMC_NetRevenues]
CREATE TABLE [CanadaOpenDataWH].[central1].[JPMC_NetRevenues]
(
	[Year] [int]  NOT NULL,	
	[NetRevenue] [float]  NOT NULL,
	[NetInterestIncome] [float]  NOT NULL,
	[NonInterestRevenue] [float]  NOT NULL
)
GO
-- Drop table [CanadaOpenDataWH].[central1].[JPMC_Expenses_Losses_Claims]
CREATE TABLE [CanadaOpenDataWH].[central1].[JPMC_Expenses_Losses_Claims]
(
	[Year] [int]  NOT NULL,	
	[PreProvisionProfit] [float]  NOT NULL,
	[ProvisionsForCreditLosses] [float]  NOT NULL	
)
GO
-- ################################# WellsFargo ##############################
-- DROP TABLE [CanadaOpenDataWH].[central1].[WellsFargo_NetIncomeTrends]
CREATE TABLE [CanadaOpenDataWH].[central1].[WellsFargo_NetIncomeTrends]
(
	[Year] [int]  NOT NULL,
	[Quarter] [int]  NOT NULL,
	[NetIncome] [float]  NOT NULL
)
GO
-- DROP TABLE [CanadaOpenDataWH].[central1].[WellsFargo_ProfitMargin]
CREATE TABLE [CanadaOpenDataWH].[central1].[WellsFargo_ProfitMargin]
(
	[Year] [int]  NOT NULL,
	[Quarter] [int]  NOT NULL,
	[NetIncome] [float]  NOT NULL,
	[GrossRevenue] [float]  NOT NULL,
	[ProfitMargin] [float]  NOT NULL
)
GO
-- DROP TABLE [CanadaOpenDataWH].[central1].[WellsFargo_ProductRevenue]
CREATE TABLE [CanadaOpenDataWH].[central1].[WellsFargo_ProductRevenue]
(
	[ProductLine] [varchar](100)  NOT NULL,
	[Revenue] [float]  NOT NULL,
	[PercentageContribution] [float]  NOT NULL
)
GO
-- DROP TABLE [CanadaOpenDataWH].[central1].[WellsFargo_GrossMargin]
CREATE TABLE [CanadaOpenDataWH].[central1].[WellsFargo_GrossMargin]
(
	[Year] [int]  NOT NULL,
	[Quarter] [int]  NOT NULL,
	[TotalRevenue] [float]  NOT NULL,
	[COGS] [float]  NOT NULL,
	[GrossMargin] [float]  NOT NULL
)
GO
-- Drop table [CanadaOpenDataWH].[central1].[WellsFargo_NetRevenues]
CREATE TABLE [CanadaOpenDataWH].[central1].[WellsFargo_NetRevenues]
(
	[Year] [int]  NOT NULL,	
	[NetRevenue] [float]  NOT NULL,
	[NetInterestIncome] [float]  NOT NULL,
	[NonInterestRevenue] [float]  NOT NULL
)
GO
-- Drop table [CanadaOpenDataWH].[central1].[WellsFargo_Expenses_Losses_Claims]
CREATE TABLE [CanadaOpenDataWH].[central1].[WellsFargo_Expenses_Losses_Claims]
(
	[Year] [int]  NOT NULL,	
	[Quarter] [int]  NOT NULL,
	[PreProvisionProfit] [float]  NOT NULL,
	[ProvisionsForCreditLosses] [float]  NOT NULL	
)
GO