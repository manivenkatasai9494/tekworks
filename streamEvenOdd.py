import streamlit as st
class evenodd:
    def even(self):
        st.title("EVEN OR ODD")
        num1=st.number_input("Enter The Number",min_value=0,step=1)

        if st.button("EVEN?ODD"):
            if num1%2==0:
                st.success("It was even Number")
            else :
                st.warning("It was odd number")

name = evenodd()
name.even()