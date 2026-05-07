### **Supply Chain Intelligence Platform**



#### End-to-End Data Warehouse \& Business Intelligence System

A business-focused analytics project built to monitor supply chain performance, identify operational risks, and support strategic decision-making across suppliers, logistics, warehouses, and product categories.

This project simulates how a real analytics team would design an end-to-end reporting system—from raw operational data to executive dashboards and actionable business recommendations.



#### Project Overview

Modern supply chains generate large volumes of operational data, but data alone does not improve decisions.  
The goal of this project was to build a centralized analytics platform capable of answering business-critical questions such as:

* Are shipments being delivered on time?
* Which suppliers are creating operational risk?
* Where are logistics costs increasing?
* Which warehouses handle the highest workload?
* Which product categories need operational attention?

To answer these questions, I built a complete analytics workflow covering data generation, ETL, warehouse design, SQL analysis, and interactive business dashboards.



#### Business Problem

Supply chain teams often struggle with:

* Delivery delays
* Supplier dependency
* High freight costs
* Uneven warehouse workload
* Lack of centralized operational visibility

This project addresses these challenges by converting raw shipment data into decision-ready insights.

#### 

#### Tech Stack

* Python
* PostgreSQL
* SQL
* Power BI
* Git

**Libraries used:**

* Pandas
* NumPy
* psycopg2



#### Architecture


Raw Data Generation
        ↓
Python ETL Pipeline
        ↓
PostgreSQL Data Warehouse
        ↓
SQL Business Analysis
        ↓
Power BI Executive Dashboards




#### Dataset

Operational dataset generated using Python.

#### Data Volume

* 150,000+ shipment records
* 50 suppliers
* 10 warehouses
* 100+ products
* Multi-category shipment transactions



#### Data Model

Star schema design:

#### Fact Table

* fact\_shipments

#### Dimension Tables

* dim\_supplier
* dim\_product
* dim\_warehouse
* dim\_date

#### 

#### Dashboard Pages



#### 1\. Executive Operations Dashboard

Tracks:

* OTIF %
* Delay Rate
* Freight Cost
* Regional Delivery Risk

Business focus:

Operational health and delivery performance.



#### 2\. Supplier Intelligence Dashboard

Tracks:

* High-risk suppliers
* Lead time analysis
* Supplier quality distribution
* Shipment concentration

Business focus:

Supplier risk and procurement performance.



#### 3\. Warehouse \& Inventory Intelligence

Tracks:

* Shipment distribution by warehouse
* Freight efficiency
* Product movement
* Inventory risk by category

Business focus:

Operational efficiency and workload balancing.

#### 

#### 4\. Strategic Insights \& Recommendations

Provides:

* Key operational findings
* Risk alerts
* Business recommendations

Business focus:

Executive decision support.



#### Key Business Insights

Some insights identified during analysis:

* OTIF performance remained below expected operational targets.
* A small group of suppliers contributed disproportionately to shipment delays.
* High-volume suppliers also showed longer lead times.
* Freight costs were concentrated in specific product categories.
* Warehouse workload distribution was uneven across facilities.



#### Recommendations

Based on the analysis:

* Introduce supplier performance scorecards.
* Renegotiate SLAs with high-risk suppliers.
* Rebalance warehouse allocation.
* Optimize freight planning for high-cost categories.
* Maintain safety stock for delay-prone inventory.



#### Project Highlights

* Built an end-to-end analytics pipeline from raw data to executive reporting.
* Designed a star-schema warehouse for business analytics.
* Developed advanced SQL queries for operational diagnostics.
* Created a 4-page Power BI command center for executive reporting.
* Focused on business impact, not just visualization.



#### Repository Structure


supply-chain-intelligence-platform/
│
├── data/
├── pipeline/
├── sql/
├── dashboard/
├── README.md



#### Author

###### **Shaheer Mustafa**

Aspiring Data Analyst focused on building business-driven analytics solutions using SQL, Python, PostgreSQL, and Power BI.

