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

streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
