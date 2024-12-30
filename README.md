# ** GraphAI**

[![Python Version](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Streamlit](https://img.shields.io/badge/Streamlit-v1.0.0-orange)](https://streamlit.io/)


---

## **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Querying the Database](#querying-the-database)
- [License](#license)

---

## **Overview**

The **Interactive Vehicle Distribution Plotter** is a web application built using **Streamlit**, **LangChain**, and **Plotly**. It allows users to generate interactive plots based on natural language descriptions of data. The app takes user input, processes it with a language model, and automatically generates a Plotly chart visualizing the dataset, which is loaded from a CSV file.

The app is designed to assist in visualizing the distribution of vehicle data, with user-friendly input and robust error handling.


---

## **Features**
- **Natural Language Processing**: Converts user input into Python code for generating plots using Plotly.
- **Interactive Plotting**: Generates interactive charts based on dataset columns.
- **Streamlit Interface**: Easy-to-use web UI for quick interaction.
- **Error Handling**: Alerts users to any issues with input or code execution.
- **Model-Based Code Generation**: Uses a pre-trained language model to create code for the desired plot.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/interactive-vehicle-distribution-plotter.git
cd interactive-vehicle-distribution-plotter
```

### **2. Create and Activate a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```



## **Usage**

### **1. Run the script**
```bash
streamlit run app.py
```
### **2. Input Description**
```bash
"Plot the graph corresponding to the natural language query."
```
### **3. View the Generated Plot**
```bash
"Once you click on the Generate Plot button, the app will process the description and generate a corresponding plot based on the dataset (Damage.csv)."
```

## **Configuration**

### **1. Configure the Dataset**
```bash
"Show all employees earning above $50,000."
```

## **License**

This project is licensed under the **GNU General Public License (GPL)**. See the [LICENSE](LICENSE) file for more details.




