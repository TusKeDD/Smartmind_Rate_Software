import streamlit as st

st.title("📊 Price Calculator")

# Provide 2 options (single-choice menu)
optionsb = [
    "Option 1 - Timing",
    "Option 2 - Ribbed",
    "Option 3 - Flat"
]
choiceb = st.radio("**Choose Belt Type:**", optionsb)
st.info(f"📌 You selected: {choiceb}")

if choiceb == "Option 1 - Timing":
    # Take inputs from user
    lp_str = st.text_input("**Enter Landing Price (25mm):**", "")
    ds_str = st.text_input("**Enter Desired Size:**", "")

    # Convert safely to float
    try:
        lp = float(lp_str) if lp_str.strip() != "" else None
        ds = float(ds_str) if ds_str.strip() != "" else None

    except ValueError:
        lp, ds = None, None

    # Provide 7 options (single-choice menu)
    options = [
        "Option 1 - KP",
        "Option 2 - KK",
        "Option 3 - B",
        "Option 4 - L",
        "Option 5 - P",
        "Option 6 - J",
        "Option 7 - G",
        "Option 8 - RC",
        "Option 9 - PML",
        "Option 10 - Others"
    ]
    choice = st.radio("**Choose One Option:**", options)
    st.info(f"📌 You selected: {choice}")

    # Calculate
    if (lp is not None and lp >= 0) and (ds is not None and ds >= 0):
        if choice == "Option 10 - Others":
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

        elif choice == "Option 7 - G":
            lp = lp * (0.79)
            lp = (lp * (1.15)) / (0.9)
            lpf = lp * (ds / 25)
            d = 0.1

        elif choice == "Option 8 - RC":
            lp = lp * (0.79)
            lp = (lp * (1.16)) / (0.88)
            lpf = lp * (ds / 25)
            d = 0.12

        elif choice == "Option 9 - PML":
            lp = lp * (0.79)
            lp = (lp * (1.16)) / (0.975)
            lpf = lp * (ds / 25)
            d = 0.025

        st.write(f"✅ Price for 25mm: **{round(lp, 2)}**")
        st.write(f"🎯 Final Price for {int(ds)}mm: **{round(lpf, 2)}**")

    else:
        st.warning("Enter valid values!")


elif choiceb == "Option 2 - Ribbed":
    # Take inputs from user
    lp_str = st.text_input("**Enter Landing Price:**", "")

    try:
        lp = float(lp_str) if lp_str.strip() != "" else None
    
    except ValueError:
        lp = None

    # Provide 3 options (single-choice menu)
    options = [
        "Option 1 - P",
        "Option 2 - L",
        "Option 3 - KK",
        "Option 4 - B",
        "Option 5 - J",
        "Option 6 - PML",
        "Option 7 - RC",
        "Option 8 - Others"
    ]
    choice = st.radio("**Choose One Option:**", options)
    st.info(f"📌 You selected: {choice}")

    # Calculate
    if lp is not None and lp >= 0:
        if choice == "Option 8 - Others":
            lp = (lp * (1.18)) / (0.9)
            d = 0.1

        elif choice == "Option 1 - P":
            lp = lp * (1.16)
            d = 0

        elif choice == "Option 2 - L":
            lp = (lp * (1.16)) / (0.87)
            d = 0.13

        elif choice == "Option 3 - KK":
            lp = (lp * (1.18)) / (0.77)
            d = 0.23

        elif choice == "Option 4 - B":
            lp = (lp * (1.18)) / (0.80)
            d = 0.2

        elif choice == "Option 5 - J":
            lp = (lp * (1.18)) / (0.85)
            d = 0.15

        elif choice == "Option 6 - PML":
            lp = (lp * (1.18)) / (0.975)
            d = 0.025

        elif choice == "Option 7 - RC":
            lp = (lp * (1.18)) / (0.88)
            d = 0.12

        elif choice == "Option 8 - Others":
            lp = (lp * (1.18)) / (0.87)
            d = 0.13

        st.write(f"✅ Final Price: **{round(lp, 2)}**")

    else:
        st.warning("Enter valid values!")
    
elif choiceb == "Option 3 - Flat":
    # Take inputs from user
    l_str = st.text_input("**Enter Length (mm):**", "")
    w_str = st.text_input("**Enter Width (mm):**", "")

    try:
        l = float(l_str) if l_str.strip() != "" else None
        w = float(w_str) if w_str.strip() != "" else None
    
    except ValueError:
        l = None
        w = None

    if w is not None and w >= 0 and l is not None and l >= 0:
        if w > 50:
            l += 500
            st.info(f"📌 Belt width more than 50mm  ➡️  500mm skiving")
        else:
            l += 250
            st.info(f"📌 Belt width less than 50mm  ➡️  250mm skiving")

    optionssize = [
        "Grade 1 - TFL 10 S",
        "Grade 2 - TFL 12 S",
        "Grade 3 - TFL 18 S",
        "Grade 4 - TFL 15 E20",
        "Grade 5 - TFL 22 E26",
        "Grade 6 - HUS 500",
        "Grade 7 - TFL 15 E25",
        "Grade 8 - TLA 30 E30"
    ]
    choicesize = st.radio("**Choose a Grade:**", optionssize)
    st.info(f"📌 You selected: {choicesize}")

    if choicesize == "Grade 1 - TFL 10 S":
        s = 124
    elif choicesize == "Grade 2 - TFL 12 S":
        s = 162
    elif choicesize == "Grade 3 - TFL 18 S":
        s = 190
    elif choicesize == "Grade 4 - TFL 15 E20":
        s = 130
    elif choicesize == "Grade 5 - TFL 22 E26":
        s = 158
    elif choicesize == "Grade 6 - HUS 500":
        s = 142
    elif choicesize == "Grade 7 - TFL 15 E25":
        s = 140
    elif choicesize == "Grade 8 - TLA 30 E30":
        s = 189
    
    options = [
        "Option 1 - P",
        "Option 2 - L",
        "Option 3 - KK",
        "Option 4 - B",
        "Option 5 - J",
        "Option 6 - PML",
        "Option 7 - RC",
        "Option 8 - Others"
    ]
    choice = st.radio("**Choose One Option:**", options)
    st.info(f"📌 You selected: {choice}")

    # Calculate
    if l is not None and l >= 0 and w is not None and w >= 0 and s is not None and s >= 0:
        if choice == "Option 8 - Others":
            final = (l * w * s) / (1000* 10)
            final = final * (1.13)
            final = final / 0.9
        
        elif choice == "Option 1 - P":
            final = (l * w * s) / (1000* 10)
            final = final * (1.13)

        elif choice == "Option 2 - L":
            final = (l * w * s) / (1000* 10)
            final = final * (1.13)
            final = final / 0.87
        
        elif choice == "Option 3 - KK":
            final = (l * w * s) / (1000* 10)
            final = final * (1.13)
            final = final / 0.77
        
        elif choice == "Option 4 - B":
            final = (l * w * s) / (1000* 10)
            final = final * (1.13)
            final = final / 0.8
        
        elif choice == "Option 5 - J":
            final = (l * w * s) / (1000* 10)
            final = final * (1.13)
            final = final / 0.85
        
        elif choice == "Option 6 - PML":
            final = (l * w * s) / (1000* 10)
            final = final * (1.13)
            final = final / 0.975
        
        elif choice == "Option 7 - RC":
            final = (l * w * s) / (1000* 10)
            final = final * (1.13)
            final = final / 0.88
        
        st.write(f"✅ Final Price: **{round(final, 2)}**")

    else:
        st.warning("Enter valid values!")