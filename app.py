import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
import io

# if  'GOOGLE_API_KEY' not in st.secrets:
#     st.error("Google API Key not found in st.secrets. Please add it to your .streamlit/secrets.toml file.")
#     st.stop()


vision_model = genai.GenerativeModel('gemini-2.0-flash')
text_model = genai.GenerativeModel('gemini-2.0-flash-lite')

def load_image_from_bytes(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image

def generate_caption(image_data, GOOGLE_API_KEY):
    genai.configure(api_key=GOOGLE_API_KEY)
    try:
        prompt_parts = [
            "You are an expert in image captioning.",
            "Generate a detailed and descriptive caption for the following image.",
            "The caption should be concise but informative.",
            image_data
        ]
        response = vision_model.generate_content(prompt_parts)
        return response.text
    except Exception as e:
        st.error(f"Error generating caption: {e}")
        return None
    
def generate_story(caption, GOOGLE_API_KEY):
    genai.configure(api_key=GOOGLE_API_KEY)
    try:
        prompt_parts = [
            "You are a creative storyteller.",
            "Based on the following caption, generate a short story.",
            "The story should be engaging and imaginative.",
            caption
        ]
        response = text_model.generate_content(prompt_parts)
        return response.text
    except Exception as e:
        st.error(f"Error generating story: {e}")
        return None
    
st.set_page_config(
    page_title="Image Story Weaver",
    page_icon="✨",
    layout="centered"
)

st.title("✨ Image Story Weaver ✨")
api_key = st.text_input("Enter your Google API Key", type="password")
st.markdown("Upload an image, and let Gemini generate a caption and a creative story for it!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("")

    image_bytes = uploaded_file.read()
    pil_image = load_image_from_bytes(image_bytes)

    st.subheader("1. Generating Caption...")
    with st.spinner("Gemini is analyzing your image..."):
        caption = generate_caption(pil_image, api_key)
    if caption:
        st.success("Caption Generated!")
        st.info(f"**Caption:** {caption}")

        st.subheader("2. Generating Story...")
        with st.spinner("Gemini is weaving a tale..."):
            story = generate_story(caption, api_key)
        if story:
            st.success("Story Generated!")
            st.markdown("---")
            st.subheader("Your Story:")
            st.write(story)
    else:
        st.error("Could not generate a caption. Please try another image or check your API key/network.")
else:
    st.info("Please upload an image to begin.")

st.markdown("---")
st.caption("Powered by Google Gemini API & Streamlit")