# PV Power Forecasting with LSTM, Genetic Algorithm Optimization, and XAI

## Overview
This repository contains the code and notebooks for forecasting photovoltaic (PV) power-related solar irradiance signals (primarily GHI) using LSTM models, optimizing model setup with a Genetic Algorithm (GA), and interpreting model behavior with Explainable AI (XAI).

The workflow compares baseline forecasting approaches against GA-tuned LSTM variants across multiple forecast horizons (10, 20, 40, 60, and 120 minutes ahead). This codebase extends ideas from earlier LSTM+XAI work into a GA-driven hyperparameter optimization pipeline.

## Motivation
Short-term PV forecasting is operationally important for grid scheduling, storage control, and renewable integration. Standard deep learning models can produce strong forecasts, but they are sensitive to configuration choices and are often treated as black boxes.

This project addresses both issues by:
- using GA to search for better-performing LSTM configurations, and
- using XAI analysis to explain which input factors most influence forecasts.

## Why Genetic Algorithm (GA) for Hyperparameter Optimization
GA is used here as a population-based search strategy for LSTM hyperparameters, rather than relying on manual tuning alone. Candidate model configurations are encoded, evaluated on forecasting error (RMSE), and iteratively improved through selection, crossover, and mutation.

In practice, this helps explore a broader hyperparameter space (for example sequence length, model size, and training settings) and can find stronger configurations than ad-hoc trial-and-error.

## Related Prior Publication
The following published work is a precursor to this project’s direction:

Duvuru, Y.R., Mahadev, S., Saranya, P. (2026). *Photovoltaic Cell Power Forecasting Using LSTM with XAI Integration*. In: Senjyu, T., So-In, C., Joshi, A. (eds) **Smart Trends in Computing and Communications**. SmartCom 2025. Lecture Notes in Networks and Systems, vol 1463. Springer, Singapore. https://doi.org/10.1007/978-981-96-7514-2_22

Precursor implementation repository:
https://github.com/Yahtze/Photovoltaic-Cell-Power-Forecasting-Using-LSTM-With-XAI-Integration

Note: the paper specifically corresponding to this repository has not yet been published.

## Repository Structure
- `data/raw/` - NSRDB CSV files used in experiments (`solar_data_2018.csv` ... `solar_data_2023.csv`)
- `src/data/nsrdb_data.py` - script for downloading NSRDB data via NREL API
- `notebooks/data_preprocessing.ipynb` - preprocessing pipeline
- `notebooks/exploratory_data_analysis.ipynb` - exploratory data analysis
- `notebooks/benchmarks/` - baseline model notebooks by forecast horizon
- `notebooks/LSTM_Feature_Search/` - LSTM feature/hyperparameter search notebooks
- `notebooks/GA_XAI/` - GA-optimized LSTM + XAI notebooks by forecast horizon

## Quick Start
1. Clone the repository:
   ```bash
   git clone <your-fork-or-repo-url>
   cd PV-Forecast-LSTM-Genetic-Algorithm-XAI
   ```
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Launch Jupyter:
   ```bash
   jupyter lab
   ```
5. Run notebooks in this recommended order:
   - `notebooks/data_preprocessing.ipynb`
   - `notebooks/exploratory_data_analysis.ipynb`
   - `notebooks/benchmarks/*`
   - `notebooks/LSTM_Feature_Search/*`
   - `notebooks/GA_XAI/*`

## Using Your Own Data
You can experiment with your own location/time-series data in two ways.

### Option A: Download new NSRDB data with the included script
1. Create a `.env` file in the project root:
   ```env
   API_KEY=your_nrel_api_key
   EMAIL=your_email
   ```
2. Edit `src/data/nsrdb_data.py`:
   - `LOCATION` (WKT point, longitude latitude)
   - `START_YEAR`, `END_YEAR`
   - `INTERVAL` (sampling interval)
3. Run:
   ```bash
   python src/data/nsrdb_data.py
   ```
4. Generated files are saved to `data/raw/`.

### Option B: Bring your own CSV files
If you use external data, align it to the schema expected by preprocessing/training notebooks. The provided NSRDB files include:
- two metadata/header rows at the top,
- timestamp fields (`Year`, `Month`, `Day`, `Hour`, `Minute`),
- forecasting features (for example `Temperature`, `DHI`, `DNI`, `GHI`, `Relative Humidity`, `Solar Zenith Angle`, `Wind Speed`, etc.).

Practical tips:
- keep column names consistent with notebook expectations,
- maintain a regular sampling interval,
- place files in `data/raw/` and update file paths inside notebooks if needed.

## Notes
- This project is notebook-first and designed for experimentation and comparative analysis.
- Dependencies are pinned to older versions because SHAP support in this workflow is tied to TensorFlow 1.14, so the environment stays on TensorFlow 1.14 for compatibility.
- Running inside a dedicated virtual environment is strongly recommended.

## Contact
For questions or collaboration:
- Email: `yathinreddy2004@gmail.com`
