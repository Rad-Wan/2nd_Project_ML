# Tanzania Tourism Project - Installation Guide

This package contains all the files needed to run the Tanzania Tourism Expense Calculator and explore the data analysis project.

## Contents

1. **Interactive Expense Calculator**
   - `app.py` - The main Streamlit application
   - `README.md` - Instructions for using the calculator

2. **Data Analysis and Machine Learning**
   - `tanzania_tourism_prediction.ipynb` - Jupyter notebook with complete analysis
   - `tanzania_tourism_prediction_reorganized.py` - Python script with organized code
   - `data/` - Directory containing the dataset files

3. **Results and Presentations**
   - PowerPoint presentations
   - Reports and visualizations

## Installation Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Install Required Libraries

Open a terminal or command prompt and run:

```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn jupyter
```

### Step 2: Run the Expense Calculator

Navigate to the directory containing this package and run:

```bash
streamlit run app.py
```

This will start the application and automatically open it in your default web browser. If it doesn't open automatically, you can access it at http://localhost:8501

### Step 3: Explore the Jupyter Notebook

To open and run the Jupyter notebook:

```bash
jupyter notebook tanzania_tourism_prediction.ipynb
```

Or if you prefer to use Jupyter Lab:

```bash
jupyter lab tanzania_tourism_prediction.ipynb
```

## Troubleshooting

If you encounter any issues:

1. **Library Installation Problems**
   - Try installing libraries one by one
   - Check for error messages and search for solutions online
   - Ensure you have the correct Python version

2. **Application Won't Start**
   - Verify all files are in the correct locations
   - Check that you're running commands from the correct directory
   - Ensure all required libraries are installed

3. **Jupyter Notebook Issues**
   - Make sure Jupyter is installed correctly
   - Try running the Python script version if the notebook doesn't work

## Offline Usage

All components of this package are designed to work completely offline. Once you have installed the required libraries, no internet connection is needed.
