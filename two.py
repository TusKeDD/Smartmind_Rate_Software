import streamlit as st

st.title("📊 Price Calculator")

# Take inputs from user
lp = st.number_input("Enter Landing Price (25mm): ", min_value=0.0, step=0.1)
ds = st.number_input("Enter Desired Size: ", min_value=0.0, step=0.1)

# Provide 7 options (single-choice menu)
options = [
    "Option 1 - KP",
    "Option 2 - KK",
    "Option 3 - B",
    "Option 4 - L",
    "Option 5 - P",
    "Option 6 - J",
    "Option 7 - Others"
]
choice = st.radio("Choose one option:", options)
st.info(f"📌 You selected: {choice}")

# Calculate
if lp > 0 and ds > 0:
    if choice == "Option 7 - Others":
        lp = lp * (0.79) 
        lp = (lp * (1.16)) / (0.9)
        lpf = lp * (ds / 25)
        d = 0.1

    elif choice == "Option 1 - KP":
        lp = lp * (0.79)
        lp = lp * (1.16)
        lpf = lp * (ds / 25)
        d = 0.04

    elif choice == "Option 2 - KK":
        lp = lp * (0.79)
        lp = (lp * (1.15)) / (0.77)
        lpf = lp * (ds / 25)
        d = 0.23

    elif choice == "Option 3 - B":
        lp = lp * (0.79)
        lp = (lp * (1.15)) / (0.8)
        lpf = lp * (ds / 25)
        d = 0.2

    elif choice == "Option 4 - L":
        lp = lp * (0.79)
        lp = (lp * (1.14)) / (0.87)
        lpf = lp * (ds / 25)
        d = 0.13

    elif choice == "Option 5 - P":
        lp = lp * (0.79)
        lp = lp * (1.14)
        lpf = lp * (ds / 25)
        d = 0

    elif choice == "Option 6 - J":
        lp = lp * (0.79)
        lp = (lp * (1.16)) / (0.85)
        lpf = lp * (ds / 25)
        d = 0.15

    st.write(f"✅ Price for 25mm: **{round(lp, 2)}**")
    st.write(f"🎯 Final Price for {int(ds)}mm: **{round(lpf, 2)}**")
    st.write(f"🔻 Discounted Price for {int(ds)}mm ({choice[11:]} -> {d*100}%): **{round(lpf*(1-d), 2)}**")

else:
    st.warning("Enter valid values!")
