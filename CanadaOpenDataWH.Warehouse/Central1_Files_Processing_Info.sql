CREATE TABLE [CanadaOpenDataWH].[central1].[Files_Processing_Info]
(
	[BankID] [int] NOT NULL,
	[FileName] [VARCHAR](50)  NOT NULL,
	[FileSubmittedDateTime] DATETIME2(3) ,
	[FileProcessedDateTime] DATETIME2(3) 
	)
GO

-- select * from [CanadaOpenDataWH].[central1].[Files_Processing_Info] order by BankID
-- drop table [CanadaOpenDataWH].[central1].[Files_Processing_Info]
-- delete from [CanadaOpenDataWH].[central1].[Files_Processing_Info]
-- ############### CITIGROUP DATA ########################
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (1, 'Citigroup-10K_Annual_2022.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (1, 'Citigroup-10Q_March2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (1, 'Citigroup-10Q_June2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (1, 'Citigroup_10Q_Sep2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (1, 'Citigroup-10Q_March2024.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (1, 'Citigroup-10Q_June2024.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (1, 'Citigroup_10Q_Sep2024.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (1, 'CitiGroup-10K_Annual_2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))

-- ############### GOLDMANSACHS DATA ########################
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (2, 'Goldman-10K_Annual_2022.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (2, 'Goldman-10Q_March2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (2, 'Goldman-10Q_June2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (2, 'Goldman-10Q_Sep2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (2, 'Goldman-10Q_March2024.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (2, 'Goldman-10Q_June2024.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (2, 'Goldman-10Q_Sep2024.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (2, 'Goldman-10K_Annual_2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))

-- ############### JPMC DATA ########################

Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (3, 'JPMC-10K_Annual_2022.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (3, 'JPMC-10Q_March2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (3, 'JPMC-10Q_June2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (3, 'JPMC-10Q_Sep2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (3, 'JPMC-10Q_March2024.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (3, 'JPMC-10Q_June2024.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (3, 'JPMC_10Q_Sep2024.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (3, 'JPMC-10K_Annual_2023',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))


-- ############### WELLSFARGO DATA ########################
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (4, 'WellsFargo-10K_Annual_2022.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (4, 'WellsFargo-10Q_March2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (4, 'WellsFargo-10Q_June2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (4, 'WellsFargo-10Q_Sep2023.pdf',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (4, 'WellsFargo-10Q_March2024',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (4, 'WellsFargo-10Q_June2024',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (4, 'WellsFargo-10Q_Sep2024',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))
Insert into [CanadaOpenDataWH].[central1].[Files_Processing_Info] values (4, 'WellsFargo-10K_Annual_2023',GETDATE(),DATEADD(MINUTE, 60, GETDATE()))