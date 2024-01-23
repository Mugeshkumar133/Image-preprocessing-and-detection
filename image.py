import numpy
import streamlit as st
from PIL import Image,ImageFilter,ImageEnhance
from streamlit_option_menu import option_menu
from PIL import ImageOps

st.set_page_config(page_title ="Image  Preprocessing and Detection ",layout="wide")

st.write("""

<div style='text-align:center'>
    <h1 style='color:#009999;'>Image Preprocessing and Detection</h1>
</div>
""", unsafe_allow_html=True)


uploaded_file=st.sidebar.file_uploader(label="Upload your jpg or jpeg file.max(200mb)",type=["jpg","jpeg"])


if uploaded_file is not None:
    
    try:
       image = Image.open(uploaded_file)
    except Exception as e:
       print(e)

with st.sidebar:
     opt = option_menu("Processed Data ",
                      ["Home","GrayImage","Blurred Image","Contrasted Image","Rotated Image","Mirror Image","Brightened Image","Negative Image","Edge Detected Image","Sharpened Image","Framed Image"],
                      menu_icon="cast",
                      styles={
                          "container":{"padding":"4!important","background-color":"gray"},
                          "icon":{"color":"red","font-size":"20px"},
                          "nav-link":{"font-size":"20px","text-align":"left"},
                          #"nav-link-selected":{"background-color":"yellow"}
                      })
if opt == "Home":
    st.subheader("This project deals with uploading an image and doing all preprocessing works like blurred, checking the shape,sharpening the image,edge detection,brightening the image,framing the image etc... ")
    st.write("Image in original format")
    image= Image.open(uploaded_file)
    st.image(image)
if opt == "GrayImage":
    gray_image=image.convert("L")
    st.image(gray_image)

if opt == "Blurred Image":
    Blurred_image= image.filter(ImageFilter.GaussianBlur(radius=10))
    st.image(Blurred_image)
if opt== "Contrasted Image":
    Blurred_image= image.filter(ImageFilter.GaussianBlur(radius=10))
    con_1 = ImageEnhance.Contrast(Blurred_image)
    st.image(con_1.enhance(20))
if opt == "Rotated Image":
    st.image(image.rotate(180))
    st.image(image.rotate(200))
if opt == "Mirror Image":
    st.image(ImageOps.mirror(image))
if opt=="Brightened Image":
    bright= ImageEnhance.Brightness(image)
    bright1=bright.enhance(3.9)
    st.image(bright1)
if opt=="Negative Image":
    neg_image = ImageOps.invert(image)
    st.image(neg_image)
if opt=="Edge Detected Image":
    st.image(image.filter(ImageFilter.FIND_EDGES))
if opt=="Sharpened Image":
    sharped_image= ImageEnhance.Sharpness(image)
    st.image(sharped_image.enhance(10))
if opt=="Framed Image":
    st.image(ImageOps.expand(image,10,"black"))


