# Cloud Azure Demand Forecasting
[![](https://img.shields.io/badge/Facebook-nguyenhoangtrung-blue)](https://www.facebook.com/nguyenhoangtrunghhh/)
[![](https://img.shields.io/badge/Gmail-nguyenhoangtrunghs%40gmail.com-red)](mailto:nguyenhoangtrunghs@gmail.com)


## Documentation

* [Architecture](#architecture)
* [Main-Workflowms](#main-workflows)
	- [Workflow one](#workflow-one)
	- [Workflow two](#workflow-two)
* [Component](#component)
	- [Data-Source](#data-source)
	- [Ingest](#ingest)
 - 	- [Process](#process)
	- [Enrich](#enrich)
 * [Achievement](#achievement)




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
Due to real-time stock prices fluctuating daily, using it for real-time representation poses some difficulties. To overcome this, our team utilized Python to simulate real-time data. Every minute, a data line is sent to the event hub. Upon receiving this data from Python, the event hub channels it into Stream Analytics. At the interface, Stream Analytics performs basic ETL on the data and applies a machine learning model trained during the enrichment process. Finally, it sends the data line with the newly generated value column from the machine learning process to Power BI for data visualization.

![image](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/00c767c2-d94a-4462-90ea-6b5ee130be5a)

#### Batch Process
Raw data sourced from external websites, specifically from GitHub, is processed by Azure Data Factory. Within Data Factory, it establishes linked services with the raw data source. It then proceeds to create triggers for scheduling data processing. Finally, the processed data is stored in Data Lake Storage Gen 2.

![image](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/1022d72e-1586-46fc-970a-d3d874c5944c)

### Process
After the ingest process, for raw data to become useful, it needs to undergo cleaning and standardization. Databricks plays a crucial role in executing this. Within the Databricks platform, it will connect to the raw data source, specifically, the Data Lake Storage Gen 2. Databricks will standardize the raw data, making it usable for various purposes, such as visualization or storage for use in other processes like machine learning.

![image](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/a6c37a2a-2272-49d4-bce0-36d66304e36d)

### Enrich
Finally, once the data has been cleaned, Azure Machine Learning will utilize it to undergo the machine learning process. Azure Machine Learning offers three different methods for machine learning: Notebook, Automated ML, and Designer. However, for simplicity, we can use Automated ML. Here, all we need to do is input the dataset we want to train, and Azure Machine Learning will train that data across all available models, then output the best-performing model. From this best model, we can export an endpoint for use in other Azure services such as Stream Analytics.
![image](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/bb66fab4-c27a-43e2-a706-98a165f346cb)

## Achievement  

![Realtime-_online-video-cutter com_](https://github.com/NguyenHoangTrungII/cloud-demand-forecasting/assets/101980170/2074dbe3-0b12-4f04-835c-7a07ae186a1d)
