import numpy as np
import streamlit as st
import pickle
import pandas as pd
from PIL import Image



st.set_page_config(page_title="Student Career Prediction", layout="wide", initial_sidebar_state="collapsed")


st.title("Student Career Prediction")

# Define the CSS styles
background = """
    <style>
        body {
            background-image: career2.png;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
        }
    </style>
"""

# Inject the CSS styles
st.write(background, unsafe_allow_html=True)


# Load the image
image = Image.open("career2.png")
resized_image = image.resize((2000, 1000))

# Display the resized image
st.image(resized_image, use_column_width=True)


st.markdown("<style>h1{font-size: 48px;}</style>", unsafe_allow_html=True)

# logo = 'career2.png'
# # st.image(logo, width=200, caption='', use_column_width=True, align='center')
# st.image(logo, width=800)

# import the model
clf = pickle.load(open('clf.pkl','rb'))
dataset = pickle.load(open('dataset.pkl','rb'))
pred = pickle.load(open('xgb_y_pred.pkl','rb'))

# Interface part start

st.markdown("---")
# Academics marks in several subjects
col1, col2 , col3 = st.columns(3)
with col1:
    os = st.number_input('Percentage in Operating Systems')
with col2:
    alg = st.number_input('Percentage in Algorithms')
with col3:
    prog = st.number_input('Percentage in Programming Concepts')



col1, col2, col3 = st.columns(3)
with col1:
    se = st.number_input('Percentage in Software Engineering')
with col2:
    cn = st.number_input('Percentage in computer Networks')
with col3:
    el = st.number_input('Percentage in Electronics')


col1, col2, col3 = st.columns(3)
with col1:
    ca = st.number_input('Percentage in Computer Architecture')
with col2:
    math = st.number_input('Percentage in Mathematics')
with col3:
    comm = st.number_input('Percentage in Communication Skills')

st.markdown("---")



# daily working hours
col1, col2, col3 = st.columns(3)
with col1:
    working_hours = st.selectbox('Hours working per day	...(in Hours)',[1,2,3,4,5,6,7,8,9,10,11,12])
with col2:
    rating_quotient = st.selectbox('Logical quotient rating(Out of 10)',[1,2,3,4,5,6,7,8,9,10])
with col3:
    hackathon = st.selectbox('Hackathons',[1,2,3,4,5,6,7,8,9,10])

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    Coding_skill_Rating = st.selectbox('Coding Skill Rating(Out of 10)',[1,2,3,4,5,6,7,8,9,10])
with col2:
    public_speaking_point = st.selectbox('Public Speaking Point(Out of 10)',[1,2,3,4,5,6,7,8,9,10])

st.markdown("---")


col1, col2, col3 = st.columns(3)
with col1:
    long_time_work = st.radio("can work long time before system?",["Yes","No"])
with col2:
    self_Learning = st.radio("self-learning capability?  ",["Yes","No"])
with col3:
    exrtra_Course = st.radio(" Extra-courses did ",["Yes","No"])

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    Certifications = st.selectbox('Certification do ',['shell programming', 'machine learning', 'app development', 'python', 'r programming', 'information security', 'hadoop', 'distro making','full stack'])
with col2:
    workshop = st.selectbox('Workshops do ',['shell programming', 'machine learning', 'app development', 'python', 'r programming', 'information security', 'hadoop', 'distro making', 'full stack'])

st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    talent_test = st.radio(" Talent test taken ?", ["Yes", "No"])
with col2:
    olympiads = st.radio("Olympiads", ["Yes", "No"])
with col3:
    Reading_writing = st.selectbox('Reading and Writing Skills Score...',['poor', 'medium', 'excellent'])


st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    memory_capability = st.selectbox('Memory Capability Score...', ['poor', 'medium', 'excellent'])
with col2:
    Interested_Subject = st.selectbox('Interested Subject...', ['cloud computing', 'networks', 'hacking', 'Computer Architecture', 'programming', 'parallel computing', 'IOT', 'data engineering', 'Software Engineering', 'Management'])
