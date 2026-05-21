import streamlit as st

# Set up page configurations
st.set_page_config(
    page_title="EWA Bill Calculator",
    page_icon="⚡",
    layout="centered"
)

# ==========================================
# SIDEBAR: CONFIGURABLE RATES
# ==========================================
st.sidebar.header("⚙️ Tariff & Rate Settings (BD)")

# Default values from your original script
ELECTRICITY_RATE = st.sidebar.number_input("Electricity Rate (per kWh)", value=0.032, format="%.3f")
WATER_RATE = st.sidebar.number_input("Water Rate (per m³)", value=0.775, format="%.3f")
SANITARY_RATE = st.sidebar.number_input("Sanitary Fee Rate", value=0.155, format="%.3f")

st.sidebar.markdown("---")
ELECTRICITY_ADMIN = st.sidebar.number_input("Elec. Admin Fee", value=1.000, format="%.3f")
WATER_ADMIN = st.sidebar.number_input("Water Admin Fee", value=1.000, format="%.3f")
MUNICIPALITY_FEE = st.sidebar.number_input("Municipality Fee", value=5.000, format="%.3f")

# ==========================================
# MAIN APP INTERFACE
# ==========================================
st.title("⚡ EWA Electricity & Water Bill Generator")
st.markdown("Calculate and preview your utility bills seamlessly. Adjust rates in the sidebar if needed.")

# User Inputs structured nicely using columns
st.subheader("📊 Enter Meter Readings")
days = st.slider("Billing Period (Days)", min_value=1, max_value=365, value=30)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### **Electricity (kWh)**")
    prev_elec = st.number_input("Previous Electricity Reading", min_value=0.0, value=0.0, step=1.0, format="%.1f")
    curr_elec = st.number_input("Current Electricity Reading", min_value=0.0, value=0.0, step=1.0, format="%.1f")

with col2:
    st.markdown("### **Water (m³)**")
    prev_water = st.number_input("Previous Water Reading", min_value=0.0, value=0.0, step=1.0, format="%.1f")
    curr_water = st.number_input("Current Water Reading", min_value=0.0, value=0.0, step=1.0, format="%.1f")

# ==========================================
# LOGIC & CALCULATIONS
# ==========================================
elec_consumption = curr_elec - prev_elec
water_consumption = curr_water - prev_water

# Validation Check
if elec_consumption < 0 or water_consumption < 0:
    st.error("⚠️ Error: Current readings cannot be lower than previous readings. Please check your inputs.")
else:
    # Calculations
    elec_charge = elec_consumption * ELECTRICITY_RATE
    elec_total = elec_charge + ELECTRICITY_ADMIN

    water_charge = water_consumption * WATER_RATE
    sanitary_fee = water_consumption * SANITARY_RATE
    water_total = water_charge + sanitary_fee + WATER_ADMIN

    grand_total = elec_total + water_total + MUNICIPALITY_FEE

    # ==========================================
    # DASHBOARD DISPLAY
    # ==========================================
    st.markdown("---")
    st.subheader("💰 Summary Dashboard")
    
    # Modern Metric Cards
    m1, m2, m3 = st.columns(3)
    m1.metric("Electricity Total", f"{elec_total:.3f} BD")
    m2.metric("Water Total", f"{water_total:.3f} BD")
    m3.metric("TOTAL AMOUNT DUE", f"{grand_total:.3f} BD", delta_color="inverse")

    # Tabs for detailed breakdown
    tab1, tab2, tab3 = st.tabs(["⚡ Electricity Details", "💧 Water Details", "📋 Printable Bill"])

    with tab1:
        st.markdown(f"**Consumption:** {elec_consumption:,.1f} kWh")
        st.markdown(f"**Energy Charge:** {elec_consumption:,.1f} × {ELECTRICITY_RATE:.3f} = **{elec_charge:.3f} BD**")
        st.markdown(f"**Administration Fee:** {ELECTRICITY_ADMIN:.3f} BD")
        st.info(f"Subtotal: {elec_total:.3f} BD")

    with tab2:
        st.markdown(f"**Consumption:** {water_consumption:,.1f} m³")
        st.markdown(f"**Water Charge:** {water_consumption:,.1f} × {WATER_RATE:.3f} = **{water_charge:.3f} BD**")
        st.markdown(f"**Sanitary Fee:** {water_consumption:,.1f} × {SANITARY_RATE:.3f} = **{sanitary_fee:.3f} BD**")
        st.markdown(f"**Administration Fee:** {WATER_ADMIN:.3f} BD")
        st.info(f"Subtotal: {water_total:.3f} BD")

    with tab3:
        # Recreating your exact classic text look inside a code box for printing/copying
        bill_text = f"""=======================================================
               EWA ELECTRICITY & WATER BILL
=======================================================

Billing Period : {days} Days

---------------------------------------------
ELECTRICITY
---------------------------------------------
Previous Reading      : {prev_elec:,.1f}
Current Reading       : {curr_elec:,.1f}
Consumption           : {elec_consumption:,.1f} kWh
Rate                  : {ELECTRICITY_RATE:.3f} BD
Energy Charge         : {elec_charge:.3f} BD
Administration Fees   : {ELECTRICITY_ADMIN:.3f} BD

Electricity Total     : {elec_total:.3f} BD

---------------------------------------------
WATER
---------------------------------------------
Previous Reading      : {prev_water:,.1f}
Current Reading       : {curr_water:,.1f}
Consumption           : {water_consumption:,.1f} m3

Water Charge          : {water_charge:.3f} BD ({water_consumption:,.1f} × {WATER_RATE:.3f})
Sanitary Fee          : {sanitary_fee:.3f} BD ({water_consumption:,.1f} × {SANITARY_RATE:.3f})
Administration Fees   : {WATER_ADMIN:.3f} BD

Water Total           : {water_total:.3f} BD

---------------------------------------------
OTHER CHARGES
---------------------------------------------
Municipality Fees     : {MUNICIPALITY_FEE:.3f} BD

=============================================
TOTAL AMOUNT DUE      : {grand_total:.3f} BD
=============================================

Pride in what we do.. Proud to serve..
======================================================="""
        
        st.text_area("Plain Text Receipt Preview", value=bill_text, height=450)
        
        # Add a download button for the text bill
        st.download_button(
            label="📥 Download Bill Text File",
            data=bill_text,
            file_name=f"EWA_Bill_{days}_days.txt",
            mime="text/plain"
        )
