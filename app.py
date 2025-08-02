
import pandas as pd
import pickle as pk
import streamlit as st

# Set page configuration
st.set_page_config(page_title="House Price Predictor", layout="centered")

# Load the model and dataset
model = pk.load(open(r'C:\Users\ASUS\SATISH 22\House prediction\House_prediction_model.pkl', 'rb'))
data = pd.read_csv(r'C:\Users\ASUS\SATISH 22\House prediction\cleaned_data.csv')

# App title
st.title(" House Price Predictor")
st.markdown("### Estimate your  house price with a few details.")
st.write("Fill in the inputs below to predict the estimated selling price of your house.")

st.markdown("---")

# Input Section
col1, col2 = st.columns(2)

with col1:
    location = st.selectbox(" Location", sorted(data['location'].unique()))
    sqft = st.number_input(" Total Area (in Sq. Ft.)", min_value=200.0, step=10.0)

with col2:
    bedrooms = st.number_input(" Bedrooms", min_value=1, step=1)
    bathrooms = st.number_input(" Bathrooms", min_value=1, step=1)
    balconies = st.number_input(" Balconies", min_value=0, step=1)

st.markdown("---")

# Predict button
if st.button(" Predict Price"):
    input_df = pd.DataFrame([[location, sqft, bathrooms, balconies, bedrooms]],
                            columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])
    
    try:
        prediction = model.predict(input_df)[0]
        price = round(prediction * 1e5, 2)
        st.success(f" **Estimated Price:** ₹ {price:,.2f}")
    except Exception as e:
        st.error("⚠️ Something went wrong during prediction. Please check the inputs or model.")

# Footer
st.markdown("---")
st.caption("Crafted by Satish Dwivedi ❤️ | Powered by cleaned and refined housing data.")

