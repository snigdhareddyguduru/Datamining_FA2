# Datamining_FA2

ATM Intelligence Demand Forecasting Dashboard

Introduction

Automated Teller Machines (ATMs) are one of the most important technologies used in the banking industry today. With the help of these machines, bank customers can withdraw cash, deposit funds, and carry out a variety of banking activities at their convenience without visiting the bank branch. However, one of the biggest challenges faced in the efficient use of these machines is the cash replenishment issue. Lack of cash in the machine results in the inability of the customer to withdraw cash, which affects the overall satisfaction level and reputation of the bank.

On the contrary, if the cash levels in the machine are too high, the bank may face security risks. With the increased availability of transaction data, banks can use data mining and analytics to efficiently forecast the demand for cash in the machine. By using the patterns in the transaction data, banks can efficiently categorize the machines according to their usage patterns.

The objective of this project is to use data mining techniques to analyze the data from ATM transactions and create an interactive dashboard to better visualize the data, identify unusual patterns, and create useful insights for decision-making.

Problem Description

Banks have numerous ATMs, sometimes as many as hundreds or even thousands, located at various locations such as urban centers, residential areas, and rural regions. Each ATM has varying levels of demand depending on various factors such as the density of the surrounding population, the number of businesses, the nature of the economy, the frequency of salaries, and sometimes events such as weekends, holidays, and special events.

The main issues that banks face include:

• Forecasting the amount of money each ATM needs
• Identifying the ATMs that frequently go out of money
• Identifying unusual peaks in withdrawal demand
• Identifying the behavioral trends of the users
• Scheduling the refill of the ATMs to save costs

Without proper data analysis, ATM management often relies on static refill schedules that do not adapt to changing demand. This may lead to either cash shortages or unnecessary excess cash storage.

This project attempts to address these challenges by analyzing ATM transaction data and building an interactive dashboard that helps identify patterns and support smarter cash distribution decisions.

Application Overview

The ATM Intelligence Demand Forecasting Dashboard is an interactive data analytics application built using Python and Streamlit. The application performs exploratory data analysis on ATM transaction data and applies machine learning techniques to identify clusters of ATMs with similar demand patterns and detect unusual withdrawal behavior.

<img width="1440" height="900" alt="Screenshot 2026-03-07 at 10 50 27 PM" src="https://github.com/user-attachments/assets/bd7d7586-a821-477a-8c47-2f4bd29ca102" />

<img width="1440" height="900" alt="Screenshot 2026-03-07 at 10 50 37 PM" src="https://github.com/user-attachments/assets/7568d970-a115-4272-ad47-059b26a72e57" />

<img width="1440" height="900" alt="Screenshot 2026-03-07 at 10 50 45 PM" src="https://github.com/user-attachments/assets/03587187-c3f7-4d71-b3ce-fe15c887e174" />

<img width="1440" height="900" alt="Screenshot 2026-03-07 at 10 51 01 PM" src="https://github.com/user-attachments/assets/8f3793c9-fafb-4252-bb63-51c311017c56" />

The dashboard will enable the user to interact with the data set, explore the visualizations, and gain insights into the demand patterns of the ATM. The dashboard will also have a basic recommendation system to calculate the amount of cash to be replenished in the ATM.

This application is created to mimic a real-life decision support tool for bank managers.

**Technologies Used**

This project uses the Python programming language along with various popular data science libraries:

**Python** – a programming language used for analysis and application development
**Streamlit** – used for creating the interactive dashboard
**Pandas** – used for data cleaning
**Matplotlib** – used for creating charts
**Seaborn** – used for creating statistical visualizations
**Scikit-learn** – used for clustering and anomaly detection algorithms

These tools help the application carry out data analysis and display the results in a user-friendly and interactive manner.

**Dataset Description**

The dataset used in this project consists of information related to the transaction carried out at the ATM. This information is used to analyze the withdrawal patterns and cash demand behavior.

**Key attributes in the dataset:**

