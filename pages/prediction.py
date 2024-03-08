"""
    Contract Study
    Madan Baduwal
"""

import streamlit as st
import numpy as np
import torch
from PIL import Image
from unet.predict import predict
from unet import model

model_dict = {'dice loss + cross entropy loss, l_rate = 0.0001': "pretrained1",
              'dice loss, l_rate = 0.0001': "pretrained2",
              'dice loss + cross entropy loss, l_rate = 0.001': "pretrained3",
              'dice loss + cross entropy loss, l_rate = 0.01': "pretrained4",
              'dice loss + cross entropy loss, l_rate = 0.1': "pretrained5"}


# import pretrained model
@st.cache_resource
def load_model(model_name: str):
    unet = model.Unet(3)
    model_params = torch.load(f"data/{model_name}/{model_name}.pth",
                              map_location=torch.device('cpu'))
    unet.load_state_dict(model_params['model'])
    return unet


# model option
st.header("Contract Study: Brain tumor segmentation")
st.markdown("<h5 style='text-align: center;'>Department of Computer Science, University of Texas Permian Basin</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>baduwal_m63609@utpb.edu</h5>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: left;'>Select a pre-trained model:</h5>", unsafe_allow_html=True)
option = st.selectbox("select a model",
                      ('dice loss + cross entropy loss, l_rate = 0.0001',
                       'dice loss, l_rate = 0.0001',
                       'dice loss + cross entropy loss, l_rate = 0.001',
                       'dice loss + cross entropy loss, l_rate = 0.01',
                       'dice loss + cross entropy loss, l_rate = 0.1'),
                      label_visibility='collapsed')

# file uploader
st.markdown("<h5 style='text-align: left;'>Select a brain MRI image:</h5>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a file", type=['png', 'jpg', 'tif'])

col1, col2 = st.columns(2)
with col1:
    # image cache
    image_cache = st.container()
    if uploaded_file is not None:
        # convert image into np array
        img = Image.open(uploaded_file).convert('RGB')
        img_array = np.array(img)

        # check if the file is valid (3 * 256 * 256)
        if img_array.shape != (256, 256, 3):
            st.write("Image size should be 256*256")
        else:
            # display image
            image_cache.subheader("Your uploaded file:")
            image_cache.image(img_array)

            # store in streamlit session
            st.session_state.img_array = img_array
            img_array = img_array / 255
    elif 'img_array' in st.session_state:
        img_array = st.session_state.img_array
        # display image
        image_cache.subheader("Your uploaded file:")
        image_cache.image(img_array)
    img_pred_button = st.button('Predict')

with col2:
    if img_pred_button:
        if "img_array" not in st.session_state:
            st.write("You haven't upload any file!")
        else:
            # get predicted mask image
            st.subheader("Model Prediction:")
            pred_img = st.session_state.img_array / 255
            pred_mask = predict(pred_img, torch.device('cpu'),
                                load_model(model_dict[option]))
            pred_mask = pred_mask[0].permute(1, 2, 0)
            st.session_state.pred_mask = pred_mask
            st.image(pred_mask.numpy())
            clear = st.button("clear prediction")

            # clear prediction and content
            if clear:
                del st.session_state.pred_maskl
                img_pred_button = False
