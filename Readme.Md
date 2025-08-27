# Semiconductor Wafer Quality Prediction

## Problem Statement
**Objective:** Develop a machine learning model to predict the quality of semiconductor wafers as either "Good" or "Bad" based on sensor readings collected during the fabrication process.

**Details:**  
Inputs (Features): The dataset consists of 590 sensor readings (Sensor-1, Sensor-2, …, Sensor-590) for each wafer. These readings capture various environmental and process parameters during the wafer's fabrication.

**Output (Target):**  
The target variable is labeled as "Good/Bad," where `1` indicates a "Good" wafer, and `-1` indicates a "Bad" wafer.

**Goal:**  
The goal is to build a classification model that can accurately predict whether a wafer is good or bad based on the sensor readings. This prediction can help in early detection of defective wafers, improving yield and reducing waste in the semiconductor manufacturing process.

**Machine Learning Task:**  
- Type: Supervised Learning (Classification)  
- Model Type: Binary Classification Model

---

## Challenges in Wafer Inspection

### 1. Post-Production Inspection
Manual or Automated Testing: Without real-time prediction, you would likely need to rely on manual or automated inspection and testing of wafers after the entire fabrication process is completed. This means that you wouldn't know if a wafer is faulty until the end, after significant resources and time have already been invested.

**Delays in Detection:** Faults would only be detected after the wafer has passed through all stages of production. This could lead to a high amount of wasted resources if a large batch of wafers is found to be defective late in the process.

### 2. Batch Testing
**Stopping Production:** In some cases, if a fault is suspected, you might need to halt production to perform batch testing. This could involve removing a sample of wafers from the production line for detailed inspection and testing. If a fault is found in the sample, you might then have to inspect the entire batch.

**Production Downtime:** Stopping production for testing can lead to significant downtime, reducing overall efficiency and potentially causing delays in product delivery.
















setup.py is a module used to build and distribute python package 
Inside it you can get :
    package 
    name
    dependencies
    version

package -> when there is  a multiple python  file and including __init__.py inside a folder then we can say that it is an package   