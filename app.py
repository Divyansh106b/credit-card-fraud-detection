import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("credit_card_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Credit Card Fraud Detection Model")
st.write(
    "Enter **30 numerical features** separated by commas\n\n"
    "**Order:** Time, V1, V2, ..., V28, Amount"
)

# Input field
input_df = st.text_input(
    "Enter features (comma-separated):",
    placeholder="e.g. 0.0, -1.23, 0.45, ... , 149.62"
)

submit = st.button("Submit")

if submit:
    try:
        # Convert input string to float list
        input_df_lst = [float(x.strip()) for x in input_df.split(",") if x.strip() != ""]

        # Check feature count
        if len(input_df_lst) != 30:
            st.error(" Please enter exactly 30 feature values")
        else:
            features = np.array(input_df_lst).reshape(1, -1)

            prediction = model.predict(features)[0]

            if prediction == 0:
                st.success(" Legitimate Transaction")
            else:
                st.error(" Fraudulent Transaction")

    except ValueError:
        st.warning(" Please enter only numeric values separated by commas")

