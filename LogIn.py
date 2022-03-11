import streamlit as st
from Authent import Login
from DBService import DbService


def main():
    """ Simple Login App"""
    dbs = DbService()
    st.title("Simple Login App")
    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login":
        st.subheader("Login Section")

        with st.sidebar:
            Log = Login(dbs)
            username, session_state = Log.LogIn_Authentication()
       # username = st.sidebar.text_input("User Name")
       # passw = st.sidebar.text_input("Password", type="password")

        if st.sidebar.checkbox("Login"):
            # check correction of password
            st.success("Logged in as {}".format(username))

            task = st.selectbox("Task", ["Add Post", "Analytics", "Profiles"])

            if task == "Add Post":
                st.subheader("Add your post")
            elif task == "Analytics":
                st.subheader("Analytics")
            elif task == "Profiles":
                st.subheader("Profiles")

    elif choice == "SignUp":
        st.subheader("Create a new account")




if __name__ == '__main__':
    main()
