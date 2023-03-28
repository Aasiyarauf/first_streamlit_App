import streamlit
import pandas
import snowflake.connector
#from urllib.error import URLERROR


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

#create repetable block
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized



#new section to display Api responsede
streamlit.header("fruityvice fruit advice")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
          streamlit.error("please select the fruit to get information")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
 


streamlit.header("The fruit list contain:")
#snoflake related function
def get_fruit_load_list():
    with  my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
    
 #add button to load the fruits
if streamlit.button("get fruit load list"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=get_fruit_load_list()
   # my_cnx.close()
    streamlit.dataframe(my_data_rows)

#allow the ned user to add the fruit
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur_execute("insert into fruit load list values('from streamlit')")
        return "thanks for adding"+new_fruit
    
add_my_fruit = streamlit.text_input('What would you like to add')
if streamlit.button('add fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_From_function=insert_row_snowflake(add_my_fruit)
    streamlit.text( back_From_function)
    
