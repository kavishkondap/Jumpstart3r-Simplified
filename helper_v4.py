import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import base64
from tensorflow import keras
from datetime import date


category_success_rate = {
    'Games':46.69,
    'Design':41.62,
    "Technology":22.45,
    "Film & Video":38.09,
    "Video":38.09,
    "Publishing":36.54,
    "Music":50.38,
    "Fashion":30.60,
    "Food":26.01,
    "Comics":64.82,
    "Art":48.00,
    "Photography":34.53,
    "Theater":59.96,
    "Crafts":26.91,
    "Journalism":23.34,
    "Dance":61.48,
}

curr_converter = {
    "USD":1,
    "NOK":0.099941,
    "AUD":0.676713,
    "EUR":1.041681,
    "MXN":0.051733,
    "HKD":0.127806,
    "GBP":1.18572,
    "SEK":0.095841,
    "CAD":0.750236,
    "DKK":0.13964,
    "NZD":0.615895,
    "SGD":0.729794,
    "CHF":1.060335,
    "JPY":0.007171,
    "PLN":0.221287
}


def numCapitals (input):
    numCapitals = 0
    for i in range (len (input)):
        if (input[i].isupper()):
            numCapitals+=1
    return numCapitals
def numNums (input):
    numNum = 0
    for i in range (len (input)):
        if (input[i].isnumeric ()):
            numNum+=1
    return numNum

def numExc (input):
    numExc = 0
    for i in range (len (input)):
        if (input[i]=='!'):
            numExc+=1
    return numExc

def strToInt (strng):
    if (strng == 'Image'):
        return 1
    else:
        return 2

def data_processing (title, blurb, media, goal, currency_used, num_days, num_creation_days, category, updates):
    data = []
    currency_used_num = curr_converter[currency_used]
    data.append (goal*currency_used_num)
    data.append (currency_used_num)
    data.append (strToInt (media))
    data.append (category_success_rate [category])
    data.append (num_days)
    data.append (num_creation_days)
    data.append (updates)
    data.append (len (title))
    data.append (len (blurb))
    data.append (numCapitals (title))
    data.append (numCapitals (blurb))
    data.append (numNums (title))
    data.append (numNums (blurb))
    data.append (numExc (title))
    data.append (numExc (blurb))
    return np.array (data)


def successBreakdown ():
    data = pd.read_excel ("machineLearningData5.xlsx")
    num_successful = 0
    num_failed = 0
    for i in data['successes']:
        if i ==1:
            num_successful+=1
        else:
            num_failed+=1
    labels = 'Successful', 'Failed'
    sizes = [num_successful, num_failed]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',startangle=90)
    ax1.axis('equal')
    return fig1


@st.cache (allow_output_mutation=True)
def load_model (model_name):
    model = keras.models.load_model (model_name)
    return model

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


def title_section ():
    col1, col2, col3 = st.columns([1, 6, 1])
    col2.image ('ai-logo.webp', use_column_width=True)

def numbers_section():
    col1, col2, col3 = st.columns (3)
    # col2.image ('mag_glass USE THIS ONE.webp', use_column_width=True)
    col1.markdown ("<h1 style='text-align: center; color: #f1961a;'>30,000</h1>", unsafe_allow_html=True)
    col1.markdown ("<h4 style='text-align: center; color: #f1961a;'>Websites Analyzed</h4>", unsafe_allow_html=True)
    # col5.image ('cross-hatch USE THIS ONE.webp', use_column_width=True)
    col2.markdown ("<h1 style='text-align: center; color: #f1961a;'>96%</h1>", unsafe_allow_html=True)
    col2.markdown ("<h4 style='text-align: center; color: #f1961a;'>Accuracy</h4>", unsafe_allow_html=True)
    # col8.image ('dots USE THIS ONE.webp', use_column_width=True)
    col3.markdown ("<h1 style='text-align: center; color: #f1961a;'>9</h1>", unsafe_allow_html=True)
    col3.markdown ("<h4 style='text-align: center; color: #f1961a;'>Data Inputs</h4>", unsafe_allow_html=True)

