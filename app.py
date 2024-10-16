import streamlit as st
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

# Custom Styling: Inject some basic CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .title {
        color: #2e86de;
        font-size: 40px;
        font-family: 'Arial Black';
        text-align: center;
    }
    .convert-btn {
        background-color: #f39c12;
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        display: inline-block;
        font-size: 16px;
        margin: 10px 2px;
        cursor: pointer;
        transition: 0.3s;
        width: 100%;
        border-radius: 8px;
    }
    .convert-btn:hover {
        background-color: #e67e22;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit App
def main():
    st.markdown('<h1 class="title">Numerical Converter</h1>', unsafe_allow_html=True)

    # Optional: Add an image as a banner
    image = Image.open('converter_banner.jpg')  # Optional: Use an image
    st.image(image, use_column_width=True)

    st.write("---")  # Add a horizontal separator
    
    # Conversion type selection with improved layout
    st.subheader("Choose Conversion Type:")
    col1, col2, col3 = st.columns(3)
    with col1:
        conversion_type = st.selectbox(
            "Select Conversion:",
            ["Decimal to Binary", "Decimal to Octal", "Decimal to Hexadecimal"]
        )
    with col2:
        conversion_type_rev = st.selectbox(
            "Select Reverse Conversion:",
            ["Binary to Decimal", "Octal to Decimal", "Hexadecimal to Decimal"]
        )
    
    st.write("---")  # Add another horizontal separator

    # Input fields based on selection
    st.subheader(f"Perform {conversion_type} or {conversion_type_rev}:")

    col_input, col_output = st.columns(2)
    
    with col_input:
        if conversion_type == "Decimal to Binary":
            num = st.number_input("Enter Decimal Number", min_value=0)
            if st.button("Convert to Binary", key='bin', css_classes='convert-btn'):
                st.success(f"Binary: {decimal_to_binary(int(num))}")

        elif conversion_type == "Decimal to Octal":
            num = st.number_input("Enter Decimal Number", min_value=0)
            if st.button("Convert to Octal", key='octal', css_classes='convert-btn'):
                st.success(f"Octal: {decimal_to_octal(int(num))}")

        elif conversion_type == "Decimal to Hexadecimal":
            num = st.number_input("Enter Decimal Number", min_value=0)
            if st.button("Convert to Hexadecimal", key='hex', css_classes='convert-btn'):
                st.success(f"Hexadecimal: {decimal_to_hexadecimal(int(num))}")

    with col_output:
        if conversion_type_rev == "Binary to Decimal":
            binary = st.text_input("Enter Binary Number (e.g., 1010):")
            if st.button("Convert to Decimal", key='bin-rev', css_classes='convert-btn'):
                try:
                    st.success(f"Decimal: {binary_to_decimal(binary)}")
                except ValueError:
                    st.error("Invalid binary number. Please enter a valid binary number.")

        elif conversion_type_rev == "Octal to Decimal":
            octal = st.text_input("Enter Octal Number (e.g., 12):")
            if st.button("Convert to Decimal", key='octal-rev', css_classes='convert-btn'):
                try:
                    st.success(f"Decimal: {octal_to_decimal(octal)}")
                except ValueError:
                    st.error("Invalid octal number. Please enter a valid octal number.")

        elif conversion_type_rev == "Hexadecimal to Decimal":
            hexadecimal = st.text_input("Enter Hexadecimal Number (e.g., 1A):")
            if st.button("Convert to Decimal", key='hex-rev', css_classes='convert-btn'):
                try:
                    st.success(f"Decimal: {hexadecimal_to_decimal(hexadecimal)}")
                except ValueError:
                    st.error("Invalid hexadecimal number. Please enter a valid hexadecimal number.")

    st.write("---")
    st.write("Built with ❤️ using Streamlit")

# Running the app
if __name__ == "__main__":
    main()
