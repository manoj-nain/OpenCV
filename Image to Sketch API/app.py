#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:07:30 2020

@author: manoj
"""


import cv2
import streamlit as st
import numpy as np
from io import BytesIO
from PIL import Image
import base64
# Our sketch generating function
def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 20)
    
    # Do an invert binarize the image 
    #ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return canny_edges
st.title("Image to Sketch")
st.markdown("This web application renders \
the uploaded images into Sketch.")
st.sidebar.title("Image to Sketch Streamlit Web Application")
st.sidebar.markdown("This web application renders \
the uploaded images into Sketch.")
uploaded_file=st.sidebar.file_uploader(label="Upload Image",\
type=["jpg","jpeg","png"],key="i")
    
def get_image_download_link(img):
	"""Generates a link allowing the PIL image to be downloaded
	in:  PIL image
	out: href string
	"""
	buffered = BytesIO()
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:file/jpg;base64,{img_str}">Download result</a>'
	return href
    
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()),\
    dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.subheader("Sketch")
    st.image(sketch(image),width=500)
    result = sketch(image)
    result = Image.fromarray(result)

    st.markdown(get_image_download_link(result), unsafe_allow_html=True)