def about_section():
    #image
    col1, col2, col3 = st.columns([2, 6, 2])
    col2.image ('about project.webp', use_column_width=True)
    col1, col2 = st.columns(2)
    col2.markdown ("<h1 style='color: #f1961a;'>Entrepreneurship is <FONT COLOR='#ffffff'>hard</FONT><br>But it doesn't have to be</h1>", unsafe_allow_html=True)
    col2.markdown ("<h5 style='color: #f1961a; line-height: 1.75;'>Jumpstart3r uses deep learning machine learning techniques to predict the success of Kickstarter campaigns. By analyzing data from past campaigns, we are able to provide valuable insights to creators looking to launch their own projects. All you have to do is provide a few details about your Kickstarter campaign, and we will output a prediction within seconds. This project was executed using a large dataset of Kickstarter projects to train an accurate model. Although public Kickstarter datasets do exist, I found them to lack size, or metrics I wanted to use for my model, and thus collected my own data. Kickstarter campaigns were scraped using a Python script and the BeautifulSoup library, and a total of over six million identifying data points were used to train the machine learning model, one of the largest Kickstarter datasets in the world.</h5>", unsafe_allow_html=True)
    col1.image ('business.webp', use_column_width=True)
    
    # st.markdown ("Hi! Thanks for checking out my website.")
    # st.markdown ("Jumpstart3r was made to help entrepreneurs with their crowdfunding campaigns, and uses a deep learning machine learning algorithm to predict the success of a project. But, before it can do that, you'll have to provide it with some more information about your project, allowing it to accurately predict the likelihood of your campaign's success.")
    
    # st.markdown ("This project was executed using a large dataset of Kickstarter projects to train an accurate model. Although public Kickstarter datasets do exist, I found them to lack size, or metrics I wanted to use for my model, and thus collected my own data. Kickstarter campaigns were scraped using a Python script and the BeautifulSoup library, and a total of over six million identifying data points were used to train the machine learning model, one of the largest Kickstarter datasets in the world. ")

    # return None

def mission_section():
    col1, col2, col3 = st.columns([2, 6, 2])
    col2.image ('mission3.webp', use_column_width=True)
    col1, col2= st.columns([9, 3])
    col2.image ('target.webp',  use_column_width=True)
    col1.markdown ("<h2 style='color: #f1961a;'>Jumpstart3r's mission is to <FONT COLOR='#ffffff'>empower</FONT COLOR> creators by providing them with the tools and information they need to successfully launch their Kickstarter campaigns. By leveraging the power of machine learning, Jumpstart3r strives to make the crowdfunding process more <FONT COLOR='#ffffff'>efficient</FONT COLOR> and <FONT COLOR='#ffffff'>effective</FONT COLOR> for both creators and backers.", unsafe_allow_html=True)
    # col1.info ("<h3 style='color: #f1961a;'>Our mission is to empower creators by providing them with the tools and information they need to successfully launch their Kickstarter campaigns. By leveraging the power of machine learning, we strive to make the crowdfunding process more efficient and effective for both creators and backers.</h3>", unsafe_allow_html=True)

