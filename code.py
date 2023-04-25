import streamlit as st

# Define the likelihoods
p_botrytis = st.sidebar.slider(
    "Chance of Botrytis", 0.0, 1.0, 0.2, 0.01
)
p_low_sugar = st.sidebar.slider(
    "Chance of Low Sugar", 0.0, 1.0, 0.4, 0.01
)
p_med_sugar = st.sidebar.slider(
    "Chance of Medium Sugar", 0.0, 1.0, 0.4, 0.01
)
p_high_sugar = st.sidebar.slider(
    "Chance of High Sugar", 0.0, 1.0 - p_low_sugar - p_med_sugar, 0.2, 0.01
)

# Calculate the expected values
ev_harvest = 960000
ev_not_harvest = (
    0.04 * (3.3 * p_botrytis + 0.42 * (1 - p_botrytis))
    + 0.96
    * (
        0.96 * p_low_sugar
        + 1.41 * p_med_sugar
        + 1.5 * p_high_sugar
    )
    + 0.88 * (3.3 * p_botrytis + 0.42 * (1 - p_botrytis))
    + 0.12
    * (0.96 * p_low_sugar + 1.41 * p_med_sugar + 1.5 * p_high_sugar)
) * 100000

# Determine the recommended alternative
if ev_harvest > ev_not_harvest:
    recommendation = "Harvest"
else:
    recommendation = "Do not harvest"

# Display the results
st.title("Grape Harvest Recommendation System")
st.sidebar.title("Parameters")
st.sidebar.write("Adjust the following parameters to see the recommendation:")
st.sidebar.write("---")
st.sidebar.write(f"Chance of Botrytis: {p_botrytis:.2f}")
st.sidebar.write(f"Chance of Low Sugar: {p_low_sugar:.2f}")
st.sidebar.write(f"Chance of Medium Sugar: {p_med_sugar:.2f}")
st.sidebar.write(f"Chance of High Sugar: {p_high_sugar:.2f}")
st.sidebar.write("---")

st.write(f"Expected value of harvest: ${ev_harvest:,.2f}")
st.write(f"Expected value of not harvest: ${ev_not_harvest:,.2f}")
st.write(f"Recommended alternative: {recommendation}")