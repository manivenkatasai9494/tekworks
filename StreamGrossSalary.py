import streamlit as st
st.title("Gross Salary Calculator")
basicSalary = st.number_input("Enter Basic Salary:", min_value=0, value=0, step=1, key="basic_salary")
if basicSalary > 0:
    if basicSalary < 10000:
        HRA = basicSalary * (67 / 100)
        DA = basicSalary * (73 / 100)
    elif 10000 <= basicSalary <= 20000:
        HRA = basicSalary * (69 / 100)
        DA = basicSalary * (76 / 100)
    else:
        HRA = basicSalary * (73 / 100)
        DA = basicSalary * (89 / 100)

    GrossSalary = HRA + DA + basicSalary
    st.write(f"Basic Salary={basicSalary}")
    st.write(f"**HRA:** {HRA}")
    st.write(f"**DA:** {DA}")
    st.write(f"### Total Gross Salary: ₹{GrossSalary}")
else:
    st.warning("Please enter a valid Basic Salary greater than 0.")
