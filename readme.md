# 🌦️ Weather Forecast Prediction

## 📌 Overview
This project uses **Naïve Bayes Classification** to predict whether it will **rain tomorrow** based on weather features such as **humidity, temperature, wind speed, and pressure**.  
The model applies **Gaussian Naïve Bayes** since the features are continuous values.  

It uses **Python** with:
- **Pandas** → data handling  
- **Matplotlib / Seaborn** → visualization  
- **Scikit-learn** → model building and evaluation  

---

## 🚀 Usage
1. Open the `weather.ipynb` notebook in Jupyter Notebook or JupyterLab.  
2. Run the cells step by step to:
   - Load and explore the weather dataset  
   - Perform Exploratory Data Analysis (EDA)  
   - Train a **Naïve Bayes classifier**  
   - Evaluate accuracy and make predictions  

---

## 📊 Results
Here are some insights from the analysis:

### 🌡️ Feature Distributions
- Histograms showing the spread of **humidity, temperature, wind_speed, and pressure**  

### 🤖 Model Accuracy
- The Naïve Bayes model was trained and tested on the dataset using an 70-30 split  
- The model achieved an **accuracy score** (value will appear in notebook output)  

### 🌦️ Prediction Example
For input conditions:  
- **humidity = 75**  
- **temperature = 28**  
- **wind_speed = 12**  
- **pressure = 1010**  

👉 The model predicts whether it will **rain tomorrow** (`0 = No`, `1 = Yes`)  

---

## ✅ Conclusion
- **Humidity** and **pressure** were found to be the most influential features in predicting rainfall.  
- The **Naïve Bayes classifier** provides a simple yet effective approach for weather forecasting with tabular data.  
- While accuracy is moderate, the model can serve as a baseline for comparison with more advanced classifiers like Decision Trees, Random Forests, or Gradient Boosting.  
- Future improvements can include:
  - Adding more weather-related features (e.g., cloud cover, dew point, seasonality)  
  - Using a larger dataset across multiple regions and seasons  

---

💡 *Feel free to fork this repo and test the model on your own weather dataset!*  