def ml_section():
    col1, col2, col3 = st.columns([2, 6, 2])
    col2.image ('machine learning.webp', use_column_width=True)
    #<h4 style='text-align: center;'>
    st.markdown ("<p style='font-size: 20px; color: #f1961a;'>Before we can make a prediction about your Kickstarter campaign, we need some more information on your project! Input the details for your campaign below, and click the \"Predict\" button to run the model and get a prediction. Play around with your inputs to see what yields the best result. It's all free. Forever.</p>", unsafe_allow_html=True)
    st.markdown ("<p style='font-size: 20px; color: #f1961a;'>A few things to keep in mind:</p>", unsafe_allow_html=True)
    tab3_col1, tab3_col2= st.columns([0.01, 20])
    tab3_col2.markdown ("<p style='font-size: 20px; color: #f1961a;'>1. <strong>Expectations</strong>: This is a machine learning model, not a fortune teller! The artificial intelligence algorithm was trained with REAL data from past Kickstarter campaigns (nearly 30,000 of them, in fact), so it's calibrated to predict the outcome of a realistic project. Providing the model with unrealistic data will yield unrealistic results.</p>", unsafe_allow_html=True)
    tab3_col2.markdown ("<p style='font-size: 20px; color: #f1961a;'>2. <strong>Accuracy</strong>: Jumpstart3r has an accuracy at about 96%, meaning it's pretty accurate—the most accurate Kickstarter predictor in the world, actually! That doesn't mean it's perfect though, and always remember that there are other, unpredictable factors that affect the outcome of your campaign.</p>", unsafe_allow_html=True)
    tab3_col2.markdown ("<p style='font-size: 20px; color: #f1961a;'>3. <strong>Privacy</strong>: Jumpstart3r is a secure platform, and NONE of the data you input is ever uploaded to the cloud or saved. The magic all happens in your browser.</p>", unsafe_allow_html=True)

    with st.form("my_form"):
        col1, col2, col3 = st.columns(3)
        title = col1.text_input ("Title", help='The title of your Kickstarter campaign')
        blurb = col2.text_input ("Blurb", help = "The brief description of your Kickstarter campaign")
        media = col3.selectbox ("Select Media Type", ("Image", "Video"), help = "The type of media you will have present on your website; if both, choose video")
        goal = col1.number_input ("Goal", min_value=0, step=1, help = "Your fundraising goal, in the currency of your campaign")
        currency_used = col2.selectbox ("Currency Used", ("USD","NOK","AUD","EUR","MXN","HKD","GBP","SEK","CAD","DKK","NZD","SGD","CHF","JPY","PLN"), help='The currency your campaign utilizes')
        num_days = col3.number_input ("Project Duration (Days)", min_value=0, step=1, help = 'How long your campaign will last, in days')
        num_creation_days = col1.number_input ("Project Worktime", min_value=0, step=1, help='The amount of time between when you first created your project and when you plan on launching it, in days')
        category = col2.selectbox ('Category', (
            'Games',
            'Design',
            "Technology",
            "Film & Video",
            "Publishing",
            "Music",
            "Fashion",
            "Food",
            "Comics",
            "Art",
            "Photography",
            "Theater",
            "Crafts",
            "Journalism",
            "Dance"), help = 'The Kickstarter category that your campaign falls under')
        updates = col3.number_input  ("Updates", min_value=0, step=1, help='How many updates you plan on providing on your campaign page throughout its duration')
        # Every form must have a submit button.
        submitted = st.form_submit_button("Predict")
        if submitted:
            model = load_model ("NN_v9")

            input = data_processing (title, blurb, media, goal, currency_used, num_days, num_creation_days, category, updates)
            output = model.predict (input)
            prediction_text = "Likelihood of Success: "

            st.markdown("<h2 style='text-align: center; color: #f1961a;'>" + prediction_text + "</h2>", unsafe_allow_html=True)
            st.markdown ("<h1 style='text-align: center; color: #f1961a;'>" +  str (np.round (output[0][0]*100, 2)) + "%" + "</h1>", unsafe_allow_html=True)

