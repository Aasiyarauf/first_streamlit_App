import streamlit
import pandas
import snowflake.connector
from urllib.error import URLERROR


streamlit.title('my parents new healty dinner')
streamlit.header('breakfast menu')
streamlit.text('🥣  Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 avocada toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avacoda','Strawberry'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(my_fruit_list)

streamlit.header("fruityvice fruit advice")
try:
fruit_choice = streamlit.text_input('What fruit would you like information about?')
     if not fruit_choice:
          streamlit.error("please select the fruit to get information")
     else:
          fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
          fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
          streamlit.dataframe(fruityvice_normalized)
 
except URLERROR as e
      streamlit.error()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit list contain:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What would you like to add','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
