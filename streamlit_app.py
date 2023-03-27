
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import urlerror


streamlit.title('my parents new healty dinner')
streamlit.header('breakfast menu')
streamlit.text('🥣  Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 avocada toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe( my_fruit_list)

#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
 #my_fruit_list = my_fruit_list.set_index('Fruit')
 #streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avacoda','Strawberry'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]


 #function create
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
# write your own comment - what does this do?
# Display the table on the page.
streamlit.header('fruityvice fruit advice')
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
           streamlit.error("please select the fruit to get the infoemation.")
#streamlit.write('The user entered ', fruit_choice)
    else:
        back_from_function=get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)

#except URLERROR as e:
 #streamlit.error()

    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    my_cur.execute("insert into fruit_load_list values('from streamlit')")
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
   my_data_row = my_cur.fetchall()
   streamlit.header("MY FRUITLIST CONTAIN:")
#streamlit.text("Hello from Snowflake:")
   streamlit.dataframe(my_data_row)
