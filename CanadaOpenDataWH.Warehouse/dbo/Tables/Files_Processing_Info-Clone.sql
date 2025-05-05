CREATE TABLE [dbo].[Files_Processing_Info-Clone] (

	[BankID] int NOT NULL, 
	[FileName] varchar(50) NOT NULL, 
	[FileSubmittedDateTime] datetime2(3) NULL, 
	[FileProcessedDateTime] datetime2(3) NULL
);