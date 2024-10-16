import streamlit as st

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

# Streamlit App
def main():
    st.title("Numerical Converter")

    # Conversion type selection
    conversion_type = st.selectbox(
        "Select the conversion type:",
        ["Decimal to Binary", "Decimal to Octal", "Decimal to Hexadecimal",
         "Binary to Decimal", "Octal to Decimal", "Hexadecimal to Decimal"]
    )

    # Based on the conversion type, show relevant input fields
    if conversion_type == "Decimal to Binary":
        num = st.number_input("Enter a decimal number:", min_value=0)
        if st.button("Convert"):
            st.success(f"Binary: {decimal_to_binary(int(num))}")

    elif conversion_type == "Decimal to Octal":
        num = st.number_input("Enter a decimal number:", min_value=0)
        if st.button("Convert"):
            st.success(f"Octal: {decimal_to_octal(int(num))}")

    elif conversion_type == "Decimal to Hexadecimal":
        num = st.number_input("Enter a decimal number:", min_value=0)
        if st.button("Convert"):
            st.success(f"Hexadecimal: {decimal_to_hexadecimal(int(num))}")

    elif conversion_type == "Binary to Decimal":
        binary = st.text_input("Enter a binary number (e.g., 1010):")
        if st.button("Convert"):
            try:
                st.success(f"Decimal: {binary_to_decimal(binary)}")
            except ValueError:
                st.error("Invalid binary number. Please enter a valid binary number.")

    elif conversion_type == "Octal to Decimal":
        octal = st.text_input("Enter an octal number (e.g., 12):")
        if st.button("Convert"):
            try:
                st.success(f"Decimal: {octal_to_decimal(octal)}")
            except ValueError:
                st.error("Invalid octal number. Please enter a valid octal number.")

    elif conversion_type == "Hexadecimal to Decimal":
        hexadecimal = st.text_input("Enter a hexadecimal number (e.g., 1A):")
        if st.button("Convert"):
            try:
                st.success(f"Decimal: {hexadecimal_to_decimal(hexadecimal)}")
            except ValueError:
                st.error("Invalid hexadecimal number. Please enter a valid hexadecimal number.")

# Running the app
if __name__ == "__main__":
    main()
