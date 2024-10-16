import streamlit as st
from time import sleep
from PIL import Image

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
    .button {
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
    .button:hover {
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

    # Optional: Add an image banner for aesthetics
    # Uncomment if you have a banner image: st.image('converter_banner.jpg', use_column_width=True)
    
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)  # Add a custom separator

    # Conversion Type Selection with a Progress Bar or Animated Loader
    st.subheader("Choose Conversion Type:")
    conversion_type = st.selectbox(
        "Select Conversion:",
        ["Decimal to Binary", "Decimal to Octal", "Decimal to Hexadecimal", "Binary to Decimal", "Octal to Decimal", "Hexadecimal to Decimal"]
    )

    # Dynamic input field based on conversion type
    if "Decimal to" in conversion_type:
        num = st.number_input("Enter Decimal Number", min_value=0)
    else:
        num_str = st.text_input("Enter the Number for Conversion:")

    # Button for Conversion
    if st.button("Convert", css_classes='button'):
        display_loader()  # Show a loader animation while converting

        # Show the result based on selected conversion type
        if conversion_type == "Decimal to Binary":
            st.success(f"Binary: {decimal_to_binary(int(num))}")
        elif conversion_type == "Decimal to Octal":
            st.success(f"Octal: {decimal_to_octal(int(num))}")
        elif conversion_type == "Decimal to Hexadecimal":
            st.success(f"Hexadecimal: {decimal_to_hexadecimal(int(num))}")
        elif conversion_type == "Binary to Decimal":
            try:
                st.success(f"Decimal: {binary_to_decimal(num_str)}")
            except ValueError:
                st.error("Invalid binary number. Please enter a valid binary number.")
        elif conversion_type == "Octal to Decimal":
            try:
                st.success(f"Decimal: {octal_to_decimal(num_str)}")
            except ValueError:
                st.error("Invalid octal number. Please enter a valid octal number.")
        elif conversion_type == "Hexadecimal to Decimal":
            try:
                st.success(f"Decimal: {hexadecimal_to_decimal(num_str)}")
            except ValueError:
                st.error("Invalid hexadecimal number. Please enter a valid hexadecimal number.")

    st.write("Built with ❤️ using Streamlit")

# Run the Streamlit app
if __name__ == "__main__":
    main()
