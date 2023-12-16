# Cloud Azure Demand Forecasting
[![](https://img.shields.io/badge/Facebook-nguyenhoangtrung-blue)](https://www.facebook.com/nguyenhoangtrunghhh/)
[![](https://img.shields.io/badge/Gmail-nguyenhoangtrunghs%40gmail.com-red)](mailto:nguyenhoangtrunghs@gmail.com)

## Architecture
This architecture is based on the [Demand forecasting architecture](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/demand-forecasting) proposed by Microsoft. However, I've made some customizations to fit, such as replacing the use of Azure Data Factory for data processing (ETL) with Azure Databricks. This ensures the scalability of the architecture, as raw data needs more complex processing rather than just simple ETL operations.

The system encompasses all components of the big data processing cycle, including Data Source, Ingest, Process, and Enrich. These components will be elaborated on in detail in the subsequent sections

![image](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/d32c3757-65f7-4442-99af-5c678b7f8c4f)


## Main Workflow
Dataflow
The Microsoft AI Platform provides advanced analytics tools through Microsoft Azure - data ingestion, data storage, data processing, and advanced analytics components. These tools include all of the essential elements for building a demand-forecasting-for-energy solution.

This solution combines several Azure services to provide actionable predictions:

1. Event Hubs collects real-time consumption data.
2. Stream Analytics aggregates the streaming data and makes it available for visualization.
3. Azure Data Lake stores and transforms the consumption data.
4. Machine Learning implements and executes the forecasting model.
5. Power BI visualizes the real-time energy consumption and the forecast results.
   
### Workflow one
Within this workflow, we extract data from the Data Source, cleanse it, and then feed it into machine learning to generate a predictive model serving the forecasting process.

![image](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/410fb3ca-49e8-41d7-a445-60754fbf2abd)

### Workflow two
Once the predictive model is in place, we apply it to real-time data for forecasting purposes.

![image](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/54e5cfac-525f-4fc0-a3bd-22178965d404)

## Component

### Data Source
The stock market data of VCB is used for demonstrating this project. Data from 1/4/2021 to 11/17/2023 is utilized to perform Workflow 1 - Machine Learning model building. Meanwhile, data from 11/18/2023 until the current moment is used for real-time prediction in Workflow 2.

![image](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/c847db70-b17c-438e-8245-d23cc1a0b315)


### Ingest 
#### Stream Process/Realtime Process

![image](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/00c767c2-d94a-4462-90ea-6b5ee130be5a)

#### Batch Process

![image](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/1022d72e-1586-46fc-970a-d3d874c5944c)

### Process

![image](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/a6c37a2a-2272-49d4-bce0-36d66304e36d)

### Enrich

![image](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/bb66fab4-c27a-43e2-a706-98a165f346cb)



