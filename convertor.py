import streamlit as st


st.set_page_config(page_title="Unit Converter", layout="centered")


st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 20px;
        border-radius: 15px;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(to right, #4CAF50, #45a049);
        color: white;
        padding: 12px;
        font-size: 18px;
        border-radius: 8px;
        border: none;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    
    /* Select box styling */
    .stSelectbox {
        margin: 15px 0;
    }
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 8px;
    }
    
    /* Success message styling */
    .success-message {
        background: linear-gradient(to right, #4CAF50, #45a049);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 22px;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Heading styling */
    h1 {
        background: linear-gradient(120deg, #1E88E5, #1565C0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 20px;
        font-size: 45px;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Number input styling */
    .stNumberInput {
        margin: 15px 0;
    }
    .stNumberInput > div > div > input {
        border-radius: 8px;
        background-color: rgba(255, 255, 255, 0.8);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #2C3E50 0%, #3498DB 100%);
    }
    .css-1d391kg .stRadio label {
        color: white;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2C3E50 0%, #3498DB 100%);
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        color: #666;
        padding: 20px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        margin-top: 30px;
    }

    /* Card styling */
    .card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
    }

    /* Input label styling */
    label {
        color: #2C3E50;
        font-weight: 500;
        font-size: 16px;
        margin-bottom: 8px;
    }

    /* Radio button styling */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("<h1>✨ Unit Converter ✨</h1>", unsafe_allow_html=True)


with st.sidebar:
    st.header("⚙️ Settings")
    
    # Theme selection
    theme = st.selectbox(
        "Choose Theme",
        ["Light", "Dark"],
        key="theme"
    )
    
    # Temperature scale preference
    temp_format = st.radio(
        "Default Temperature Scale",
        ["Celsius", "Fahrenheit", "Kelvin"],
        key="temp_format"
    )
    
    st.markdown("---")
    st.markdown("""
    ### Quick Reference
    
    🌡️ **Temperature**
    - Water freezes at:
        - 0°C
        - 32°F
        - 273.15K
    - Water boils at:
        - 100°C
        - 212°F
        - 373.15K
    
    ### About
    This converter helps you convert between different units of measurement.
    """)

# Dark theme styling
if theme == "Dark":
    st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #1E1E1E 0%, #2D3436 100%);
            color: #ffffff;
        }
        h1 {
            background: linear-gradient(120deg, #00ADB5, #00838F);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .success-message {
            background: linear-gradient(to right, #00ADB5, #00838F);
        }
        .stButton>button {
            background: linear-gradient(to right, #00ADB5, #00838F);
        }
        .stSelectbox > div > div {
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
        }
        .stNumberInput > div > div > input {
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
        }
        label {
            color: #ffffff;
        }
        .card {
            background: rgba(255, 255, 255, 0.05);
        }
    </style>
    """, unsafe_allow_html=True)

# Create a container with background
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Create conversion categories
    conversion_type = st.selectbox(
        "Select Conversion Type",
        ["Length", "Weight", "Temperature"],
        key="conversion_type"
    )

    # Input value with custom styling
    col1, col2 = st.columns([3, 1])
    with col1:
        input_value = st.number_input("Enter value to convert", value=0.0, key="input_value")

    # Conversion logic for Length
    if conversion_type == "Length":
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From", ["Meters", "Kilometers", "Miles", "Feet"])
        with col2:
            to_unit = st.selectbox("To", ["Meters", "Kilometers", "Miles", "Feet"])
        
        if st.button("Convert!", key="convert_length"):
            # Convert everything to meters first
            if from_unit == "Kilometers":
                meters = input_value * 1000
            elif from_unit == "Miles":
                meters = input_value * 1609.34
            elif from_unit == "Feet":
                meters = input_value * 0.3048
            else:
                meters = input_value
            
            # Convert meters to target unit
            if to_unit == "Kilometers":
                result = meters / 1000
            elif to_unit == "Miles":
                result = meters / 1609.34
            elif to_unit == "Feet":
                result = meters / 0.3048
            else:
                result = meters
                
            st.markdown(f"""
            <div class="success-message">
                {input_value} {from_unit} = {result:.2f} {to_unit}
            </div>
            """, unsafe_allow_html=True)

    # Conversion logic for Weight
    elif conversion_type == "Weight":
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
        with col2:
            to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
        
        if st.button("Convert!", key="convert_weight"):
            # Convert everything to kilograms first
            if from_unit == "Grams":
                kg = input_value / 1000
            elif from_unit == "Pounds":
                kg = input_value * 0.453592
            elif from_unit == "Ounces":
                kg = input_value * 0.0283495
            else:
                kg = input_value
            
            # Convert kilograms to target unit
            if to_unit == "Grams":
                result = kg * 1000
            elif to_unit == "Pounds":
                result = kg / 0.453592
            elif to_unit == "Ounces":
                result = kg / 0.0283495
            else:
                result = kg
                
            st.markdown(f"""
            <div class="success-message">
                {input_value} {from_unit} = {result:.2f} {to_unit}
            </div>
            """, unsafe_allow_html=True)

    # Conversion logic for Temperature
    else:
        col1, col2 = st.columns(2)
        with col1:
            # Set default temperature scale based on sidebar selection
            temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
            # Move preferred temperature to the start of the list
            temp_units.remove(temp_format)
            temp_units.insert(0, temp_format)
            from_unit = st.selectbox("From", temp_units)
        with col2:
            to_unit = st.selectbox("To", temp_units)
        
        if st.button("Convert!", key="convert_temp"):
            # Convert everything to Celsius first
            if from_unit == "Fahrenheit":
                celsius = (input_value - 32) * 5/9
            elif from_unit == "Kelvin":
                celsius = input_value - 273.15
            else:
                celsius = input_value
            
            
            if to_unit == "Fahrenheit":
                result = (celsius * 9/5) + 32
            elif to_unit == "Kelvin":
                result = celsius + 273.15
            else:
                result = celsius
                
            st.markdown(f"""
            <div class="success-message">
                {input_value} {from_unit} = {result:.2f} {to_unit}
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    Made with ❤️ by Hamna
</div>
""", unsafe_allow_html=True)
