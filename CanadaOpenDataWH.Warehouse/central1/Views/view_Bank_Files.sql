-- Auto Generated (Do not modify) B4B096F8DF7EDB44A94F4BDE1E36CA77D84217EB8F487EEC43E0A7A4B084921D


create view central1.view_Bank_Files as 
select f.BankID, count(*) numFiles, max(FileSubmittedDateTime) lastSubmmited, max(FileProcessedDateTime) lastProcessed  from central1.Files_Processing_Info f
GROUP by BankID