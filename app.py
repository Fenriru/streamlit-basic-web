#  pipenv run streamlit run app.py

import streamlit as st

st.title("Streamlit Basics")

st.text("This is a simple text")

st.write("This is a write dimension")

st.markdown("[Streamlit](https://www.streamlit.io)")

st.markdown("https://www.streamlit.io")

html_page = """
<div style="background-color:blue;padding:50px">
<p style="color:yellow;font-size:50px">Enjoy Streamlit!</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

st.success("Success!")
st.info("Information")
st.warning("This is a warning!")
st.error("This is an error!")

from PIL import Image
img = Image.open("st_image_ex.jpg")
st.image(img, width=300, caption="Some Logo")

# video_file = open("Invincible.S03E08.1080p.AMZN.WEB-DL.DDP5.1.H.264-PrimeFix.mkv","rb")

video_file = open("InvincibleS0EF.m4v", "rb")

video_bytes = video_file.read()

st.video(video_bytes)

st.video("https://www.youtube.com/watch?v=q2EqJW8VzJo")

audio_file = open("Espresso.mp3", "rb")

audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/mp3")

# st.button("Play")

if st.button("Play"):
      st.text("Hello world!")


radio_but = st.radio("Your Selection", ["A", "B"])

if radio_but == "A":
      st.info("You selected A")
else:
      st.info("You selected B")

city = st.selectbox("Your City", ["Napoli", "Palermo", "Catania"])


occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "IT Consultant", "DBA"])


Name = st.text_input("Your Name", "Write something…")

st.text(Name)

Age = st.number_input("Input a number")


message = st.text_area("Your Message", "Write something...")

select_val = st.slider("Select a Value", 1, 10)


if st.button("Balloons"):
      st.balloons()

st.header("Dataframes and Tables")
import pandas as pd
df = pd.read_csv("auto.csv")
st.dataframe(df.head(10))

st.table(df.head(10))

st.area_chart(df[["mpg","cylinders"]])


st.bar_chart(df[["mpg","cylinders"]].head(20))

st.line_chart(df[["mpg","cylinders"]].head(20))

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
corr_plot = sns.heatmap(df[["mpg","cylinders", "displacement"]].corr(), annot= True)
st.pyplot(fig)

import datetime
today = st.date_input("Today is",datetime.datetime.now())

import time
hour = st.time_input("The time is",datetime.time(12,30))

data = {"name":"John","surname":"Wick"}
st.json(data)

st.code("import pandas as pd")

julia_code = """
function doit(num::int)
      println(num)
end
"""
st.code(julia_code, language='julia')

import time
my_bar = st.progress(0)
for value in range(100):
      time.sleep(0.1)
      my_bar.progress(value+1)

import time
with st.spinner("Please wait..."):
      time.sleep(10)
st.success("Done!")