import streamlit as st
import backend as bd

st.title("ONLINE FOOD DELIVERY SYSTEM")

tabs = st.tabs(["Menu", "Place Order", "Total Revenue", "Unique Customers"])

with tabs[0] :
    menu=bd.fetch_menu()

    st.write("### Menu")
    for item in menu:
        st.write(f"{item['item_name']} - ${item['price']} ({item['category']})")

with tabs[1] :

    name=st.text_input("Enter your Name ")
    item_selection=st.multiselect("Select items ", [item['item_name'] for item in menu])
    
    if item_selection:
        # Calculate total bill
        total = sum(item['price'] for item in menu if item['item_name'] in item_selection)
        st.write(f"### Total Bill: ${total:.2f}")
        
        # Place an order
        if st.button("Place Order"):
            if name and item_selection:
                bd.place_order(name,item_selection,total)
                st.success(f"Order placed successfully for {name}!")
            else:
                st.error("Please fill in all the details.")

with tabs[2]:
    
    # Fetch total revenue
    revenue=bd.total_order_revenue()
    st.write(f"### Total Revenue: ${revenue:.2f}")

with tabs[3] :
    st.header("Customers")

    customers=bd.unique_customers()

    if customers :
        for name in customers :
            st.write(name)
    else :
        st.warning("No customers are there")