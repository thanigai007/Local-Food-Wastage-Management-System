import streamlit as st
import pandas as pd
import mysql.connector

# DB Connection
def get_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='thanigai@1234',
        database='food_waste_db'
    )

st.set_page_config(page_title="Food Wastage Management", layout="wide")
st.title("🍽️ Local Food Wastage Management System")

menu = st.sidebar.radio("Menu", ["Project Introduction", "View Tables", "CRUD Operations", "SQL Queries & Visualization", "Learner SQL Queries", "About me"])

# Home Page
if menu == "Project Introduction":
    st.markdown("""
        The Local Food Wastage Management System is a digital solution that connects surplus food providers (like restaurants and supermarkets) with receivers (such as NGOs and individuals in need). It aims to reduce local food waste and fight hunger by enabling efficient food donation and claiming.

Key Features:

* Food listing by providers with expiry tracking

* Food claiming by verified receivers

* Dashboards for food type, quantity, and claim status

* CRUD operations for managing providers, receivers, food, and claims

* Analytical queries for user learning and insights

Tech Stack:

* Frontend: Python + Streamlit

* Backend: MySQL

* Libraries: pandas, mysql-connector-python

* Data Analysis: SQL-based queries & dashboards
    """)
# View Tables
elif menu == "View Tables":
    st.subheader("📋 View Database Tables")
    tables = ["providers", "receivers", "food_listings", "claims"]
    selected_table = st.selectbox("Select a table to view", tables)

    conn = get_connection()
    try:
        df = pd.read_sql(f"SELECT * FROM {selected_table}", conn)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error loading table: {e}")
    finally:
        conn.close()

