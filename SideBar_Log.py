import streamlit as st
from DBService import DbService
#from Authent import main_authentication
from Users import Users,UsersDao


def Sign(dbs: DbService):
    auth = st.container()

    with auth:
        Sign_request = auth.expander(label="Iscriviti", expanded=False)
        with Sign_request:
            Sign_up(dbs=dbs)
        Log_request = auth.expander(label="Connetti al tuo account", expanded=False)
        with Log_request:
            name, passw = Log_in_form(dbs)

    return name, passw


def Sign_up(dbs: DbService):
    New_user_Registration = st.form(key="New_user_Registration", clear_on_submit=True)

    with New_user_Registration:
        with st.container():
                nick = st.text_input(label="Nickname", max_chars=50)
                password = st.text_input(label="Password", max_chars=50, type="password")
                telemetry = st.text_input(label="Telemetry url", type="password")
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            usr = Users(nickname=nick, pass_w=password, telemetry_url=telemetry)
            usr_srv = UsersDao(Dbs=dbs)
            #if not usr_srv.is_user_registered(User=usr):
            usr_srv.insert(User=usr)
            st.success(f"Ciao {nick}, hai effettuato la registrazione con successo")
           # elif usr_srv.is_user_registered(User=usr):
            #    st.error(f"Ci spiace ma {nick} è già presente, scegli un altro nickname")
            #else:
            #    st.warning("Ci spiace ma qualcosa è andato storto")
        return

""" 
def Log_in_form(dbs: DbService):
    try:
        return main_authentication(DbService=dbs)
    except Exception as ex:
        print(ex)
"""