ATM_ID – This attribute is used as a unique identifier.
Date – This attribute contains the date when the transaction occurred.
Day_of_Week – This attribute contains the day when the transaction occurred.
Location_Type – This attribute contains the type of location where the transaction occurred.
Total_Withdrawals – This attribute contains the total amount of cash withdrawn using the ATM.
Total_Deposits – This attribute contains the total amount deposited into the ATM.
Nearby_Competitor_ATMs – This attribute contains the number of competitor ATMs located nearby.
Previous_Day_Cash_Level – This attribute contains the cash available in the ATM the previous day.
Cash_Demand_Next_Day – This attribute contains the cash demand the following day.

The data in this dataset helps the project to understand the different factors affecting the demand at the ATM.

Features of the Application

The features of the application include various analytical tools that are meant to provide meaningful insights from the transactional data of the ATMs.

**Exploratory Data Analysis (EDA)**

The application provides exploratory data analysis, which helps in understanding various patterns of usage of ATMs. Various visualizations are included, such as withdrawal distribution, deposit distribution, weekday demand comparison, and correlation heatmap.

**ATM Clustering Analysis**

K-means clustering analysis is also included, which helps in clustering the ATMs based on their transactional behavior. Various clusters are formed based on the withdrawal patterns of the ATMs, including low-demand ATMs, medium-demand ATMs, and high-demand ATMs.

Anomaly Detection

Anomaly detection is carried out using Isolation Forest, which helps identify unusual withdrawal peaks. These peaks may arise due to various reasons, such as special events, holidays, salary days, and so forth. These peaks are often unpredictable, and their detection helps the bank prepare for a sudden surge in withdrawals.

ATM Refill Recommendation System

The application includes a simple recommendation system that helps estimate the amount of cash that should be added to an ATM based on average usage. This shows how data can be utilized to aid operational decisions.

ATM Demand Risk Indicator

The application categorizes ATMs based on their risk levels, such as low, medium, and high. These categorizations are based on their usage. High-risk ATMs may need more frequent replenishment to avoid cash depletion.

Automatic Insight Generation
The application is able to generate important insights based on the data. This is achieved by determining the day on which there is an average high amount of withdrawals. It also compares the difference in weekdays and weekends.

How the Application Works

The application is able to work by following a process that involves converting the data into important insights.
The first process is the loading of the ATM data using the Pandas library. This is followed by exploring the data using visualizations that help in determining the trends in the data.
After loading the data, the application performs a clustering process on the data. This is achieved by using the K-Means algorithm. This process is important in grouping the ATMs based on their demand.
After the clustering process, the application performs an anomaly process on the data. This process is achieved by using the Isolation Forest algorithm. This process is important in determining the spikes in the data.
The last process is the decision-support process. This process is important in determining the refill recommendations.

Reflections
This project illustrates the significance of data mining techniques in addressing real-world operational issues. By examining the data collected from the ATM transaction data, it is possible to establish patterns that might otherwise be impossible to establish.

From this project, one of the most important things learned is the significance of exploratory data analysis in establishing hidden trends in the data before using machine learning models. Visualization is also crucial in understanding complex data and effectively communicating the insights.

Another important thing learned from this project is the significance of using clustering and anomaly detection techniques. By using clustering, it is possible to group different ATMs depending on their characteristics, which might be important in managing the machines efficiently.

In addition, the project also illustrates the importance of integrating data science models into a user interface using the Streamlit library. Instead of using static data analysis, the project creates a dashboard where users can interact with the data.

Conclusion
In conclusion, this project has demonstrated the capabilities of data mining techniques in analyzing ATM transactional data, which can be beneficial in making better decisions regarding banking operations. By integrating exploratory data analysis, clustering, anomaly detection, and data visualization, the ATM Intelligence Dashboard has been developed as an effective solution for better understanding ATM demand behavior.

The project has also demonstrated the capabilities of data mining techniques in improving operational efficiency for banks by predicting ATM demand, identifying anomalies, and developing cash distribution strategies. However, it is also possible to extend this project further by implementing more sophisticated machine learning algorithms for predicting ATM demand.

In summary, this project has demonstrated the capabilities of data mining and data visualization techniques in transforming raw transactional data into more meaningful information for better decision-making in banking operations.