def data_section ():
    
    col1, col2, col3 = st.columns([2, 6, 2])
    col2.image ('data_breakdown.webp', use_column_width=True)
    st.markdown("""
    <style>
    .big-font {
        font-size:300px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown ("<p style='font-size: 20px; color: #f1961a;'>Below is some more information on the dataset collected, and the makeup of the Kickstarter projects sampled for the model. First is a distribution of the successful projects vs. unsuccessful projects that were part of the ~30,000 websites analyzed.", unsafe_allow_html=True)
    tab3_col1, tab3_col2 = st.columns([0.05, 20])
    tab3_col2.markdown ("<p style='font-size: 20px; color: #f1961a;'>- 62.9% of Websites Successful, 37.1% of Websites Failed", unsafe_allow_html=True)
    # image = Image.open()
    st.markdown ("<p style='font-size: 20px; color: #f1961a;'>Next is a distribution of success for projects that had a video present on their webpage. Note that these percentages should be compared relative to the above data.", unsafe_allow_html=True)
    tab3_col1, tab3_col2 = st.columns([0.05, 20])
    tab3_col2.markdown ("<p style='font-size: 20px; color: #f1961a;'>- 70.2% of Websites Successful, 29.8% of Websites Failed", unsafe_allow_html=True)
    # image = Image.open()
    st.markdown ("<p style='font-size: 20px; color: #f1961a;'>Below is a distribution of success for projects that solely had one or multiple images present on their webpage, rather than a video:", unsafe_allow_html=True)
    # image = Image.open()
    tab3_col1, tab3_col2 = st.columns([0.05, 20])
    tab3_col2.markdown ("<p style='font-size: 20px; color: #f1961a;'>- 47.3% of Websites Successful, 52.7% of Websites Failed", unsafe_allow_html=True)
    st.markdown ("<p style='font-size: 20px; color: #f1961a;'>Finally, quantitative statistics about a few of the metrics being analyzed are provided here:", unsafe_allow_html=True)
    
    col1, col2 = st.columns (2)
    col1.markdown ("<p style='font-size: 20px; color: #f1961a;'><br>Fundraising Goal (in USD)", unsafe_allow_html=True)
    col1.markdown ("<pre><p style='font-size: 20px; color: #f1961a;'>&emsp;1. Overall Average: 39,311.60", unsafe_allow_html=True)
    col1.markdown ("<pre><p style='font-size: 20px; color: #f1961a;'>&emsp;2. Successful Campaign Average: 8,673.09, Successful Campaign Standard Deviation: 25,220.63", unsafe_allow_html=True)
    col1.markdown ("<pre><p style='font-size: 20px; color: #f1961a;'>&emsp;3. Failed Campaign Average: 91,350.94, Failed Campaign Standard Deviation: 2,135,599.16<br><br><br>Project Worktime", unsafe_allow_html=True)

    col2.markdown ("<p style='font-size: 20px; color: #f1961a;'><br>Project Duration", unsafe_allow_html=True)
    col2.markdown ("<pre><p style='font-size: 20px; color: #f1961a;'>&emsp;1. Overall Average: 32.76", unsafe_allow_html=True)
    col2.markdown ("<pre><p style='font-size: 20px; color: #f1961a;'>&emsp;2. Successful Campaign Average: 31.20, Successful Campaign Standard Deviation: 11.07", unsafe_allow_html=True)
    col2.markdown ("<pre><p style='font-size: 20px; color: #f1961a;'>&emsp;3. Failed Campaign Average: 35.41, Failed Campaign Standard Deviation: 13.26<br><br><br>Number of Updates", unsafe_allow_html=True)

    # col1.markdown ("<p style='font-size: 20px;'>Project Worktime", unsafe_allow_html=True)
    col1.markdown ("<pre><p style='font-size: 20px; color: #f1961a;'>&emsp;1. Overall Average: 49.38", unsafe_allow_html=True)
    col1.markdown ("<pre><p style='font-size: 20px; color: #f1961a;'>&emsp;2. Successful Campaign Average: 53.42, Successful Campaign Standard Deviation: 141.78", unsafe_allow_html=True)
    col1.markdown ("<pre><p style='font-size: 20px; color: #f1961a;'>&emsp;3. Failed Campaign Average: 42.50, Failed Campaign Standard Deviation: 134.25", unsafe_allow_html=True)

    # col2.markdown ("<p style='font-size: 20px;'>Number of Updates", unsafe_allow_html=True)
    col2.markdown ("<pre><p style='font-size: 20px; color: #f1961a;'>&emsp;1. Overall Average: 7.13", unsafe_allow_html=True)
    col2.markdown ("<pre><p style='font-size: 20px; color: #f1961a;'>&emsp;2. Successful Campaign Average: 10.71, Successful Campaign Standard Deviation: 11.67", unsafe_allow_html=True)
    col2.markdown ("<pre><p style='font-size: 20px; color: #f1961a;'>&emsp;3. Failed Campaign Average: 1.05, Failed Campaign Standard Deviation: 2.68", unsafe_allow_html=True)

def footer_section():
    st.markdown ('<br><br><br><br><br>', unsafe_allow_html=True)
    todays_date = date.today()
    year = todays_date.year
    copyright_text = "<p style='text-align: center; color: #f1961a;'>© " + str(year) + " Jumpstart3r. All Rights Reserved.</p>"
    col1, col2, col3 = st.columns (3)
    col2.markdown (copyright_text, unsafe_allow_html=True)



# def footer_section ():
#     footer="""<style>
#     a:link , a:visited{
#     color: blue;
#     background-color: transparent;
#     text-decoration: underline;
#     }

#     a:hover,  a:active {
#     color: red;
#     background-color: transparent;
#     text-decoration: underline;
#     }

#     .footer {
#     position: fixed;
#     left: 0;
#     bottom: 0;
#     width: 100%;
#     background-color: white;
#     color: black;
#     text-align: center;
#     }
#     </style>
#     © 2023 Jumpstart3r. All Rights Reserved.
#     """
#     st.markdown(footer,unsafe_allow_html=True)

# from streamlit.components.v1 import html
# from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
# from htbuilder.units import percent, px
# from htbuilder.funcs import rgba, rgb

# def image(src_as_string, **style):
#     return img(src=src_as_string, style=styles(**style))


# def link(link, text, **style):
#     return a(_href=link, _target="_blank", style=styles(**style))(text)


# def layout(*args):
#     style = """
#     <style>
#       # MainMenu {visibility: hidden;}
#       footer {visibility: hidden;}
#      .stApp { bottom: 40px; }
#     </style>
#     """

#     style_div = styles(
#         position="fixed",
#         left=0,
#         bottom=0,
#         margin=px(0, 0, 0, 0),
#         width=percent(100),
#         color="black",
#         text_align="center",
#         height="auto",
#         opacity=1
#     )

#     # 分割线
#     style_hr = styles(
#         display="block",
#         margin=px(0, 0, 0, 0),
#         border_style="inset",
#         border_width=px(2)
#     )

#     # 修改p标签内文字的style
#     body = p(
#         id='myFooter',
#         style=styles(
#             margin=px(0, 0, 0, 0),
#             # 通过调整padding自行调整上下边距以达到满意效果
#             padding=px(5),
#             # 调整字体大小
#             font_size="0.8rem",
#             color="rgb(51,51,51)"
#         )
#     )
#     foot = div(
#         style=style_div
#     )(
#         hr(
#             style=style_hr
#         ),
#         body
#     )

#     st.markdown(style, unsafe_allow_html=True)

#     for arg in args:
#         if isinstance(arg, str):
#             body(arg)

#         elif isinstance(arg, HtmlElement):
#             body(arg)

#     st.markdown(str(foot), unsafe_allow_html=True)

#     # js获取背景色 由于st.markdown的html实际上存在于iframe, 所以js检索的时候需要window.parent跳出到父页面
#     # 使用getComputedStyle获取所有stApp的所有样式，从中选择bgcolor
#     js_code = '''
#     <script>
#     function rgbReverse(rgb){
#         var r = rgb[0]*0.299;
#         var g = rgb[1]*0.587;
#         var b = rgb[2]*0.114;
        
#         if ((r + g + b)/255 > 0.5){
#             return "rgb(49, 51, 63)"
#         }else{
#             return "rgb(250, 250, 250)"
#         }
        
#     };
#     var stApp_css = window.parent.document.querySelector("#root > div:nth-child(1) > div > div > div");
#     window.onload = function () {
#         var mutationObserver = new MutationObserver(function(mutations) {
#                 mutations.forEach(function(mutation) {
#                     /************************当DOM元素发送改变时执行的函数体***********************/
#                     var bgColor = window.getComputedStyle(stApp_css).backgroundColor.replace("rgb(", "").replace(")", "").split(", ");
#                     var fontColor = rgbReverse(bgColor);
#                     var pTag = window.parent.document.getElementById("myFooter");
#                     pTag.style.color = fontColor;
#                     /*********************函数体结束*****************************/
#                 });
#             });
            
#             /**Element**/
#             mutationObserver.observe(stApp_css, {
#                 attributes: true,
#                 characterData: true,
#                 childList: true,
#                 subtree: true,
#                 attributeOldValue: true,
#                 characterDataOldValue: true
#             });
#     }
    

#     </script>
#     '''
#     html(js_code)


# def footer():
#     # use relative path to show my png instead of url
#     ######
#     with open('logo5.png', 'rb') as f:
#         img_logo = f.read()
#     logo_cache = st.image(img_logo)
#     logo_cache.empty()
#     ######
#     myargs = [
#         "沪ICP备2077777777号-1	Made in ",
#         image('logo5.png',
#               width=px(25), height=px(25)),
#         " with ❤️ by ",
#         link("https://www.zhihu.com/people/Gu.meng.old-dream", "@wangnov"),
#     ]
#     layout(*myargs)