import json
import os
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from dotenv import load_dotenv
load_dotenv()
import utils
with open('assets/data.json') as file:
    my_info = json.loads(file.read())

with open('assets/Sowmya_Cherukupally_Resume19.pdf', 'rb') as file:
    pdf_data = file.read()




img_weather = Image.open('images/weather.webp')
img_whats_bot = Image.open('images/whats_bot.webp')
img_photo = Image.open('images/img.png')
img_aws = Image.open('images/aws.png')
img_pizza_bot = Image.open('images/pizza_bot.png')

st.set_page_config(page_title='Sowmya Cherukupally', page_icon='😎', layout='wide')
st.markdown(utils.local_css('style/style.css'), unsafe_allow_html=True)

with st.container():
    left, right = st.columns((2, 3), gap='small')

    with right:
        st.subheader(my_info['header'])
        st.title(my_info['title'])
        st.write(my_info['about_me'])

        st.download_button(
            label=" 📄 Download Resume",
            data=pdf_data,
            file_name='Sowmya_Cherukupally_Resume19.pdf',
            mime="application/octet-stream",
        )
    
    with left:
        st.image(img_photo, width=200)

st.write('---')
st.header('Connect with me...')

c1, c2, c3, c4 = st.columns(4)
with st.container():
    c1.write(my_info['github'])
    c4.write(my_info['linkedin'])

with st.container():
    st.write('---')
    interests, annimation = st.columns((2, 3), gap='small')

    with interests:
        st.write(
            '''
            ## My interests are:
            * Chatbot development using WhatsApp , Dialogflow ES
            * Computer Vision
            * Natural Language Processing
            * RESTFul API development Python and Flask
            
            '''
        )

    



with st.container():
    st.write('---')
    st.header('My Projects')
    image, text = st.columns((1, 3), gap='small')

    with image:
        st.image(img_weather)

    with text:
        st.subheader('Weather Application')
        st.write(
            '''
            Weather Application is a weather forecasting application that provides real-time weather information using open weather map API to fetch current details of weather
            * Real time weather updates
            * Forecast Data
            * User friendly interface
            * Location Search
            The code used in this project can be found at my [GitHub repository](https://github.com/sowmya19github/Weather-Application)
            '''
        )


with st.container():
    st.write('---')
    image, text = st.columns((1, 3), gap='small')

    with image:
        st.image(img_whats_bot)

    with text:
        st.subheader('WhatsApp ChatBot')
        st.write(
            '''
            Developed WhatsApp Chatbot which responds to the predefined messages
            * Integrated with a Gupshup API platform to handle the incoming messages
            * Demonstrated proficiency in python for logical implementation
            The code used in this project can be found at my [GitHub repository](https://github.com/sowmya19github/WhatsApp_Chatbot)
            '''
        )
with st.container():
    st.write('---')
    image, text = st.columns((1, 3), gap='small')

    with image:
        st.image(img_aws)

    with text:
        st.subheader('AWS Integration Using Python')
        st.write(
            '''
            AWS integration using Python typically involves using the Boto3 library to programmatically manage AWS services by making API calls for resource creation, management, and automation.
            * Implemented face indexing and image search using rekognition
            * Website hosting using s3
            * Dynamic workflow with s3 bucket to trigger notifications upon image upload
            '''
        )
with st.container():
    st.write('---')
    image, text = st.columns((1, 3), gap='small')

    with image:
        st.image(img_pizza_bot)

    with text:
        st.subheader('Pizza Bot')
        st.write(
            '''
            Created a pizza ordering bot using Dialogflow and Python .
            * Developed an interactive AI chatbot using Dialog Flow (Natural Language Processing)
            * Python to streamline the pizza ordering process 
            * Showcasing NLP and conversational AI capabilities
            '''

        )
        
    


with st.container():
    st.write('---')
    st.header('Get in touch with me...')

    contact_form = f'''
    <form action="https://formsubmit.co/{os.getenv("form_submit")}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    '''

    form, empty = st.columns(2)
    with form:
        st.markdown(contact_form, unsafe_allow_html=True)