# CRUD Operations
elif menu == "CRUD Operations":
    st.subheader("🛠️ CRUD Operations")
    
    table_choice = st.selectbox("Choose Table", ["food_listings", "providers", "receivers", "claims"])
    crud_option = st.selectbox("Choose Operation", ["Create", "Read", "Update", "Delete"])

    conn = get_connection()
    cursor = conn.cursor()

    if table_choice == "food_listings":
        if crud_option == "Create":
            st.markdown("### ➕ Add New Food Listing")
            food_id = st.number_input("Food ID", min_value=1)
            provider_id = st.number_input("Provider ID", min_value=1)
            Food_name = st.text_input("Food_name")
            food_type = st.text_input("Food Type")
            quantity = st.number_input("Quantity", min_value=1)
            location = st.text_input("Location")
            provider_type = st.text_input("provider_type")
            meal_type = st.text_input("meal_type")
            expiry = st.date_input("Expiry Date")
            if st.button("Add"):
                try:
                    cursor.execute("""
                        INSERT INTO food_listings (food_id, Provider_ID, Food_name, Food_Type, Quantity, Location, provider_type, meal_type, Expiry_Date)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (food_id, provider_id, Food_name, food_type, quantity, location, provider_type, meal_type, expiry,))
                    conn.commit()
                    st.success("Food listing added successfully.")
                except Exception as e:
                    st.error(f"Error: {e}")

        elif crud_option == "Read":
            st.markdown("### 📄 All Food Listings")
            df = pd.read_sql("SELECT * FROM food_listings", conn)
            st.dataframe(df)

        elif crud_option == "Update":
            food_id = st.number_input("Food ID to update", min_value=1)
            column = st.selectbox("Column", ["Food_name", "Food_Type", "Quantity", "Location", "provider_type", "meal_type", "Expiry_Date"])
            value = st.text_input("New Value")
            if st.button("Update"):
                try:
                    cursor.execute(f"UPDATE food_listings SET {column} = %s WHERE Food_ID = %s", (value, food_id))
                    conn.commit()
                    st.success("Updated successfully.")
                except Exception as e:
                    st.error(f"Error: {e}")

        elif crud_option == "Delete":
            food_id = st.number_input("Food ID to delete", min_value=1)
            if st.button("Delete"):
                try:
                    cursor.execute("DELETE FROM food_listings WHERE Food_ID = %s", (food_id,))
                    conn.commit()
                    st.success("Deleted successfully.")
                except Exception as e:
                    st.error(f"Error: {e}")

    elif table_choice == "providers":
        if crud_option == "Create":
            st.markdown("### ➕ Add New Provider")
            name = st.text_input("Name")
            type_ = st.text_input("Type (Restaurant, Grocery Store, etc.)")
            address = st.text_input("Address")
            city = st.text_input("City")
            contact = st.text_input("Contact")
            if st.button("Add"):
                try:
                    cursor.execute("""
                        INSERT INTO providers (Name, Type, Address, City, Contact)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (name, type_, address, city, contact))
                    conn.commit()
                    st.success("Provider added successfully.")
                except Exception as e:
                    st.error(f"Error: {e}")

        elif crud_option == "Read":
            st.markdown("### 📄 All Providers")
            df = pd.read_sql("SELECT * FROM providers", conn)
            st.dataframe(df)

        elif crud_option == "Update":
            provider_id = st.number_input("Provider ID to update", min_value=1)
            column = st.selectbox("Column", ["Name", "Type", "Address", "City", "Contact"])
            value = st.text_input("New Value")
            if st.button("Update"):
                try:
                    cursor.execute(f"UPDATE providers SET {column} = %s WHERE Provider_ID = %s", (value, provider_id))
                    conn.commit()
                    st.success("Updated successfully.")
                except Exception as e:
                    st.error(f"Error: {e}")

        elif crud_option == "Delete":
            provider_id = st.number_input("Provider ID to delete", min_value=1)
            if st.button("Delete"):
                try:
                    cursor.execute("DELETE FROM providers WHERE Provider_ID = %s", (provider_id,))
                    conn.commit()
                    st.success("Deleted successfully.")
                except Exception as e:
                    st.error(f"Error: {e}")


    elif table_choice == "receivers":
        if crud_option == "Create":
            st.markdown("### ➕ Add New Receiver")
            name = st.text_input("Name")
            type_ = st.text_input("Type (NGO, Individual, etc.)")
            city = st.text_input("City")
            contact = st.text_input("Contact")
            if st.button("Add"):
                try:
                    cursor.execute("""
                        INSERT INTO receivers (Name, Type, City, Contact)
                        VALUES (%s, %s, %s, %s)
                    """, (name, type_, city, contact))
                    conn.commit()
                    st.success("Receiver added successfully.")
                except Exception as e:
                    st.error(f"Error: {e}")

        elif crud_option == "Read":
            st.markdown("### 📄 All Receivers")
            df = pd.read_sql("SELECT * FROM receivers", conn)
            st.dataframe(df)

        elif crud_option == "Update":
            receiver_id = st.number_input("Receiver ID to update", min_value=1)
            column = st.selectbox("Column", ["Name", "Type", "City", "Contact"])
            value = st.text_input("New Value")
            if st.button("Update"):
                try:
                    cursor.execute(f"UPDATE receivers SET {column} = %s WHERE Receiver_ID = %s", (value, receiver_id))
                    conn.commit()
                    st.success("Updated successfully.")
                except Exception as e:
                    st.error(f"Error: {e}")

        elif crud_option == "Delete":
            receiver_id = st.number_input("Receiver ID to delete", min_value=1)
            if st.button("Delete"):
                try:
                    cursor.execute("DELETE FROM receivers WHERE Receiver_ID = %s", (receiver_id,))
                    conn.commit()
                    st.success("Deleted successfully.")
                except Exception as e:
                    st.error(f"Error: {e}")
                    
                    
    elif table_choice == "claims":
        if crud_option == "Create":
            st.markdown("### ➕ Create New Claim")
            food_id = st.number_input("Enter Food ID", min_value=1)
            receiver_id = st.number_input("Enter Receiver ID", min_value=1)
            status = st.selectbox("Status", ["Request", "Cancelled"])
            if st.button("Create Claim"):
                try:
                    cursor.execute("""
                        INSERT INTO claims (Food_ID, Receiver_ID, Status, Timestamp)
                        VALUES (%s, %s, %s, NOW())
                    """, (food_id, receiver_id, status))
                    conn.commit()
                    st.success("✅ Claim created successfully!")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

        elif crud_option == "Read":
            st.markdown("### 📄 All Claims")
            try:
                df = pd.read_sql("SELECT * FROM claims", conn)
                st.dataframe(df)
            except Exception as e:
                st.error(f"❌ Error: {e}")

        elif crud_option == "Update":
            st.markdown("### 🔄 Update Existing Claim")
            claim_id = st.number_input("Enter Claim ID to Update", min_value=1)
            new_status = st.selectbox("New Status", ["Pending", "Completed", "Cancelled"])
            if st.button("Update Claim"):
                try:
                    cursor.execute("""
                        UPDATE claims SET Status=%s WHERE Claim_ID=%s
                    """, (new_status, claim_id))
                    conn.commit()
                    if cursor.rowcount > 0:
                        st.success("✅ Claim updated successfully!")
                    else:
                        st.warning("⚠️ No claim found with that ID.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

        elif crud_option == "Delete":
            st.markdown("### 🗑️ Delete Claim")
            claim_id = st.number_input("Enter Claim ID to Delete", min_value=1)
            if st.button("Delete Claim"):
                try:
                    cursor.execute("DELETE FROM claims WHERE Claim_ID=%s", (claim_id,))
                    conn.commit()
                    if cursor.rowcount > 0:
                        st.success("✅ Claim deleted successfully!")
                    else:
                        st.warning("⚠️ No claim found with that ID.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
        
    conn.close()

elif menu == "SQL Queries & Visualization":
    st.subheader("📊 SQL Queries & Visualization")
    
    question = st.selectbox("Select a question to analyze:", [
        "1. Providers & Receivers in each city",
        "2. Top food contributor types",
        "3. Contact info of providers in a specific city",
        "4. Receivers with most food claims",
        "5. Total quantity of food available",
        "6. City with highest food listings",
        "7. Most common food types",
        "8. Claims per food item",
        "9. Provider with most successful claims",
        "10. Percentage of claim statuses",
        "11. Average food claimed per receiver",
        "12. Most claimed meal type",
        "13. Total food donated by each provider"
    ])
    
    conn = get_connection()
    
    if question == "1. Providers & Receivers in each city":
        df1 = pd.read_sql("SELECT City, COUNT(*) AS Provider_Count FROM providers GROUP BY City", conn)
        df2 = pd.read_sql("SELECT City, COUNT(*) AS Receiver_Count FROM receivers GROUP BY City", conn)
        st.write("### Providers per City")
        st.dataframe(df1)
        st.write("### Receivers per City")
        st.dataframe(df2)

    elif question == "2. Top food contributor types":
        df = pd.read_sql("""
            SELECT p.Type, COUNT(f.Food_ID) AS Total_Contributions
            FROM providers p
            JOIN food_listings f ON p.Provider_ID = f.Provider_ID
            GROUP BY p.Type
            ORDER BY Total_Contributions DESC
        """, conn)
        st.bar_chart(df.set_index("Type"))
        st.dataframe(df)

    elif question == "3. Contact info of providers in a specific city":
        city = st.text_input("Enter city name:")
        if city:
            df = pd.read_sql(f"SELECT Name, Contact, Address FROM providers WHERE City = '{city}'", conn)
            st.dataframe(df)

    elif question == "4. Receivers with most food claims":
        df = pd.read_sql("""
            SELECT r.Name, COUNT(c.Claim_ID) AS Total_Claims
            FROM receivers r
            JOIN claims c ON r.Receiver_ID = c.Receiver_ID
            GROUP BY r.Receiver_ID
            ORDER BY Total_Claims DESC
        """, conn)
        st.dataframe(df)

    elif question == "5. Total quantity of food available":
        df = pd.read_sql("""
            SELECT SUM(Quantity) AS Total_Quantity_Available
            FROM food_listings
            WHERE Expiry_Date >= CURDATE()
        """, conn)
        st.dataframe(df)

    elif question == "6. City with highest food listings":
        df = pd.read_sql("""
            SELECT Location AS City, COUNT(*) AS Listings
            FROM food_listings
            GROUP BY Location
            ORDER BY Listings DESC
            LIMIT 1
        """, conn)
        st.dataframe(df)

    elif question == "7. Most common food types":
        df = pd.read_sql("""
            SELECT Food_Type, COUNT(*) AS Frequency
            FROM food_listings
            GROUP BY Food_Type
            ORDER BY Frequency DESC
        """, conn)
        st.bar_chart(df.set_index("Food_Type"))
        st.dataframe(df)

    elif question == "8. Claims per food item":
        df = pd.read_sql("""
            SELECT f.Food_ID, f.Food_Name, COUNT(c.Claim_ID) AS Claim_Count
            FROM food_listings f
            JOIN claims c ON f.Food_ID = c.Food_ID
            GROUP BY f.Food_ID
            ORDER BY Claim_Count DESC
        """, conn)
        st.dataframe(df)

    elif question == "9. Provider with most successful claims":
        df = pd.read_sql("""
            SELECT p.Name, COUNT(c.Claim_ID) AS Successful_Claims
            FROM providers p
            JOIN food_listings f ON p.Provider_ID = f.Provider_ID
            JOIN claims c ON f.Food_ID = c.Food_ID
            WHERE c.Status = 'Completed'
            GROUP BY p.Provider_ID
            ORDER BY Successful_Claims DESC
            LIMIT 1
        """, conn)
        st.dataframe(df)

    elif question == "10. Percentage of claim statuses":
        df = pd.read_sql("""
            SELECT Status, 
                   COUNT(*) AS Count,
                   ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims), 2) AS Percentage
            FROM claims
            GROUP BY Status
        """, conn)
        st.dataframe(df)

    elif question == "11. Average food claimed per receiver":
        df = pd.read_sql("""
            SELECT r.Name, AVG(f.Quantity) AS Avg_Quantity_Claimed
            FROM receivers r
            JOIN claims c ON r.Receiver_ID = c.Receiver_ID
            JOIN food_listings f ON c.Food_ID = f.Food_ID
            GROUP BY r.Receiver_ID
        """, conn)
        st.dataframe(df)

    elif question == "12. Most claimed meal type":
        df = pd.read_sql("""
            SELECT f.Meal_Type, COUNT(c.Claim_ID) AS Claim_Count
            FROM food_listings f
            JOIN claims c ON f.Food_ID = c.Food_ID
            GROUP BY f.Meal_Type
            ORDER BY Claim_Count DESC
        """, conn)
        st.bar_chart(df.set_index("Meal_Type"))
        st.dataframe(df)

    elif question == "13. Total food donated by each provider":
        df = pd.read_sql("""
            SELECT p.Name, SUM(f.Quantity) AS Total_Quantity_Donated
            FROM providers p
            JOIN food_listings f ON p.Provider_ID = f.Provider_ID
            GROUP BY p.Provider_ID
            ORDER BY Total_Quantity_Donated DESC
        """, conn)
        st.dataframe(df)

    conn.close()

# learner sql Queries
elif menu == "Learner SQL Queries":
    st.subheader("📚 Learner SQL-Based Queries")

    query_options = [
        "1. Number of food providers and receivers in each city",
        "2. Provider type contributing the most food",
        "3. Contact info of food providers in a specific city",
        "4. Receivers with most food claims",
        "5. Total quantity of food available",
        "6. City with highest number of food listings",
        "7. Most commonly available food types",
        "8. Number of claims per food item",
        "9. Provider with most successful claims",
        "10. Claim status distribution",
        "11. Average quantity claimed per receiver",
        "12. Most claimed meal type",
        "13. Total quantity donated by each provider",
        "14. Average time between listing and claim per food type"
        
    ]

    selected_query = st.selectbox("Select a question to analyze:", query_options)

    conn = get_connection()

    if selected_query == query_options[0]:
        df = pd.read_sql("""
            SELECT p.City,
                   COUNT(DISTINCT p.Provider_ID) AS Providers,
                   (SELECT COUNT(*) FROM receivers r WHERE r.City = p.City) AS Receivers
            FROM providers p
            GROUP BY p.City;
        """, conn)

    elif selected_query == query_options[1]:
        df = pd.read_sql("""
            SELECT Provider_Type, COUNT(*) AS Total_Contributions
            FROM food_listings
            GROUP BY Provider_Type
            ORDER BY Total_Contributions DESC;
        """, conn)

    elif selected_query == query_options[2]:
        city = st.text_input("Enter City Name")
        if city:
            df = pd.read_sql(f"""
                SELECT Name, Contact FROM providers WHERE City = '{city}'
            """, conn)
        else:
            df = pd.DataFrame()

    elif selected_query == query_options[3]:
        df = pd.read_sql("""
            SELECT r.Name, COUNT(c.Claim_ID) AS Total_Claims
            FROM receivers r
            JOIN claims c ON r.Receiver_ID = c.Receiver_ID
            GROUP BY r.Name
            ORDER BY Total_Claims DESC;
        """, conn)

    elif selected_query == query_options[4]:
        df = pd.read_sql("""
            SELECT SUM(Quantity) AS Total_Quantity FROM food_listings;
        """, conn)

    elif selected_query == query_options[5]:
        df = pd.read_sql("""
            SELECT Location AS City, COUNT(*) AS Listings
            FROM food_listings
            GROUP BY Location
            ORDER BY Listings DESC;
        """, conn)

    elif selected_query == query_options[6]:
        df = pd.read_sql("""
            SELECT Food_Type, COUNT(*) AS Frequency
            FROM food_listings
            GROUP BY Food_Type
            ORDER BY Frequency DESC;
        """, conn)

    elif selected_query == query_options[7]:
        df = pd.read_sql("""
            SELECT f.Food_Name, COUNT(c.Claim_ID) AS Total_Claims
            FROM food_listings f
            JOIN claims c ON f.Food_ID = c.Food_ID
            GROUP BY f.Food_Name
            ORDER BY Total_Claims DESC;
        """, conn)

    elif selected_query == query_options[8]:
        df = pd.read_sql("""
            SELECT p.Name, COUNT(c.Claim_ID) AS Successful_Claims
            FROM providers p
            JOIN food_listings f ON p.Provider_ID = f.Provider_ID
            JOIN claims c ON f.Food_ID = c.Food_ID
            WHERE c.Status = 'Completed'
            GROUP BY p.Name
            ORDER BY Successful_Claims DESC;
        """, conn)

    elif selected_query == query_options[9]:
        df = pd.read_sql("""
            SELECT Status, COUNT(*) AS Count
            FROM claims
            GROUP BY Status;
        """, conn)

    elif selected_query == query_options[10]:
        df = pd.read_sql("""
            SELECT r.Name, AVG(f.Quantity) AS Avg_Quantity
            FROM receivers r
            JOIN claims c ON r.Receiver_ID = c.Receiver_ID
            JOIN food_listings f ON f.Food_ID = c.Food_ID
            GROUP BY r.Name;
        """, conn)

    elif selected_query == query_options[11]:
        df = pd.read_sql("""
            SELECT Meal_Type, COUNT(*) AS Total_Claims
            FROM food_listings f
            JOIN claims c ON f.Food_ID = c.Food_ID
            GROUP BY Meal_Type
            ORDER BY Total_Claims DESC;
        """, conn)

    elif selected_query == query_options[12]:
        df = pd.read_sql("""
            SELECT p.Name, SUM(f.Quantity) AS Total_Quantity
            FROM providers p
            JOIN food_listings f ON p.Provider_ID = f.Provider_ID
            GROUP BY p.Name
            ORDER BY Total_Quantity DESC;
        """, conn)

    elif selected_query == query_options[13]:
        df = pd.read_sql("""
            SELECT fl.Food_Type,
                   ROUND(AVG(TIMESTAMPDIFF(HOUR, fl.Expiry_Date, c.Timestamp)), 2) AS Avg_Hours_To_Claim
            FROM food_listings fl
            JOIN claims c ON fl.Food_ID = c.Food_ID
            WHERE c.Status = 'Completed'
            GROUP BY fl.Food_Type;
        """, conn)

    else:
        df = pd.DataFrame()

    if not df.empty:
        st.dataframe(df)
    else:
        st.info("No data found or query not selected.")

    conn.close()
# About me
if menu == "About me":
    st.subheader("A little about me")
    st.markdown("""
        I'm Thanigai Kumar K V, currently pursuing my Master's in Information Technology at VELS University. I have a strong interest in software development. My skills include programming in Python,database, as well as experience with web development. I'm passionate about applying IT solutions to real-world challenges and continuously expanding my technical expertise.
    """)
