import streamlit as st
from textblob import TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity  
    return polarity, subjectivity



st.title("Sentiment Analysis App Using TextBlob")


st.subheader("What is Sentiment Analysis?")
st.write("""
Sentiment analysis is a technique used to determine the emotional tone behind a series of words. 
It helps us understand the attitudes, opinions, and emotions expressed in text data.
""")
st.write("""
Sentiment analysis is utilized across various industries to understand and 
interpret the emotions and opinions expressed in text data. 
It helps businesses gauge customer opinions about products and services, 
enabling them to improve offerings based on feedback. By analyzing sentiment, 
companies can monitor brand reputation, manage crises, and track public opinion in political contexts. Additionally, sentiment analysis provides valuable insights for market research, allowing organizations to adapt strategies based on consumer preferences and trends. In financial markets, it aids in predicting stock movements by assessing market sentiment from news and social media. Overall, sentiment analysis empowers organizations to make data-driven decisions, enhance customer satisfaction, and improve overall performance.
""")

st.subheader("Key Concepts")
st.write("### Polarity")
st.write("""
- **Polarity** refers to the orientation of the sentiment expressed in a piece of text.
- It is measured on a scale from -1 to 1:
  - **-1**: Strongly Negative
  - **0**: Neutral
  - **1**: Strongly Positive
""")

st.write("### Sentiment")
st.write("""
- **Sentiment** categorizes the emotional tone of the text into:
  - **Positive**: Indicates a favorable attitude.
  - **Negative**: Indicates an unfavorable attitude.
  - **Neutral**: Indicates a lack of strong emotion or opinion.
""")

st.write("### Enter the text you want to analyze for sentiment:")


input_text = st.text_area("Input text here")

if st.button("Analyze"):
    if not input_text:
        st.warning("Please enter some text for analysis.")
    else:

        polarity, subjectivity = analyze_sentiment(input_text)


        st.write(f"**Polarity:** {polarity} (Range: -1 to 1)")
        st.write(f"**Subjectivity:** {subjectivity} (Range: 0 to 1)")


        if -0.1 < polarity <= 0.1:
            sentiment = "Neutral"
        elif polarity > 0.1:
            sentiment = "Positive"
        else:
            sentiment = "Negative"

        st.write(f"**Sentiment:** {sentiment}")

