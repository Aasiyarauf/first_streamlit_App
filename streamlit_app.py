import streamlit
import pandas
import requests
#import snowflake.connector
#from urllib.error import urlerror


streamlit.title('my parents new healty dinner')
streamlit.header('breakfast menu')
streamlit.text('🥣  Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 avocada toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
 streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
 #my_fruit_list = my_fruit_list.set_index('Fruit')
 streamlit.dataframe(my_fruit_list)


#fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avacoda','Strawberry'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(fruits_to_show)

   
streamlit.header("fruityvice fruit advice")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

