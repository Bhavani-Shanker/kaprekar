import streamlit as st

def kaprekar_step(num):
    # Convert the number to a zero-padded 4-digit string
    num_str = f"{num:04d}"
    
    # Create descending and ascending orders
    desc_num = int("".join(sorted(num_str, reverse=True)))
    asc_num = int("".join(sorted(num_str)))
    
    # Subtract ascending from descending
    result = desc_num - asc_num
    return desc_num, asc_num, result

def kaprekar_process(start_num):
    num = start_num
    steps = []
    while num != 6174:
        desc_num, asc_num, next_num = kaprekar_step(num)
        steps.append(f"{desc_num:04d} - {asc_num:04d} = {next_num:04d}")
        num = next_num
    steps.append("Reached 6174 (Kaprekar Constant)")
    return steps

# Streamlit app
st.title("Kaprekar Constant Calculator")

st.write("""
### Enter a four-digit number, and this app will calculate the steps to reach the Kaprekar constant (6174).
""")

# User input
input_num = st.number_input("Enter a 4-digit number (at least two different digits):", min_value=0, max_value=9999, step=1)

# Ensure number is valid and process
if 1000 <= input_num <= 9999:
    if len(set(str(input_num))) > 1:  # Ensure not all digits are the same
        steps = kaprekar_process(input_num)
        
        st.write(f"### Steps to reach Kaprekar constant for {input_num}:")
        for step in steps:
            st.write(step)
    else:
        st.write("Please enter a number with at least two different digits.")
else:
    st.write("Enter a valid four-digit number.")
