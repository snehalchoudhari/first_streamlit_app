import streamlit
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

#frutis_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado'])
#fruits_to_show = my_fruit_list[frutis_selected]
#streamlit.dataframe(fruits_to_show)
