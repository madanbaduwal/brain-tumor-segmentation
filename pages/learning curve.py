"""
    Contract Study : Brain Tumor Segmentation
    -Training and validating a U-Net model
    Madan Baduwal
"""
import pandas as pd
import streamlit as st
from PIL import Image

# set up necessary variables
path = "data/data_analysis"
model_list = ('dice loss + cross entropy loss, l_rate = 0.0001',
              'dice loss, l_rate = 0.0001',
              'dice loss + cross entropy loss, l_rate = 0.001',
              'dice loss + cross entropy loss, l_rate = 0.01',
              'dice loss + cross entropy loss, l_rate = 0.1')
model_dict = {model_list[0]: "pretrained1",
              model_list[1]: "pretrained2",
              model_list[2]: "pretrained3",
              model_list[3]: "pretrained4",
              model_list[4]: "pretrained5"}

# # show learning curves of multiple model with different learning rate
# st.subheader("Compare learning curves")
# multiple_loss = Image.open(f"{path}/accuracy_curves_multiple_loss.png")
# st.image(multiple_loss)

# # display test accuracy
# df = pd.read_csv("data/data_analysis/test_accuracy.csv", index_col=False)
# st.dataframe(df, use_container_width=True)

# # show details of selected model
# st.subheader("See details:")
# option = st.selectbox("select a model",
#                       model_list,
#                       label_visibility='collapsed')
# chosen_model = model_dict[option]
# accuracy_curve = Image.open(f"{path}/{chosen_model}_accuracy_curve.png")
# train_valid_dices = Image.open(f"{path}/{chosen_model}_train_valid_dice.png")

# st.image(accuracy_curve)
# st.image(train_valid_dices)
