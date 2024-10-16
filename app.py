import streamlit as st
from time import sleep

# Conversion Functions
def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def decimal_to_octal(n):
    return oct(n).replace("0o", "")

def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "").upper()

def binary_to_decimal(b):
    return int(b, 2)

def octal_to_decimal(o):
    return int(o, 8)

def hexadecimal_to_decimal(h):
    return int(h, 16)

# Custom Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;  /* Light Background */
    }
    .title {
        color: #2d3436;
        font-size: 36px;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
    }
    .stButton > button {
        background-color: #0984e3;
        border: none;
        color: white;
        padding: 10px;
        text-align: center;
        font-size: 16px;
        margin: 10px 2px;
        cursor: pointer;
        width: 100%;
        border-radius: 10px;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #74b9ff;
    }
    .separator {
        border-top: 3px solid #6c5ce7;
        margin: 15px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Function to display loaders or animations
def display_loader():
    with st.spinner('Converting...'):
        sleep(1.5)

# Streamlit App Main Function
def main():
    st.markdown('<h1 class="title">Interactive Numerical Converter</h1>', unsafe_allow_html=True)

    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)  # Add a custom separator

    # Conversion Type Selection with a Progress Bar or Animated Loader
    st.subheader("Choose Conversion Type:")
    conversion_type = st.selectbox(
        "Select Conversion:",
        ["Decimal
