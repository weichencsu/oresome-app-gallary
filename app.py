import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth


st.set_page_config(page_title='Oresome App Gallary Login System',
                   layout='centered', initial_sidebar_state='auto')

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Oresome App Gallary Login System', 'main')

if authentication_status:
    st.image("pics/iot.gif")
    st.title("Oresome Technology App Gallary")
    #st.markdown(
    #    '<nobr><p style="text-align: left;font-family:sans serif; color:#262730; font-size: 23px;">'
    #    'Welcome to the app gallary. We share the past and most <br> '
    #    'exciting IoT apps that have been deployed by our team. <br>'
    #    'Simply click on each app’s URL to view the app.</p></nobr>',
    #    unsafe_allow_html=True)
    st.write('Welcome to the app gallary.')
    st.write('We share the past and most exciting IoT apps that have been deployed by our team.')
    st.write('Simply click on each app’s URL to view the app.')
    st.markdown('###')
    st.markdown('###')
    # st.subheader("Welcome to the app gallary. We share the past and most exciting IoT apps that have been deployed by "
    #              "our team. Simply click on each app’s URL to view the app. We would love to hear your feedback.")

    #st.markdown("---")
    ##########################################################################
    st.subheader("Dexing Copper 34FT SAG Mill App", divider='rainbow')
    #st.markdown(
    #    '<nobr><p style="text-align: left;font-family:sans serif; color:#262730; font-size: 25px; font-weight: bold">'
    #    'Dexing Copper 34FT SAG Mill</p></nobr>',
    #    unsafe_allow_html=True)
    #st.markdown("###")
    st.write(
        '<style>a {text-decoration: underline; color: blue; font-size: 18px}</style><a target="_blank" '
        'href="https://dexing34ftsag22.streamlit.app/">https://dexing34ftsag22.streamlit.app/</a>',
        unsafe_allow_html=True)
    st.markdown("###")
    st.image("pics/example1.png")
    st.write("Author: Wei Chen")
    st.caption('This is the demo app for a SAG mill shell liner wear monitoring app!')

    ######################################################################
    ##########################################################################
    st.markdown("###")  
    st.markdown("###")
    st.subheader("Dexing Copper Hydrocyclone App", divider='rainbow')
    #st.markdown(
    #    '<nobr><p style="text-align: left;font-family:sans serif; color:#262730; font-size: 25px; font-weight: bold">'
    #    'Dexing Copper 34FT SAG Mill</p></nobr>',
    #    unsafe_allow_html=True)
    #st.markdown("###")
    st.write(
        '<style>a {text-decoration: underline; color: blue; font-size: 18px}</style><a target="_blank" '
        'href="https://dexingcopperhydrocyclone22.streamlit.app/">https://dexingcopperhydrocyclone22.streamlit.app/</a>',
        unsafe_allow_html=True)
    st.markdown("###")
    st.image("pics/example2.png")
    st.write("Author: Wei Chen")
    st.caption('This is the demo app for a hydrocyclone underflow pipe wear monitoring app!')

    ##########################################################################
    st.markdown("###")  
    st.markdown("###")
    st.subheader("Dexing Copper Slurry Pump Wear Monitoring App", divider='rainbow')
    #st.markdown(
    #    '<nobr><p style="text-align: left;font-family:sans serif; color:#262730; font-size: 25px; font-weight: bold">'
    #    'Dexing Copper 34FT SAG Mill</p></nobr>',
    #    unsafe_allow_html=True)
    #st.markdown("###")
    st.write(
        '<style>a {text-decoration: underline; color: blue; font-size: 18px}</style><a target="_blank" '
        'href="https://dexingcoppernzjah350pump22.streamlit.app/">https://dexingcoppernzjah350pump22.streamlit.app/</a>',
        unsafe_allow_html=True)
    st.markdown("###")
    st.image("pics/example3.png")
    st.write("Author: Wei Chen")
    st.caption('This is the demo app for a front liner of the slurry pump wear monitoring app!')

    ######################################################################

    ##########################################################################
    st.markdown("###")  
    st.markdown("###")
    st.subheader("CHINALCO Paste Backfill Pipe Wear Monitoring App", divider='rainbow')
    #st.markdown(
    #    '<nobr><p style="text-align: left;font-family:sans serif; color:#262730; font-size: 25px; font-weight: bold">'
    #    'Dexing Copper 34FT SAG Mill</p></nobr>',
    #    unsafe_allow_html=True)
    #st.markdown("###")
    st.write(
        '<style>a {text-decoration: underline; color: blue; font-size: 18px}</style><a target="_blank" '
        'href="https://huize1stage22.streamlit.app/">https://huize1stage22.streamlit.app/</a>',
        unsafe_allow_html=True)
    st.markdown("###")
    st.image("pics/example4.png")
    st.write("Author: Wei Chen")
    st.caption('This is the demo app for a paste backfill pipeline wear monitoring app!')

    ######################################################################

    ##########################################################################
    st.markdown("###")  
    st.markdown("###")
    st.subheader("CHINALCO Backfill Pipe Wear Monitoring App - Phase Two", divider='rainbow')
    st.write("Due to confidentiality issue, only a screen recording of the system is shown here!")
    #st.markdown(
    #    '<nobr><p style="text-align: left;font-family:sans serif; color:#262730; font-size: 25px; font-weight: bold">'
    #    'Dexing Copper 34FT SAG Mill</p></nobr>',
    #    unsafe_allow_html=True)
    #st.markdown("###")
    #st.write(
    #    '<style>a {text-decoration: underline; color: blue; font-size: 18px}</style><a target="_blank" '
    #    'href="https://huize1stage22.streamlit.app/">https://huize1stage22.streamlit.app/</a>',
    #    unsafe_allow_html=True)
    st.markdown("###")
    st.video("pics/huize2.mp4")
    st.write("Author: Wei Chen")
    st.caption('This is the screen recording for 2nd phase of the paste backfill pipeline wear monitoring app!')

    ######################################################################

elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
