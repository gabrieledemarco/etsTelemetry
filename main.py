from Game import Ets2
from datetime import datetime, timedelta
import streamlit as st
from DBService import DbService
from SideBar_Log import Sign_up
from Users import UsersDao, Users
from Authent import Login

dbs = DbService()
session_state = None
username = None

with st.sidebar:
    auth = st.container()
    with auth:
        Sign_request = auth.expander(label="Iscriviti", expanded=False)
        with Sign_request:
            Sign_up(dbs=dbs)
        Log_request = auth.expander(label="Connetti al tuo account", expanded=False)

        with Log_request:
            try:
                Log = Login(dbs)
                username, session_state = Log.LogIn_Authentication()
            except:
                print("")

if session_state:
    try:
        usr = Users(nickname=username)
        url = UsersDao(Dbs=dbs).get_user_telemetry(User=usr)[0]
        game = Ets2(url=url)

        #place_time = st.empty()
        place_container_connection = st.empty()
        place_container_job = st.empty()
        place_conteiner_truck = st.empty()

        while session_state:
           # place_time.write(f"⏳ {datetime.now()} seconds have passed")
            with place_container_connection:
                if game.game.connected[0]:
                    st.subheader("Game Connected")
                else:
                    st.subheader("Game is not connected")
                    st.text("Open Ets2 and connect to ets2-telemetry-server-master")
                    st.text(f"If Ets2 is working and connected then check IP address below:")
                    st.write(f"{game.url}")
                    st.write("You can download  ets2-telemetry-server-master from [Here]("
                             "https://github.com/Funbit/ets2-telemetry-server) ")

            with place_container_job:
                with st.expander(label="Job Info"):
                    st.subheader("Job Info")
                    st.text(f"Merce           : {game.trailer.mass[0]} Kg di {game.trailer.name[0]}")
                    st.text(f"Source City     : {game.job.sourceCity[0]}")
                    st.text(f"Source Company  : {game.job.sourceCompany[0]}")
                    st.text(f"Destination City: {game.job.destinationCity[0]}")
                    st.text(f"Expected Income : {game.job.income[0]}")
                    st.text(f"Expected Time of Journey: {game.expected_real_time()}")
                    st.text(f"Expected Time of Arrive : {game.expected_real_arriv()}")

           # with place_conteiner_truck:
           #     with st.expander(label="Truck info"):
           #         st.subheader("Truck Info")


    except:
        print("")
