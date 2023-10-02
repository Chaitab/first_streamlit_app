import streamlit
streamlit.title('My Restaurant new healthy diner')

streamlit.header('Lunch Favourites')
streamlit.title('🥣 Fhalakurra fhappu')
streamlit.title('🥗 Kakarkaya Karam')
streamlit.title('🥑 Vankaya Pulusu')
streamlit.title('🍞 Majjiga Charu')

streamlit.header('🍌🥭 Build Your Own fruit smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
