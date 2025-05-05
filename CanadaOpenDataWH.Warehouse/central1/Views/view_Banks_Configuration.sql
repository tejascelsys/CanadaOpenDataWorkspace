-- Auto Generated (Do not modify) F69C7CA4E5B8CD3B13512288B82020FEDF2159547D59B9F9286C9A69B3EB5861


create view central1.view_Banks_Configuration as 
select c.*, v.numFiles, v.lastSubmmited, v.lastProcessed
from central1.Configuration c left join central1.view_Bank_Files v 
on c.BankID = v.BankID