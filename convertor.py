import streamlit as st


st.set_page_config(page_title="Package Calculator", layout="centered")


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


st.markdown("<h1>📦 Ramazan Package Calculator 📦</h1>", unsafe_allow_html=True)

# Define package items and their units
package_items = {
    "Flour": {"unit": "kg", "default": 5},
    "Rice": {"unit": "kg", "default": 2},
    "Sugar": {"unit": "kg", "default": 1},
    "Cooking Oil": {"unit": "ltr", "default": 1},
    "Dates": {"unit": "g", "default": 200},
    "Tea": {"unit": "g", "default": 80},
    "Chickpeas": {"unit": "kg", "default": 1},
    "Dal Chana": {"unit": "kg", "default": 1},
    "Vermicelli": {"unit": "g", "default": 150},
    "Salt": {"unit": "g", "default": 800},
    "Sharbat": {"unit": "ml", "default": 800}
}

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Package selection
    package_type = st.selectbox(
        "Select Package Type",
        ["Basic Package", "Premium Package", "Custom Package"]
    )

    if package_type == "Custom Package":
        st.subheader("Customize Your Package")
        total_price = 0
        selected_items = {}

        for item, details in package_items.items():
            col1, col2, col3 = st.columns([3, 2, 2])
            with col1:
                quantity = st.number_input(
                    f"{item} ({details['unit']})", 
                    value=float(details['default']),
                    step=0.1
                )
            with col2:
                price_per_unit = st.number_input(
                    f"Price per {details['unit']}", 
                    value=0.0,
                    step=0.1
                )
            with col3:
                item_total = quantity * price_per_unit
                st.text(f"Total: Rs. {item_total:.2f}")
                total_price += item_total
                if quantity > 0:
                    selected_items[item] = f"{quantity} {details['unit']}"

        if st.button("Calculate Total"):
            st.markdown(f"""
            <div class="success-message">
                <h3>Package Summary</h3>
                <p>Selected Items:</p>
                {"<br>".join([f"• {item}: {qty}" for item, qty in selected_items.items()])}
                <h4>Total Price: Rs. {total_price:.2f}</h4>
            </div>
            """, unsafe_allow_html=True)

    else:
        # Pre-defined packages
        if package_type == "Basic Package":
            package_price = 2849
            package_items_display = {
                "Flour": "5 kg",
                "Rice": "2 kg",
                "Sugar": "1 kg",
                "Cooking Oil": "1 ltr",
                "Dal Chana": "1 kg",
                "Tea": "80 g"
            }
        else:  # Premium Package
            package_price = 4999
            package_items_display = {
                "Flour": "10 kg",
                "Rice": "5 kg",
                "Sugar": "2 kg",
                "Cooking Oil": "2 ltr",
                "Dal Chana": "2 kg",
                "Tea": "160 g",
                "Dates": "400 g",
                "Sharbat": "1600 ml"
            }

        st.markdown(f"""
        <div class="success-message">
            <h3>{package_type}</h3>
            <p>Package Contents:</p>
            {"<br>".join([f"• {item}: {qty}" for item, qty in package_items_display.items()])}
            <h4>Package Price: Rs. {package_price}</h4>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    Ramazan Mubarak! 🌙
</div>
""", unsafe_allow_html=True)
