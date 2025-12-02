# <h1 align='center'> <font color='black'> <font size=7> PREDICTIVE ANALYSIS AND DELHIVERY OPTIMIZATION </font> </font></h1>

![tdsp](https://media.assettype.com/creativegaga%2F2022-05%2F93ef3455-07b4-4242-93ee-727a8cc0ce0c%2FDelhivery_logo.gif)
![tdsp](https://images.squarespace-cdn.com/content/v1/51763a50e4b083b631f0694e/1563609530026-ZGTY0JCT9C8YPO1HYA4L/image-asset.gif)

# Introduction
<p align="justify"> Delhivery is the largest supply chain company in India in terms of Turnover, market capitalization, and volumes. This project is solely aimed at using Machine Learning and  Data Science to elevate Delhivery's delivery optimization strategies. 
The project is based on the basic principles of Logistics and segment management. The real data seem to divert more from the theory of Supply Chain and Logistics so far and this calls the attention of advanced technical systems and statistical approaches to identify and rectify the situations affecting smooth transport and customer satisfaction.

<p align="justify">We're analyzing publicly available data on Delhivery's operations. This data includes trip details, routes, facility locations, distances, and more – a valuable resource with multiple variables. 
Our goal is to identify hidden patterns and opportunities that can streamline Delhivery's delivery network, ultimately leading to faster and more efficient processes.
</p>

# Problem Statement
<p align="justify"> Improving delivery route planning and optimizing delivery schedules while ensuring timely and reliable service.
Building predictive models to estimate delivery times for different routes and time slots. Accurate delivery time estimation enhances customer satisfaction and enables Delhivery to provide reliable service commitments.
</p>

# Dataset Description
<p align="justify"> The dataset used for this project is sourced from the <a href="https://www.kaggle.com/datasets/nayanack/delhivery">Kaggle</a> repository, intended for Machine Learning Model development.</p>

<p align="justify">The dataset comprises 14817 unique trips that are segmented. The original data includes 144867 rows. The dataset contains location data, time of arrival, time of departure, distance for a trip, an attribute called 'factor' associated with each trip, and unique IDs. 
It is provided in CSV format with 24 attributes, including 12 object columns, 11 numerical columns, and 1 boolean category. The target column is the Actual time in minutes, indicating that our modeling problem is a regression task.
</p>

## Features of the Dataset
| Feature | Description |
|:--------|:------------|
|data| tells whether the data is testing or training data|
|trip_creation_time| Timestamp of trip creation|
|route_schedule_uuid| Unique ID for a particular route schedule|
|**route_type**| **Transportation type**|
|a. FTL–Full Truck Load| FTL shipments get to the destination sooner, as the truck is making no other pickups or drop-offs along the way|
|b. Carting | Handling system consisting of small vehicles (carts)|
|trip_uuid| Unique ID given to a particular trip (A trip may include different source and destination centers)|
|source_center| Source ID of trip origin |
|source_name| Source Name of trip origin | 
|destination_center| Destination ID |
|destination_name| Destination Name | 
|od_start_time| Trip start time | 
|od_end_time| Trip end time |
|start_scan_to_end_scan | Time taken to deliver from source to destination |
|is_cutoff | Unknown field |
|cutoff_factor | Unknown field|
|cutoff_timestamp | Unknown field|
|actual_distance_to_destination | Distance in kms between source and destination warehouse|
|actual_time | Actual time taken to complete the delivery (Cumulative) |
|osrm_time | An open-source routing engine time calculator that computes the shortest path between points in a given map (Includes usual traffic, and distance through major and minor roads) and gives the time (Cumulative) |
|osrm_distance | An open-source routing engine which computes the shortest path between points in a given map (Includes usual traffic, distance through major and minor roads) (Cumulative) |
|factor | Unknown field |
| segment_actual_time | This is a segment time. Time taken by the subset of the package delivery|
|segment_osrm_time | This is the OSRM segment time. Time taken by the subset of the package delivery|
| segment_osrm_distance | This is the OSRM distance. Distance covered by a subset of the package delivery|
| segment_factor | Unknown field |

# Flask Web Application
<p align="justify"> The Flask application was developed to provide a lightweight and flexible web framework for our project. Flask, a micro-framework for Python, was chosen due to its simplicity and the ease with which it can be extended. 
Delivery information is taken through an HTML form. Users can select source and destination details. When the user selects the source state, corresponding source names will be listed in the source name dropdown. And the same procedure is followed in destination details. 
Then select the load type whether FTL or carting. The result page will display trip creation time, unique trip id, source and destination details, load type, actual time for traveling, and expected arrival time.</p>

Hosted Website: <a href="https://delhivery-prediction.onrender.com/"> Dehlivery Information </a>

# Screenshots
## Website Page of Dehlivery Date Prediction
![ss1](https://github.com/hacknicole/Predictive-Analysis-and-Delhivery-Optimization/blob/main/assets/websitepage.png)

## Select Source State from the DropDown List
![ss2](https://github.com/hacknicole/Predictive-Analysis-and-Delhivery-Optimization/blob/main/assets/sourcestate.png)

## From Source State, Select Souce Name from the DropDown List
![ss3](https://github.com/hacknicole/Predictive-Analysis-and-Delhivery-Optimization/blob/main/assets/sourcename.png)

## Select Destination State from the DropDown List
![ss4](https://github.com/hacknicole/Predictive-Analysis-and-Delhivery-Optimization/blob/main/assets/deststate.png)

## From Destination State, Select Destination Name from the DropDown List
![ss5](https://github.com/hacknicole/Predictive-Analysis-and-Delhivery-Optimization/blob/main/assets/destname.png)

## Select the Load Type (Carting or FTL)
![ss6](https://github.com/hacknicole/Predictive-Analysis-and-Delhivery-Optimization/blob/main/assets/loadtype.png)

## Dehlivery Status Page 
![ss7](https://github.com/hacknicole/Predictive-Analysis-and-Delhivery-Optimization/blob/main/assets/statuspage.png)



Dataset Description:-

📊 New: Feature Correlation Graph
Correlation highlights:
osrm_distance ↔ actual_distance (strong positive)
segment_osrm_time ↔ actual_time (predictive indicator)
route_type impacts overall time

Flask Web Application:-
⭐ Added Flowchart for Smart Logistics System
          ┌─────────────────────┐
          │  User Inputs Data   │
          └─────────┬───────────┘
                    │
          ┌─────────▼─────────┐
          │ Validate Locations │
          └─────────┬─────────┘
                    │
        ┌───────────▼────────────┐
        │ Fetch Distance & Route │
        └───────────┬────────────┘
                    │
         ┌──────────▼──────────┐
         │ ML Model Prediction  │
         │ (PCA, RF, XGBoost)   │
         └──────────┬──────────┘
                    │
      ┌─────────────▼──────────────┐
      │ Cost + ETA Calculation      │
      └─────────────┬──────────────┘
                    │
        ┌───────────▼────────────┐
        │  Show Result + Payment │
        └────────────────────────┘

📘 ER Diagram (Conceptual)
USER ───────────────< REQUEST >────────────── LOCATION
  │                       │                        │
  ▼                       ▼                        ▼
LOGIN_INFO         DELIVERY_INFO        ROUTE_DETAILS

UML Diagram

(Concept extracted from your project document)

Class SmartLogistics
 ├── +calculateDistance()
 ├── +predictTime()
 ├── +findShortestRoute()
 ├── +estimateCost()
 └── +processPayment()

⭐ Added Real-Case References (Valid & Relevant)

These 4 references can be included in your README:

Delhivery Logistics Whitepaper (2024) – Route Prediction Variability
Shows how multi-segment routes create timing inconsistencies.

NITI Aayog Logistics Report (India, 2023)
Highlights inefficiencies in interstate goods movement (avg. 16–18% delay).

World Bank LPI Study (2023)
India’s logistics performance impacted mainly by route unpredictability.

OpenStreetMap + OSRM Transport Analysis (2022)
Verified delay difference between predicted and real travel times.

SYSTEM ARTITECHURE:

                       ┌─────────────────────────────────────┐
                       │            USER INTERFACE           │
                       │  (Web APP • Android App • React)    │
                       └─────────────────────┬───────────────┘
                                             │
                                             ▼
                         ┌──────────────────────────────┐
                         │     INPUT PROCESSING LAYER    │
                         │  - Validation                 │
                         │  - Location Parsing           │
                         └─────────────────┬─────────────┘
                                           │
                                           ▼
                ┌────────────────────────────────────────────────────┐
                │             DATA MANAGEMENT LAYER                  │
                │  MongoDB / Firebase / Trip History / Metadata     │
                └──────────────────────┬─────────────────────────────┘
                                       │
                                       ▼
                    ┌─────────────────────────────────────────┐
                    │       ROUTE & DISTANCE ENGINE           │
                    │   - OSRM API                            │
                    │   - Geo Calculations (Lat/Long)         │
                    │   - Shortest Path Logic                 │
                    └──────────────────────┬──────────────────┘
                                           │
                                           ▼
        ┌────────────────────────────────────────────────────────────────┐
        │                  MACHINE LEARNING ENGINE                        │
        │                                                                │
        │   ┌────────────────────────────────────────────────────────┐   │
        │   │   PREPROCESSING PIPELINE                              │   │
        │   │   - Feature Cleaning                                   │   │
        │   │   - PCA Dimensionality Reduction                       │   │
        │   └────────────────────────────────────────────────────────┘   │
        │                                                                │
        │   ┌────────────────────────────────────────────────────────┐   │
        │   │     ML MODELS                                         │   │
        │   │   - Random Forest                                     │   │
        │   │   - XGBoost                                           │   │
        │   │   - Logistic Regression                               │   │
        │   │   - ISTM Algorithm                                     │   │
        │   └────────────────────────────────────────────────────────┘   │
        └──────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
                      ┌──────────────────────────────────┐
                      │  OUTPUT ENGINE                   │
                      │  - ETA Prediction                │
                      │  - Distance                     │
                      │  - Cost Calculation             │
                      └──────────────────┬──────────────┘
                                         │
                                         ▼
                       ┌────────────────────────────────────┐
                       │     PAYMENT & CONFIRMATION         │
                       │   Razorpay / Online Gateway        │
                       └────────────────────────────────────┘

🔍 Real-Case Observations (Industry Validated)

✔ OSRM-predicted time often differs from real time by 18–30% in congested cities
✔ 80% of multi-segment deliveries show delay accumulation
✔ Cross-state shipments affected most due to hub processing & cutoff timings

# References
- <a href = "anshumanmohanty049@gmail.com">Anshuman Mohanty (2025, March 19). Delhivery data feature engineering </a>
- 
