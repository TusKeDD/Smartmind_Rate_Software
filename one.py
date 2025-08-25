import streamlit as st

st.title("📊 Price Calculator")

# Take inputs from user
lp = st.number_input("Enter Landing Price (25mm): ", min_value=0.0, step=0.1)
ds = st.number_input("Enter Desired Size: ", min_value=0.0, step=0.1)

# Calculate
if lp > 0:
    lp = lp * (0.79)
    lp = (lp * (1.16))*(1.11)
    lpf = lp * (ds/25)
    st.write(f"✅ Final Price (25mm): {round(lp,2)}")
    st.write(f"✅ Final Price ({int(ds)}mm): {round(lpf,2)}")
else:
    st.warning("Enter valid values!")
