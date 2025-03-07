from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import io

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("Google_API_Key"))

# Initialize Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get Gemini response
def get_gemini_response(text_input, image):
    contents = []

    # Ensure at least some text is present
    if not text_input.strip():
        text_input = "Describe this image in detail."

    contents.append(text_input)  # Add text input

    if image:
        # Convert image to bytes
        img_byte_array = io.BytesIO()
        image.save(img_byte_array, format="PNG")  # Convert image to PNG format
        img_bytes = img_byte_array.getvalue()

        # Append image in the correct format
        contents.append({"mime_type": "image/png", "data": img_bytes})

    # Generate response from Gemini
    response = model.generate_content(contents)
    return response.text if response else "No response received."

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

# User text input
text_input = st.text_input("Enter your text prompt:", key="text_input")

# File uploader
uploaded_file = st.file_uploader("Upload an image (JPG, PNG, JPEG):", type=["jpg", "png", "jpeg"])
image = None

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)  # Updated parameter
    st.success("Image uploaded successfully!")

# Submit button
if st.button("Tell me about the image"):
    if text_input.strip() or image:  # Ensure at least one input is provided
        response = get_gemini_response(text_input, image)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.warning("Please enter a text prompt or upload an image.")

