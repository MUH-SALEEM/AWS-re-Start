# Database fact finding exercise

## Questions

**1) What is the difference between a relational and a non-relational database?**

A relational database is structured, meaning the data is organized in tables. Many times, the data within these tables have relationships with one another, or dependencies. 
Some of the most common relational databases
* MySQL
* IBM Db2
* Snowflake
* Amazon Aurora
* PostgreSQL
* Microsoft SQL Server


A non relational database is document-oriented, meaning, data in a document-based format, with each document representing a record representing data in  whatever manner is best suited to the type of data being stored. Non-relational databases are designed to contain unstructured data.
Some of the most common relational databases
* MongoDB
* IBM Cloundant
* Amazon DynamoDB
* Apache Cassandra


**2) What are indexes?**

An index is a database structure that you can use to improve the performance of database activity. A database table can have one or more indexes associated with it. An index is defined by a field expression that you specify when you create the index. 
a single field name, like EMP_ID.


**3) What are primary keys and secondary keys?**

##### Primary Key
The attribute that uniquely identifies a row or record in a relation is known as primary key -like page number of a book

##### Secondary Key
A field or combination of fields that is basis for retrieval is known as secondary key (mainly used for finding details from large data)
like an index page of a book

**4) What are inner joins and outer joins?**

##### Inner Join
An Inner Join returns only the rows that have matching values in both the tables (we are considering here the join is done between the two tables).

##### Outer Join
The Outer Join includes the matching rows as well as some of the non-matching rows between the two tables. An Outer join basically differs from the Inner join in how it handles the false match condition.
There are 3 types of Outer Join:
Left Outer Join
Right Outer Join
Full Outer Join


**5) What is the difference between DROP TABLE and TRUNCATE TABLE?**

##### TRUNCATE TABLE
Removes all rows from a table without logging the individual row deletions. TRUNCATE TABLE is similar to the DELETE statement with no WHERE clause; however, TRUNCATE TABLE is faster and uses fewer system and transaction log resources.

##### DROP TABLE
Removes one or more table definitions and all data, indexes, triggers, constraints, and permission specifications for those tables.


**6) What are the different data types in SQL?**

In SQL, there are several data types that can be used to represent different types of data. 

##### Some common data types include:

* Integer: Used to store whole numbers without decimal places.
* Float/Real: Used to store decimal numbers.
* Char/Character: Used to store fixed-length character strings.
* Varchar/Varchar2: Used to store variable-length character strings.
* Date/Time: Used to store dates and times.
* Boolean: Used to store true/false values.
* Blob/Binary Large Object: Used to store large binary objects such as images, audio, or video files.
* Decimal/Numeric: Used to store decimal numbers with fixed precision and scale.
* Text: Used to store large amounts of text data.
* XML: Used to store XML documents.

These data types can be used in SQL to define the structure of tables, columns, and variables, and to ensure that the data stored in the database is consistent and accurate.

**7) Explain the WHERE and HAVING clauses.**

##### WHERE Clause
The WHERE clause is used to fetch the data which specify the given condition. It is used to filter records and select only necessary records. It is used with SELECT, UPDATE, DELETE, etc. query. The SQL also implements and, or, and not in the WHERE clause which is known as the boolean condition.
Example:
SELECT COUNT(*)
FROM employee;
Result:
COUNT(*)200 

##### HAVING Clause

The HAVING clause is generally used along with the GROUP BY clause. This clause is used in the column operation and is applied to aggregate rows or groups according to given conditions.
Example: Let’s say you wanted to find the SUM of salaries per department.
SELECT department_id,
SUM(salary) AS total_sal
FROM employee
GROUP BY department_id
ORDER BY department_id; The difference between WHERE and HAVING clauses are:
The WHERE clause is used to filter rows before the grouping is performed.
The HAVING clause is used to filter rows after the grouping is performed. It often includes the result of aggregate functions and is used with GROUP BY