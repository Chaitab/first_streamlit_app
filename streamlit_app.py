import streamlit
streamlit.title('My Restaurant new healthy diner')

streamlit.header('Lunch Favourites')

streamlit.title('🥣 Fhalakurra fhaffu')
streamlit.title('🥗 Kakarkaya Karam')
streamlit.title('🥑 Vankaya Pulusu')
streamlit.title('🍞 Majjiga Charu')

streamlit.header('🍌🥭 Build Your Own fruit smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.dataframe(fruits_to_show)

# New section to display Fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# Removed this code --streamlit.text(fruityvice_response.json()) #just writes data to the screen

#take the json verson of response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
Add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', Add_my_fruit)

# This will not work correctly. But go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
