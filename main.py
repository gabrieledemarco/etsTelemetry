from Game import Ets2
from datetime import datetime, timedelta
import streamlit as st
from DBService import DbService
from SideBar_Log import Sign_up
from Users import UsersDao, Users
import streamlit_authenticator as stauth


def main_authentication(DbService: DbService):
    usr_serv = UsersDao(Dbs=DbService)
    names = usr_serv.get_users_list()
    passw = usr_serv.get_passw_list()
    name = ""
    try:
        authenticator = aunthenticator(names, passw)
        name, authentication_status = authenticator.login('Login', 'main')
        authentication_msg(authentication_status=authentication_status)
    except:
        print("")
    finally:
        return name, passw


def aunthenticator(names: list, password: list):
    hashed_passwords = stauth.hasher(password).generate()
    authenticator = stauth.authenticate(names, names, hashed_passwords,
                                        'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)
    return authenticator


def authentication_msg(authentication_status):
    if authentication_status is False:
        st.error("Username or Password are incorrect")
    elif authentication_status is True:
        st.success(f"User Authorized, welcome dear user ")
    elif authentication_status is None:
        st.warning("Please access to your account with a Username and Password")
    return


dbs = DbService()

auth = st.container()

with auth:
    Sign_request = auth.expander(label="Iscriviti", expanded=False)
    with Sign_request:
        Sign_up(dbs=dbs)
    Log_request = auth.expander(label="Connetti al tuo account", expanded=False)
    with Log_request:
        with st.form(key="LogIn"):
            nick = st.text_input(label="Nickname")
            pass_w = st.text_input(label="Password")

            if st.form_submit_button():
                usr = Users(nickname=nick, pass_w=pass_w)
                url = UsersDao(Dbs=dbs).get_user_telemetry(User=usr)[0]
                game = Ets2(url=url)

                with st.container():
                    st.subheader("Ets2 Dashboard")

                with st.container():
                    st.text(f"Merce           : {game.trailer.mass[0]} Kg di {game.trailer.name[0]}")
                    st.text(f"Source City     : {game.job.sourceCity[0]}")
                    st.text(f"Source Company  : {game.job.sourceCompany[0]}")
                    st.text(f"Destination City: {game.job.destinationCity[0]}")
                    st.text(f"Expected Income : {game.job.income[0]}")

                with st.container():
                    st.text(f"Expected Time of Journey: {game.expected_real_time()}")
                    st.text(f"Expected Time of Arrive : {game.expected_real_arriv()}")
