# 01. Data Warehouse, Schemas and OLAP

## Aim
Create a conceptual data warehouse/data mart and understand Star, Snowflake and Fact Constellation schemas. Perform Slice, Dice, Roll-up, Drill-down and Pivot.

## Schema
**Star:** one fact table directly connected to dimension tables.  
**Snowflake:** dimension tables are normalized into hierarchy tables.  
**Fact Constellation:** multiple fact tables share common dimensions.

## OLAP
- Slice: Product = Laptop.
- Dice: Product in {Laptop, Phone} and Region = South.
- Roll-up: City → State.
- Drill-down: Year → Quarter → Month.
- Pivot: rotate dimensions to obtain another view.

## Result
The schemas and OLAP operations are understood using a sample sales cube.