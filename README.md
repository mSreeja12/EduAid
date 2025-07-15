# 🧠 EduAid: AI Learning Assistant for Dyslexic Students

EduAid is a personalized, AI-powered learning assistant designed specifically for students with dyslexia and other learning differences. It helps simplify complex text, translate explanations into the user's native language, and generate both audio and visual learning aids for better comprehension.

![EduAid Interface](images/screenshot_1.png)

---

## 🚀 Features

✅ **Text Simplification**  
Breaks down complex academic paragraphs into simpler, easy-to-understand language.

🌐 **Multilingual Translation**  
Translates the simplified text into over 25 languages using HuggingFace Transformers.

🔊 **Text-to-Speech (TTS)**  
Reads out the explanation in the selected language using gTTS (Google Text-to-Speech).

🖼️ **Visual Aid Generator**  
Fetches contextual images from Unsplash based on user-provided prompts to aid visual learners.

🧑‍💻 **Built With**  
- [Streamlit](https://streamlit.io/) for UI  
- [HuggingFace Transformers](https://huggingface.co/transformers/)  
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)  
- [Unsplash Source API](https://source.unsplash.com/) for free contextual images

---

## 💡 Example Use Case

### 🔤 Input:
- **Language Chosen:** German  
- **Text Provided:**

> Photosynthesis is the process used by plants, algae, and some bacteria to convert sunlight, carbon dioxide, and water into food in the form of glucose and oxygen.  
> This process takes place mainly in the leaves of plants, where chlorophyll — the green pigment — captures the energy from sunlight.

- **Visual Prompt:** `Photosynthesis`

![EduAid Input Screenshot](images/screenshot_2.png)

---

### ✅ Output

#### ✅ **Simplified Text**
> photosynthesis is the process used by plants, algae, and some bacteria to convert sunlight, carbon dioxide, and water into food in the form of glucose and oxygen...

#### 🌍 **Translated Text (German)**
> Photosynthese ist der Prozess, der von Pflanzen, Algen und einigen Bakterien verwendet wird, um Sonnenlicht, Kohlendioxid und Wasser in Form von Glukose und Sauerstoff in Nahrung umzuwandeln...

#### 🔊 **Listen to Explanation**
> ✔️ Audio is generated using `gTTS` in the selected language (e.g., German).

#### 🖼️ **Visual Aid**
> ✔️ Image generated based on keyword "Photosynthesis" using Unsplash.

![EduAid Output Screenshot](images/screenshot_3.png)

---

## 🧑‍🏫 Who is this for?

- Students with learning difficulties like dyslexia  
- Educators looking for inclusive teaching tools  
- Parents who support their child's remote learning journey  
- Schools promoting accessible education

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/eduaid-ai.git
cd eduaid-ai

# (Optional) Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the app
streamlit run eduaid.py
