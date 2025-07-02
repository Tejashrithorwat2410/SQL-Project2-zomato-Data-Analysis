# 📊 Project Report: Zomato Data Analysis using SQL Server

🧾 Project Title
Zomato Data Analysis using SQL Server

📌 Objective

To perform end-to-end analysis on a simulated Zomato-like food delivery dataset to generate business insights, identify customer behavior, restaurant performance, delivery efficiency, and support decision-making through data-driven conclusions.

🗂️ Dataset Overview

The project uses multiple relational tables:

customers – Customer details (ID, name, registration date)

restaurants_data – Restaurant details (ID, name, city, opening hours)

orders – Order details (ID, customer, restaurant, items, date, time, status, total)

deliveries – Delivery records (ID, order ID, rider, time, status)

riders – Rider details (ID, name, signup date)

🔧 Tech Stack

Database: SQL Server

Tools Used: SSMS (SQL Server Management Studio)

Languages: T-SQL


🔐 Data Preparation

Created relational database: Zomato_Data_Analysis

Defined primary and foreign key constraints to maintain referential integrity:

orders → customers, orders → restaurants_data

deliveries → orders, deliveries → riders

Checked for and removed null values across all tables.

📈 Key Business Questions & Insights

✅ 1. Top 5 Most Frequently Ordered Dishes (Last 1 Year)
Identified most popular items using order frequency, grouped by customers.

✅ 2. Best Time Slots for Orders
Found high-demand hours using 2-hour interval time buckets to optimize delivery/rider allocation.

✅ 3. Total Orders by Each City
Revealed top-performing cities, helpful for marketing & expansion.

✅ 4. Monthly Order Trends
Detected seasonality in orders using monthly breakdowns to plan promotions.

✅ 5. Total Revenue by Restaurant
Analyzed restaurant-wise contribution to total revenue.

✅ 6. Average Delivery Time by Rider
Evaluated rider efficiency to identify training needs or reward top performers.

✅ 7. Repeat Customers
Flagged loyal customers (more than 3 orders) to target with loyalty programs.

✅ 8. Order Status Distribution
Analyzed percentage of delivered vs cancelled orders to reduce churn.

✅ 9. Hourly Order Distribution
Found peak hours for platform engagement.

✅ 10. Most Profitable City
Identified cities with highest revenue contribution.

🧠 Outcomes

Delivered actionable insights on customer behavior, city-wise demand, and rider efficiency.

Provided a foundation for dashboard development in Power BI or Excel for stakeholders.

🌟 What I Learned

Writing optimized SQL queries for business logic.

Performing data cleaning and integrity validation.

Using real-world analytics techniques such as cohort analysis, time-series trends, and performance benchmarking.
