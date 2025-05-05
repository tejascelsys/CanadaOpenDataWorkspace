CREATE TABLE [central1].[Files_Processing_Info] (

	[BankID] int NOT NULL, 
	[FileName] varchar(50) NOT NULL, 
	[FileSubmittedDateTime] datetime2(3) NULL, 
	[FileProcessedDateTime] datetime2(3) NULL
);