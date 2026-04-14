import streamlit as st 


name = st.text_input("Enter your name")
newname = st.text_input("Enter your new name")
abc = st.text_area("Enter your text")
classdata = st.selectbox("Select your class",["Class 1","Class 2","Class 3"])


# if st.button("Submit"):
#     st.write("Hello", name ,"",newname,"",abc,"",classdata)

button = st.button("Submit")
if button:
    st.markdown(f"""Hello\n
                name: {name}\n
                new name: {newname}\n
                text: {abc}\n
                class:   {classdata}""")
