# Project for Operations research and logistics

## Boil1 - The issue of the intermediary
First project that include:
* route blocking: rigidly blocked one transport node of goods (any), regardless of its unit profit.
* no interface is required so the input data can be changed directly in the code
* no visualization of the results is required so: unit profits, optimal transports and listed: total cost, total revenue, broker profit are exported to .txt file

## Boil2 - Linear programming
Application design: optimization of flow in transportation networks based on linear programming
Model:
* Linear objective function 
* Linear boundary 
* Solution of the problem: application of the algorithm of the "Simplex" method.

The application takes: 
* Number of suppliers + supply 
* Number of customers + demand 
* Intermediary points 
* Connections between individual points 
* Flow costs on individual gaps (supply networks) 
* Flow limits (capacity)
