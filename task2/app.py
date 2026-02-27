# app.py

import streamlit as st
from PIL import Image
import torch
import matplotlib.pyplot as plt
from model import style_transfer
from utils import load_image

st.title("🎨 Neural Style Transfer App")

content_file = st.file_uploader("Upload Content Image", type=["jpg", "png"])
style_file = st.file_uploader("Upload Style Image", type=["jpg", "png"])

if content_file and style_file:
    content_image = Image.open(content_file).convert("RGB")
    style_image = Image.open(style_file).convert("RGB")

    st.image(content_image, caption="Content Image")
    st.image(style_image, caption="Style Image")

    if st.button("Generate Stylized Image"):
        st.write("Processing... ⏳")

        content_tensor = load_image(content_image)
        style_tensor = load_image(style_image)

        output = style_transfer(content_tensor, style_tensor)

        output_image = output.squeeze().detach().cpu().clamp(0, 1)
        output_image = transforms.ToPILImage()(output_image)

        st.image(output_image, caption="Stylized Output")