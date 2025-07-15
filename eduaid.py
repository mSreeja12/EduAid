import streamlit as st
from transformers import pipeline
from gtts import gTTS
import tempfile
import os
from PIL import Image
from io import BytesIO
import requests

# 🌍 Hugging Face Token for access to translation models
HF_TOKEN = "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"

# -------------------- SETUP -------------------- #
st.set_page_config(page_title="EduAid - Learning Assistant", layout="centered")
st.title("🧠 EduAid: AI Learning Assistant for Dyslexic Students")
st.markdown("Helps simplify, translate, and speak out educational content.")

# -------------------- CACHED MODELS -------------------- #
@st.cache_resource(show_spinner=True)
def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@st.cache_resource(show_spinner=True)
def load_simplifier():
    return pipeline("text2text-generation", model="t5-base")

@st.cache_resource(show_spinner=True)
def load_translator(model_id):
    return pipeline("translation", model=model_id, token=HF_TOKEN)

# -------------------- MODEL INITIALIZATION -------------------- #
summarizer = load_summarizer()
simplifier = load_simplifier()

# -------------------- LANGUAGE SELECTION -------------------- #
language_options = {
    "English": ("en", None),
    "Hindi": ("hi", "Helsinki-NLP/opus-mt-en-hi"),
    "French": ("fr", "Helsinki-NLP/opus-mt-en-fr"),
    "Spanish": ("es", "Helsinki-NLP/opus-mt-en-es"),
    "German": ("de", "Helsinki-NLP/opus-mt-en-de")
}

st.subheader("🌐 Choose Language for Audio")
lang_name = st.selectbox("Select a language for the explanation:", list(language_options.keys()))
lang_code, model_id = language_options[lang_name]

# -------------------- USER INPUT -------------------- #
st.subheader("📄 Enter or Paste Text")
text_input = st.text_area("Paste the paragraph you want simplified or explained:", height=200)

st.subheader("🖼️ Image Prompt (Optional)")
image_prompt = st.text_input("Enter a keyword for visual aid (e.g., solar system)")

# -------------------- ACTION -------------------- #
if st.button("🔍 Generate Aids"):
    if not text_input.strip():
        st.warning("Please enter some text to process.")
        st.stop()

    with st.spinner("Processing..."):
        try:
            # Step 1: Simplify
            simplified = simplifier(f"simplify: {text_input}", max_length=100)[0]['generated_text']

            # Step 2: Translate (if needed)
            if model_id:
                try:
                    translator = load_translator(model_id)
                    translated = translator(simplified, max_length=100)[0]['translation_text']
                except Exception as e:
                    st.warning(f"⚠️ Translation failed: {e}")
                    translated = simplified
            else:
                translated = simplified

            # Step 3: Text-to-Speech
            tts = gTTS(translated, lang=lang_code)
            temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(temp_audio_file.name)

            # Step 4: Summarize for image
            summary = summarizer(text_input, max_length=40, min_length=10, do_sample=False)[0]['summary_text']

            # -------------------- OUTPUT -------------------- #
            st.success("Done! See results below:")

            st.subheader("✅ Simplified Text")
            st.write(simplified)

            st.subheader("🌍 Translated Text")
            st.write(translated)

            st.subheader("🔊 Listen to Explanation")
            audio_file = open(temp_audio_file.name, 'rb')
            st.audio(audio_file.read(), format='audio/mp3')
            audio_file.close()

            if image_prompt:
                st.subheader("🖼️ Visual Aid")
                url = f"https://source.unsplash.com/600x400/?{image_prompt}"
                response = requests.get(url)
                image = Image.open(BytesIO(response.content))
                st.image(image, caption=f"Illustration: {image_prompt.title()}", use_column_width=True)

        except Exception as e:
            st.error(f"❌ Failed to generate aids: {e}")

# -------------------- FOOTER -------------------- #
st.markdown("---")
st.markdown("Made with ❤️ using HuggingFace, gTTS, and Streamlit")
