# sql-challenge
This challenge was surprisingly difficult.  I went in to it thinking it should be the easiest HW to date, but I had the hardest time with it for possibly the silliest of reasons.  I had a lockout of my GCP database instance that required many hours of phone support and eventually a loss of the database. #restart.


folders:
EmployeeSQL - original csv's to be imported in to the DB
query results - csv's exported from DB query
sql_queries - query code exported by pgAdmin
xx_misc_xx - **see below**


You will see I have afolder named xx_misc_xx.  This is a dumping ground for my speedbumps along the way.  Our class video that showed how to import csv's to pgAdmin was corrupt.  As an attempt to make up for that, my instructor added a suplimantal video, but got fancier and added the csv the the DB directly from python.  It was very cool, but unfortunately it seems to have allowed the DB to analyze the tablea and assign types.  for the most part this was fine, but it didnt properly identify the date columns as such and pgAdmin would allow for the proper type change to occure.  in figuring this all out, I went down a rabbit hole thinking that the format of the date needed to be changed in the original csv, so I created code to change the dates from mm/dd/yyyy to mm-dd-yyyy.  This was cool and educational but did nothing to fix my issue.  I ended up figuring out how to manually import the csv's with the proper data types.  I suppose i'm better for having done it.

