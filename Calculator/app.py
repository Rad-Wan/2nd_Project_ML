import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# Set page configuration
st.set_page_config(
    page_title="Tanzania Tourism Expense Calculator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #3366ff;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #5c5c5c;
        text-align: center;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .big-number {
        font-size: 3rem;
        font-weight: bold;
        color: #3366ff;
        text-align: center;
    }
    .info-text {
        color: #5c5c5c;
        font-size: 0.9rem;
    }
    .recommendation {
        background-color: #e6f7ff;
        padding: 15px;
        border-radius: 5px;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-header'>Tanzania Tourism Expense Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Estimate your travel expenses based on your preferences</p>", unsafe_allow_html=True)

# Load the model
@st.cache_resource
def load_model():
    try:
        # For offline use, we'll use a simplified calculation approach
        # The actual model would be loaded here in a production environment
        return None
    except:
        # If model not available, we'll use a simplified calculation approach
        return None

model = load_model()

# Sidebar for inputs
st.sidebar.header("Travel Details")

# Basic information
with st.sidebar.expander("Basic Information", expanded=True):
    country_options = ["United States", "United Kingdom", "Germany", "France", "China", 
                      "India", "South Africa", "Kenya", "Australia", "Canada", "Other"]
    country = st.selectbox("Country of Origin", country_options)
    
    age_group_options = ["18-24", "25-44", "45-64", "65+"]
    age_group = st.selectbox("Age Group", age_group_options)
    
    purpose_options = ["Leisure and Holidays", "Business", "Visiting Friends/Relatives", "Other"]
    purpose = st.selectbox("Purpose of Visit", purpose_options)
    
    travel_with_options = ["Alone", "Friends/Relatives", "Tour group", "Spouse", "Children", "Other"]
    travel_with = st.selectbox("Traveling With", travel_with_options)
    
    total_people = st.number_input("Number of People in Group", min_value=1, max_value=20, value=2)

# Accommodation and stay details
with st.sidebar.expander("Accommodation & Stay", expanded=True):
    accommodation_options = ["Hotel", "Lodge", "Resort", "Apartment/House Rental", "Camping", "Other"]
    accommodation_type = st.selectbox("Accommodation Type", accommodation_options)
    
    accommodation_cost_per_night = st.slider("Accommodation Cost per Night (USD)", 
                                           min_value=30, max_value=500, value=100, step=10)
    
    nights_mainland = st.slider("Nights in Mainland Tanzania", 
                              min_value=1, max_value=30, value=5)
    
    nights_zanzibar = st.slider("Nights in Zanzibar", 
                              min_value=0, max_value=14, value=0)
    
    total_nights = nights_mainland + nights_zanzibar

# Transportation
with st.sidebar.expander("Transportation", expanded=True):
    air_ticket_class_options = ["Economy", "Premium Economy", "Business", "First Class"]
    air_ticket_class = st.selectbox("Air Ticket Class", air_ticket_class_options)
    
    air_ticket_cost_mapping = {
        "Economy": 800,
        "Premium Economy": 1200,
        "Business": 2500,
        "First Class": 4000
    }
    
    transport_mode_options = ["Rental Car", "Tour Vehicle", "Public Transport", "Taxi/Uber", "Mix"]
    transport_mode = st.selectbox("Local Transportation Mode", transport_mode_options)
    
    transport_cost_mapping = {
        "Rental Car": 50,
        "Tour Vehicle": 80,
        "Public Transport": 15,
        "Taxi/Uber": 30,
        "Mix": 40
    }
    
    transport_cost_per_day = transport_cost_mapping[transport_mode]

# Activities and tours
with st.sidebar.expander("Activities & Tours", expanded=True):
    main_activity_options = ["Wildlife Safari", "Beach Holiday", "Mountain Climbing", 
                           "Cultural Tourism", "Business Meeting/Conference", "Other"]
    main_activity = st.selectbox("Main Activity", main_activity_options)
    
    tour_arrangement_options = ["Package Tour", "Independent Travel"]
    tour_arrangement = st.selectbox("Tour Arrangement", tour_arrangement_options)
    
    if tour_arrangement == "Package Tour":
        package_cost_per_day = st.slider("Package Tour Cost per Day (USD)", 
                                       min_value=100, max_value=1000, value=250, step=50)
    else:
        package_cost_per_day = 0
        
    tour_guide = st.checkbox("Hire a Tour Guide", value=False)
    tour_guide_cost_per_day = 50 if tour_guide else 0
    
    sites_to_visit = st.multiselect(
        "Sites to Visit",
        ["Serengeti National Park", "Ngorongoro Crater", "Mount Kilimanjaro", 
         "Zanzibar Beaches", "Stone Town", "Lake Manyara", "Tarangire National Park",
         "Selous Game Reserve", "Ruaha National Park", "Mafia Island"],
        default=["Serengeti National Park", "Ngorongoro Crater"]
    )
    
    site_costs = {
        "Serengeti National Park": 60,
        "Ngorongoro Crater": 50,
        "Mount Kilimanjaro": 70,
        "Zanzibar Beaches": 20,
        "Stone Town": 15,
        "Lake Manyara": 40,
        "Tarangire National Park": 45,
        "Selous Game Reserve": 55,
        "Ruaha National Park": 50,
        "Mafia Island": 30
    }
    
    total_site_cost = sum(site_costs[site] for site in sites_to_visit)

# Food and extras
with st.sidebar.expander("Food & Extras", expanded=True):
    meal_plan_options = ["Full Board", "Half Board", "Bed & Breakfast", "Self-Catering"]
    meal_plan = st.selectbox("Meal Plan", meal_plan_options)
    
    meal_cost_mapping = {
        "Full Board": 60,
        "Half Board": 40,
        "Bed & Breakfast": 20,
        "Self-Catering": 30
    }
    
    meal_cost_per_day = meal_cost_mapping[meal_plan]
    
    souvenirs = st.slider("Souvenir Budget (USD)", 
                        min_value=0, max_value=500, value=100, step=20)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Your Tanzania Adventure")
    
    # Display selected options summary
    st.subheader("Trip Summary")
    
    summary_data = {
        "Category": ["Basic Information", "", "", "", 
                    "Accommodation", "", 
                    "Transportation", "", 
                    "Activities", "", "", 
                    "Food & Extras", ""],
        "Detail": ["Origin", "Purpose", "Group Size", "Duration", 
                  "Type", "Location", 
                  "Air Ticket", "Local Transport", 
                  "Main Activity", "Tour Type", "Sites to Visit", 
                  "Meal Plan", "Souvenirs"],
        "Selection": [country, purpose, f"{total_people} people", f"{total_nights} nights", 
                     accommodation_type, f"{nights_mainland} nights mainland, {nights_zanzibar} nights Zanzibar", 
                     air_ticket_class, transport_mode, 
                     main_activity, tour_arrangement, ", ".join(sites_to_visit) if sites_to_visit else "None", 
                     meal_plan, f"${souvenirs}"]
    }
    
    summary_df = pd.DataFrame(summary_data)
    st.table(summary_df)
    
    # Instead of loading images from URLs (which requires internet),
    # we'll use emoji icons and descriptive text for offline use
    activity_emojis = {
        "Wildlife Safari": "🦁",
        "Beach Holiday": "🏖️",
        "Mountain Climbing": "🏔️",
        "Cultural Tourism": "🏛️",
        "Business Meeting/Conference": "💼",
        "Other": "✨"
    }
    
    selected_emoji = activity_emojis.get(main_activity, activity_emojis["Other"])
    
    st.markdown(f"""
    <div style="background-color:#f0f8ff; padding:20px; border-radius:10px; text-align:center;">
        <span style="font-size:72px;">{selected_emoji}</span>
        <h3>Experience {main_activity} in Tanzania</h3>
        <p>Your {total_nights}-night adventure awaits!</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.header("Cost Estimate")
    
    # Calculate costs
    # Air ticket cost (per person)
    air_ticket_total = air_ticket_cost_mapping[air_ticket_class] * total_people
    
    # Accommodation cost
    accommodation_total = accommodation_cost_per_night * total_nights * (total_people / 2 + 0.5)
    
    # Transportation cost
    transportation_total = transport_cost_per_day * total_nights
    
    # Activities cost
    if tour_arrangement == "Package Tour":
        activities_total = package_cost_per_day * total_nights * total_people
    else:
        activities_total = (total_site_cost + tour_guide_cost_per_day * total_nights) * total_people
    
    # Food cost
    food_total = meal_cost_per_day * total_nights * total_people
    
    # Souvenirs
    souvenirs_total = souvenirs
    
    # Calculate total cost
    total_cost = air_ticket_total + accommodation_total + transportation_total + activities_total + food_total + souvenirs_total
    
    # Apply model adjustment if available
    model_adjustment = 1.0
    if model is not None:
        # Create feature vector based on selections
        # This is simplified and would need to match the actual model features
        features = {
            'package_tour': 1 if tour_arrangement == "Package Tour" else 0,
            'purpose_leisure': 1 if purpose == "Leisure and Holidays" else 0,
            'total_nights': total_nights,
            'total_people': total_people
        }
        
        # In a real implementation, we would transform this to match the model's expected input
        # For now, we'll use a simplified adjustment
        if features['package_tour'] == 1:
            model_adjustment = 1.2  # Package tours tend to cost more
        if features['purpose_leisure'] == 1:
            model_adjustment *= 1.1  # Leisure travelers spend more
        if features['total_nights'] > 7:
            model_adjustment *= 0.9  # Longer stays get some discount
        if features['total_people'] > 2:
            model_adjustment *= 0.95  # Group discounts
    
    # Apply the adjustment
    adjusted_total = total_cost * model_adjustment
    
    # Display the cost breakdown
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.subheader("Cost Breakdown (USD)")
    
    cost_data = {
        "Category": ["Air Tickets", "Accommodation", "Local Transportation", 
                    "Activities & Tours", "Food & Drinks", "Souvenirs", "Total"],
        "Cost (USD)": [f"${air_ticket_total:,.2f}", 
                      f"${accommodation_total:,.2f}", 
                      f"${transportation_total:,.2f}", 
                      f"${activities_total:,.2f}", 
                      f"${food_total:,.2f}", 
                      f"${souvenirs_total:,.2f}", 
                      f"${adjusted_total:,.2f}"]
    }
    
    cost_df = pd.DataFrame(cost_data)
    st.table(cost_df)
    
    # Display the total cost prominently
    st.markdown(f"<p class='big-number'>${adjusted_total:,.2f}</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Estimated Total Cost</p>", unsafe_allow_html=True)
    
    # Add some context about the estimate
    st.markdown("<p class='info-text'>This estimate includes all major expenses for your trip. Actual costs may vary based on seasonal pricing, specific vendor choices, and exchange rates.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Recommendations to optimize cost
    st.subheader("Cost Optimization Tips")
    
    recommendations = []
    
    if air_ticket_class in ["Business", "First Class"]:
        recommendations.append("Consider Premium Economy for a balance of comfort and cost")
    
    if accommodation_cost_per_night > 200:
        recommendations.append("Look for accommodation deals during shoulder season")
    
    if tour_arrangement == "Independent Travel" and total_nights > 5:
        recommendations.append("Package tours may offer better value for longer stays")
    
    if meal_plan == "Full Board" and total_nights > 7:
        recommendations.append("Mix meal plans - try local restaurants for some meals")
    
    if len(sites_to_visit) > 4 and total_nights < 10:
        recommendations.append("Focus on fewer sites for a more relaxed experience")
    
    if not recommendations:
        recommendations.append("Your selections are already well optimized for cost and experience")
    
    for rec in recommendations:
        st.markdown(f"<div class='recommendation'>💡 {rec}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Tanzania Tourism Expense Calculator | Data Science Project</p>", unsafe_allow_html=True)