with col3:
    Interested_career_area = st.selectbox('Interested Career Area...', ['system developer', 'Business process analyst', 'developer', 'testing', 'security', 'cloud computing'])


st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    Job_HigherStudies = st.selectbox('Job/Higher Studies?', ['job', 'Higher studies'])
with col2:
    Type_of_company_want = st.selectbox('Type of company want to settle in? ', ['Web Services', 'SAaS services', 'Sales and Marketing', 'Testing and Maintainance Services',
                                                                            'product development', 'BPA', 'Service Based', 'Product based', 'Cloud Services', 'Finance'])

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    taken_input_from_senior = st.radio("Taken inputs from seniors or elders", ["Yes", "No"])
with col2:
    Interested_games = st.radio("Interested in games...", ['Yes','No'])

st.markdown("---")
# Interested type of Books
col1, col2, col3 = st.columns(3)
with col1:
    interest_book = st.selectbox('Interested type of Books',['Prayer books','childrens','Travel','Romance','Cookbooks','Journals',
                                                         'Drama','Travels','Self help','Math','Religion-Spirituality','Anthology','Trilogy',
                                                         'Autobiographies', 'Mystery', 'Diaries' ,'Journals', 'History' ,'Art',
                                                         'Dictionaries' ,'Horror', 'Encyclopedias' ,'Action and Adventure' ,'Fantasy',
                                                         'Comics' ,'Science fiction' ,'Series', 'Guide', 'Biographies', 'Health',
                                                         'Satire' ,'Science', 'Poetry'
                                                         ])
with col2:
    Salary_or_work = st.selectbox("Expected in Salary / Work...", ['salary','Work'])
with col3:
    In_relation = st.selectbox('In a Relationship 0r Not ?', ['Yes', 'No'])

st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    Gentle_tuff = st.selectbox("Gentle or Tuff behaviour?", ['gentle','stubborn'])
with col2:
    Manage_Tech = st.selectbox("Management or Technical", dataset['Management or Technical'].unique())
with col3:
    salary_work  =  st.selectbox("Salary/work...", ['salary','work'])


st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    hard_smart = st.radio("Hard work /Smart work...", ['hard work', 'smart work'])
with col2:
    worked_in_team = st.radio("worked in teams ever?", ['Yes', 'No'])
with col3:
    Introvert = st.radio("Introvert or Not ? ", ['Yes', 'No'])
st.markdown("---")

# Interface part end


st.write('')
st.write('')
st.write('')

if st.button('Predict'):
    input_df = pd.DataFrame(
     {'Percentage in Operating Systems': os, 'Percentage in Algorithm': alg, 'Percentage in Programming Concepts':[prog], 'Percentage in Software Engineering': [se],'Percentage in Computer Networks ': [cn], 'Percentage in Electronics Subjects': [el], 'Percentage in Computer Architecture': [ca], 'Percentage in Mathematics': [math], 'Percentage in Communication skills': [comm], 'Hour working per day': [working_hours], 'Logical quotient rating': [rating_quotient],
      'Hackathons': [hackathon], 'coding rating skills': [Coding_skill_Rating], 'public speaking points': [public_speaking_point], 'can work long time before system?': [long_time_work], 'self learning capability?': [self_Learning], 'Extra courses did': [exrtra_Course], 'Certifications': [Certifications], 'Workshops': [workshop], 'Talent tests taken ': [talent_test], 'Olympiads': [olympiads], 'reading and writing skills': [Reading_writing],
      'Memory Capability score': [memory_capability], 'Interested Subjects': [Interested_Subject], 'Interested Career area': [Interested_career_area], 'Job/HighStudies': [Job_HigherStudies], 'Type of company want to settle in?': [Type_of_company_want], 'Taken inputs from seniors or elders': [taken_input_from_senior], 'interested in games': [Interested_games], 'Interested Type of Books': [interest_book], 'Salary or Work': [Salary_or_work], 'In a Relationship': [In_relation],
      'Gentle or tuff behaviour': [Gentle_tuff], 'Management or Technical': [Manage_Tech], 'Salary/work': [salary_work], 'Hard/smart worker': [hard_smart], 'Introvert': [Introvert]})
    result = pred.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))


