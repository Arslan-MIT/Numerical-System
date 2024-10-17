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

# Custom Styling with Improved Color Scheme and Animations
st.markdown("""
    <style>
    /* Overall page styling */
    .stApp {
        background-color: #EAEDED;  /* Light grey background for better contrast */
    }
    /* Title styling */
    .title {
        color: #1C2833;  /* Dark navy for high contrast text */
        font-size: 42px;
        font-family: 'Arial', sans-serif;
        text-align: center;
        font-weight: bold;
        padding: 10px;
        border-radius: 10px;
    }
    /* Button styling with hover animation */
    .stButton > button {
        background-color: #3498DB;  /* Bright blue for buttons */
        color: white;
        padding: 12px;
        border: none;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: transform 0.2s ease, background-color 0.3s ease; /* Button animation */
    }
    /* Button hover effect */
    .stButton > button:hover {
        background-color: #2E86C1;  /* Darker blue on hover */
        transform: scale(1.05);  /* Slight scale effect */
    }
    /* Separator styling */
    .separator {
        border-top: 4px solid #34495e;
        margin: 20px 0;
    }
    /* Subheader styling */
    .stText {
        color: #1C2833;
        font-size: 24px;
        font-family: 'Arial', sans-serif;
    }
    /* Input box styling */
    input {
        border: 2px solid #3498DB;
        border-radius: 8px;
        padding: 10px;
        font-size: 18px;
        color: #34495e;
    }
    /* Output text styling */
    .output-text {
        color: #1C2833; /* Dark text color */
        background-color: #D5E8F2; /* Light blue background for output */
        padding: 10px;
        border-radius: 8px;
        font-size: 18px;
    }
    /* Custom styling for footer text */
    .footer-text {
        color: #2980B9; /* Change to a nice blue */
        font-size: 16px;
        font-family: 'Arial', sans-serif;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to display animated loader or progress spinner
def display_loader():
    with st.spinner('Converting...'):
        sleep(1.5)

# Streamlit App Main Function
def main():
    # App title
    st.markdown('<h1 class="title">Interactive Numerical Converter</h1>', unsafe_allow_html=True)

    # Separator
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    # Conversion Type Selection
    st.markdown('<h3 class="stText">Choose Conversion Type:</h3>', unsafe_allow_html=True)
    conversion_type = st.selectbox(
        "Select Conversion:",
        ["Decimal to Binary", "Decimal to Octal", "Decimal to Hexadecimal", "Binary to Decimal", "Octal to Decimal", "Hexadecimal to Decimal"]
    )

    # Input fields based on conversion type
    if "Decimal to" in conversion_type:
        num = st.number_input("Enter Decimal Number", min_value=0)
    else:
        num_str = st.text_input("Enter the Number for Conversion:")

    # Convert button with animation
    if st.button("Convert"):
        display_loader()  # Show animated loader

        # Perform conversion based on type
        if conversion_type == "Decimal to Binary":
            st.markdown(f'<div class="output-text">Binary: {decimal_to_binary(int(num))}</div>', unsafe_allow_html=True)
        elif conversion_type == "Decimal to Octal":
            st.markdown(f'<div class="output-text">Octal: {decimal_to_octal(int(num))}</div>', unsafe_allow_html=True)
        elif conversion_type == "Decimal to Hexadecimal":
            st.markdown(f'<div class="output-text">Hexadecimal: {decimal_to_hexadecimal(int(num))}</div>', unsafe_allow_html=True)
        elif conversion_type == "Binary to Decimal":
            try:
                st.markdown(f'<div class="output-text">Decimal: {binary_to_decimal(num_str)}</div>', unsafe_allow_html=True)
            except ValueError:
                st.error("Invalid binary number. Please enter a valid binary number.")
        elif conversion_type == "Octal to Decimal":
            try:
                st.markdown(f'<div class="output-text">Decimal: {octal_to_decimal(num_str)}</div>', unsafe_allow_html=True)
            except ValueError:
                st.error("Invalid octal number. Please enter a valid octal number.")
        elif conversion_type == "Hexadecimal to Decimal":
            try:
                st.markdown(f'<div class="output-text">Decimal: {hexadecimal_to_decimal(num_str)}</div>', unsafe_allow_html=True)
            except ValueError:
                st.error("Invalid hexadecimal number. Please enter a valid hexadecimal number.")

    st.markdown('<div class="footer-text">Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()
