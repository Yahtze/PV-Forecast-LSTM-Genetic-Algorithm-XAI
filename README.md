# 🌞 Optimizing and Interpreting Forecasts of PV Power Output with LSTM and Genetic Algorithms Integrated with XAI

This repository contains the implementation of the research project titled:

**"Optimizing and Interpreting Forecasts of PV Power Output with LSTM and Genetic Algorithms Integrated with XAI"**
**Authors: Yathin Reddy Duvuru, Seshank Mahadev, Saranya P**

## 📌 Project Overview

The objective of this project is to forecast Global Horizontal Irradiance (GHI) values across multiple forecasting windows using deep learning techniques. The project involves:

- Constructing **benchmark models** for comparative evaluation.
- Implementing a **Genetic Algorithm (GA)** to optimize the hyperparameters of LSTM models.
- Minimizing the **Root Mean Squared Error (RMSE)** to improve prediction accuracy.
- Applying **Explainable AI (XAI)** methods to interpret and visualize the feature contributions for the LSTM predictions.

---

## 🧠 Key Features

- 📉 Accurate time series forecasting using LSTM networks.
- 🧬 Genetic Algorithm-based optimization for LSTM hyperparameters.
- 🪞 Model interpretability using XAI techniques.
- 📊 Comparative analysis against traditional benchmarks.

---

## 🗂️ Project Structure

- `src/data/`: Contains Python scripts responsible for fetching GHI data using the NSRDB API.
- `data/`: Holds the raw GHI data collected from the API, organized by year.
- `notebooks/`: Includes Jupyter notebooks for different stages of the workflow such as data preprocessing, exploratory data analysis (EDA), model training, and interpretability.
  - Within `notebooks/`, there are subdirectories for:
    - Benchmark models used for comparison.
    - LSTM hyperparameter optimization using the Genetic Algorithm.
    - XAI analysis for interpreting model outputs.

---

## ⚙️ How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/pv-forecast-ga-lstm-xai.git
   cd pv-forecast-ga-lstm-xai
   
2. Install dependencies

Create a virtual environment and install required packages:

pip install -r requirements.txt

3. (Optional) Fetch data from NSRDB

Run the script to collect GHI data using the NSRDB API:

python src/data/nsrdb_api_fetcher.py

4. Explore the notebooks

Open Jupyter Lab or Notebook to interact with the analysis and model development:

    jupyter lab

📈 Results

The GA-enhanced LSTM models demonstrated improved performance in terms of RMSE across different forecasting windows. Additionally, XAI methods revealed critical insights into the temporal and feature-based behavior of the models.

Results and visualizations are available in the corresponding notebooks.

🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

📬 Contact

For questions, feedback, or collaboration opportunities:

    Email: yathinreddy2004@gmail.com
