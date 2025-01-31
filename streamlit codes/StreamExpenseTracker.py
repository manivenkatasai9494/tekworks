import streamlit as st

# st.title("MANI VENKATA SAI")
# st.title("SAHAARH PABBATHI")
# st.header("CVR COLLEGE ENGINEERING")
# st.subheader("THIS IS SUB HEADER")
# st.markdown("# it was h1")

st.title("Shopping ")


emp_salary = st.number_input("Enter Employee Salary",  step=1)
shopping_bill1 = st.number_input("Enter Shopping Bill 1 Amount", min_value=0, step=1)
shopping_bill2 = st.number_input("Enter Shopping Bill 2 Amount", min_value=0, step=1)
shopping_bill3 = st.number_input("Enter Shopping Bill 3 Amount", min_value=0, step=1 )

if emp_salary > 0:
    total_amt_shopping_used = shopping_bill1 + shopping_bill2 + shopping_bill3
    percentage_used = (total_amt_shopping_used / emp_salary) * 100
    st.write(f"### Total Amount Used in Shopping =  **{total_amt_shopping_used}**")
    st.write(f"### Percentage of Salary Used in Shopping= **{percentage_used:.2f}%**")
else:
    st.warning("Please enter a valid Employee Salary greater than 0 to calculate.")