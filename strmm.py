# import streamlit as st
# st.title("I am streamlit")
# st.subheader("Am mani sub header")
# st.header("CVR COllge header")
# st.markdown("# HELLO ") #using H it will bold   // ## is h2 and ### h3
#
# st.markdown("[google](https://google.com)")
# st.caption("AM CAPTION")
# st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
#
#
import streamlit as st

# Title of the app
st.title("Shopping Expense Calculator 💸")

# Inputs for employee salary and shopping bills
emp_salary = st.number_input("Enter Employee Salary",  step=1, format="%d")
shopping_bill1 = st.number_input("Enter Shopping Bill 1 Amount", min_value=0, value=0, step=1, format="%d")
shopping_bill2 = st.number_input("Enter Shopping Bill 2 Amount", min_value=0, value=0, step=1, format="%d")
shopping_bill3 = st.number_input("Enter Shopping Bill 3 Amount", min_value=0, value=0, step=1, format="%d")

# Calculate the total shopping amount and percentage
if emp_salary > 0:
    total_amt_shopping_used = shopping_bill1 + shopping_bill2 + shopping_bill3
    percentage_used = (total_amt_shopping_used / emp_salary) * 100

    # Display the results
    st.write(f"### Total Amount Used in Shopping: **₹{total_amt_shopping_used}**")
    st.write(f"### Percentage of Salary Used in Shopping: **{percentage_used:.2f}%**")
else:
    st.warning("Please enter a valid Employee Salary greater than 0 to calculate.")


