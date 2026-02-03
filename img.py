# app.py
# AI Image Analytics using Streamlit & Gemini (Error-Free Version)

import streamlit as st
import google.generativeai as genai
from PIL import Image

# ---------------- CONFIG ----------------
# ⚠️ For testing only. Do NOT upload this key to GitHub.
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- UI ----------------
st.set_page_config(page_title="AI Image Analytics", layout="centered")

st.title("🖼️ AI Image Analytics System")
st.write("Upload an image and ask questions using Generative AI.")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

# ---------------- IMAGE PREVIEW ----------------
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.subheader("📊 Image Details")
    st.write(f"**Format:** {image.format}")
    st.write(f"**Size:** {image.size[0]} x {image.size[1]}")

# ---------------- QUESTION SECTION ----------------
st.subheader("❓ Ask a Question")

sample_questions = [
    "Describe this image",
    "What objects are visible?",
    "What is happening in the image?",
    "What is the main subject?"
]

question = st.selectbox("Choose a sample question", sample_questions)
custom_question = st.text_input("Or type your own question")

final_question = custom_question if custom_question.strip() else question

# ---------------- BUTTON ACTION ----------------
if st.button("🔍 Analyze Image"):
    if image is None:
        st.error("Please upload an image first.")
    else:
        try:
            with st.spinner("Analyzing image..."):
                response = model.generate_content([final_question, image])

            st.success("Analysis Complete")
            st.markdown("### 🧠 AI Response")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("MCA Mini Project | AI Image Analytics using Streamlit & Gemini")
