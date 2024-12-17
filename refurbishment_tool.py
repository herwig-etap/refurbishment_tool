# File: refurbishment_tool.py
import streamlit as st
import pandas as pd

# Constants
CO2_CONVERSION_FACTOR = 0.42  # kg CO2 per kWh (average emission factor)
ENERGY_COST = 0.15  # Cost per kWh in USD
LIFECYCLE_EXTENSION_YEARS = 10  # Average extension after refurbishment

# Function to calculate energy and savings
def calculate_refurbishment(current_power, upgrade_power, operating_hours, age, cost_of_refurbishment):
    energy_consumed_current = current_power * operating_hours
    energy_consumed_upgrade = upgrade_power * operating_hours

    annual_energy_savings = energy_consumed_current - energy_consumed_upgrade
    annual_cost_savings = annual_energy_savings * ENERGY_COST
    co2_reduction = annual_energy_savings * CO2_CONVERSION_FACTOR

    payback_period = cost_of_refurbishment / annual_cost_savings if annual_cost_savings > 0 else "N/A"
    lifecycle_extension = age + LIFECYCLE_EXTENSION_YEARS

    return {
        "Annual Energy Savings (kWh)": annual_energy_savings,
        "Annual Cost Savings (USD)": annual_cost_savings,
        "CO₂ Reduction (kg/year)": co2_reduction,
        "Payback Period (years)": payback_period,
        "New Lifecycle Duration (years)": lifecycle_extension
    }

# Streamlit App
def main():
    st.title("Lighting System Refurbishment Assessment Tool")
    st.write("""
    Evaluate the energy savings, cost reduction, and lifecycle extension of upgrading your lighting system.
    """)

    # Input Form
    st.header("Input Your Current Lighting System Details")
    current_power = st.number_input("Current System Power Consumption (W)", min_value=0.0, value=500.0)
    upgrade_power = st.number_input("Proposed Upgrade Power Consumption (W)", min_value=0.0, value=200.0)
    operating_hours = st.number_input("Annual Operating Hours", min_value=0, value=4000)
    age = st.number_input("Current System Age (years)", min_value=0, value=5)
    cost_of_refurbishment = st.number_input("Estimated Cost of Refurbishment (USD)", min_value=0.0, value=1000.0)

    # Calculation Trigger
    if st.button("Calculate"):
        results = calculate_refurbishment(current_power, upgrade_power, operating_hours, age, cost_of_refurbishment)

        # Display Results
        st.header("Refurbishment Results")
        st.write(pd.DataFrame([results]))

        # Insights
        st.subheader("Insights")
        st.write(f"""
        - **Energy Savings**: {results['Annual Energy Savings (kWh)']} kWh annually.
        - **Cost Savings**: ${results['Annual Cost Savings (USD)']:.2f} per year.
        - **CO₂ Reduction**: {results['CO₂ Reduction (kg/year)']:.2f} kg annually.
        - **Payback Period**: {results['Payback Period (years)']} years.
        - **Extended System Lifecycle**: {results['New Lifecycle Duration (years)']} years.
        """)

        
    st.write("---")
    st.write("Developed with ❤️ by Code Copilot")

if __name__ == "__main__":
    main()
