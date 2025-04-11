# Tanzania Tourism Expense Calculator

This application allows users to calculate estimated expenses for tourists visiting Tanzania based on various selected features like length of stay, class of air ticket, tour guide services, meal plans, and site-seeing destinations.

## Installation Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Install Required Libraries
Open a terminal or command prompt and run:

```bash
pip install streamlit pandas numpy scikit-learn
```

### Step 2: Run the Application
Navigate to the directory containing the app.py file and run:

```bash
streamlit run app.py
```

This will start the application and automatically open it in your default web browser. If it doesn't open automatically, you can access it at http://localhost:8501

## Using the Application

1. Use the sidebar on the left to input your travel preferences:
   - Basic information (country of origin, age group, purpose of visit)
   - Accommodation details (type, cost per night, duration)
   - Transportation options (air ticket class, local transport mode)
   - Activities and tours (main activity, tour arrangement, sites to visit)
   - Food and extras (meal plan, souvenir budget)

2. The main panel will display:
   - A summary of your selected options
   - A visualization related to your main activity
   - A detailed cost breakdown
   - The total estimated cost
   - Cost optimization recommendations

## Offline Usage

This application is designed to work completely offline. Once you have installed the required libraries, no internet connection is needed to run the calculator.

## Customization

You can modify the app.py file to:
- Add more destination options
- Update pricing information
- Change the visual design
- Add additional features

## Troubleshooting

If you encounter any issues:
1. Ensure all required libraries are installed
2. Check that you're using a compatible Python version
3. Make sure you're running the command from the correct directory
