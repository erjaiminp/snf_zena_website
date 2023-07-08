import streamlit
import pandas
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()
df = pandas.DataFrame(my_catalog)
# temp write the dataframe to the page so I Can see what I am working with
streamlit.write(df)
# put the first column into a list


