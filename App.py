import streamlit as st
import backend as bd

# Title of the web page
st.title("College Event Management System")

tab1, tab2, tab3, tab4 = st.tabs(["Register", "View Participants", "Search Participant", "Summary"])

# Prompt the user to enter their name

with tab1 :

    st.subheader("Register for an Event")
    name = st.text_input("Enter your name:")
    contact=st.text_input("Enter your contact number")
    dept=st.text_input("Enter your department")
    event=st.selectbox("Select an event :",bd.Events)
    attendance=st.selectbox("Select your participation status",["select","Attended","Not Attended"])


    if st.button("Confirm"):
        if name and dept and contact and event!="select" and attendance!="select" :
            bd.save_name(name,dept,contact,event,attendance)
            st.write(f"Hello, {name}! Welcome to the College event manager app.")
        elif event=="select" or attendance=="select" :
            st.warning("please select event and participation status")
        else:
            st.warning("please fill all the details.")



# Display the list of participants for a specific event. 

with tab2 :

    st.subheader("View Participants by Event")
    query_event = st.selectbox("Select an event to view participants:", bd.Events)

    if st.button("Confirm Event Participants"):
        names = bd.get_participants_for_event(query_event)
        if names:
            st.write(f"Names of participants in {query_event}:")
            for name in names:
                st.write(name)
        else:
            st.warning(f"No participants found for {query_event}.")


# Search for a participant by name and display their event details.
with tab3:

    st.subheader("Search Participant Details")
    query_name = st.text_input("Enter the name to view the details of the participants")

    if st.button("Confirm details") :
        if query_name :
            row=bd.get_details_by_name(query_name)

            if len(row)!=0 :
                for details in row :
                    st.write("Name   :",details[0])
                    st.write("Contact number :",details[1])
                    st.write("Department :",details[2])
                    st.write("Event :",details[3])
                    st.write("Participation status :",details[4])
                    st.write("---------------------------------------")
            else :
                st.warning(f"No record found for {query_name}.")
        else :
            st.warning("Please enter the name")


# Section 3: Summary of Total Participants
with tab4:
    st.subheader("Event Summary")
    if st.button("Generate Summary"):
        summary = {}
        for event in bd.Events:
            if event != "select":  # Exclude placeholder option
                summary[event] = bd.get_participants_for_event(event)

        if summary:
            st.write("Total participants in each event:")
            for event, participant in summary.items():
                st.write(f"Participants in {event} :-")

                if len(participant)!=0 :
                    for row in participant :
                        st.write(row)
                else :
                    st.write("None")
                st.write("---------------------------------------")
        else:
            st.warning("No participants registered yet.")