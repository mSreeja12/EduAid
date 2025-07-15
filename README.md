# 🧠 EduAid: AI Learning Assistant for Dyslexic Students

EduAid is a personalized, AI-powered learning assistant designed specifically for students with dyslexia and other learning difficulties. It simplifies complex educational content, translates it into the user’s preferred language, provides audio explanations, and generates visual aids to make learning inclusive and engaging.

---

## 🚀 Features

- ✅ **Simplifies complex text**
- 🌍 **Translates to multiple languages**
- 🔊 **Reads aloud translated content**
- 🖼️ **Generates contextual visual aids**
- 🎯 **Designed for neurodivergent learners**

---

## 💡 Example Use Case

### 🔤 Input

- **Selected Language**: German  
- **Input Paragraph**:

> Photosynthesis is the process used by plants, algae, and some bacteria to convert sunlight, carbon dioxide, and water into food in the form of glucose and oxygen.  
> This process takes place mainly in the leaves of plants, where chlorophyll — the green pigment — captures the energy from sunlight.  
> During this process, carbon dioxide from the air enters the leaves through small openings called stomata, and water absorbed by the roots is transported to the leaves.  
> The energy from sunlight splits the water molecules into hydrogen and oxygen. The hydrogen combines with carbon dioxide to produce glucose, which is used by the plant for energy and growth, while the oxygen is released into the atmosphere as a byproduct.

- **Image Prompt**: `Photosynthesis`

---

### ✅ Output

#### ✅ Simplified Text

> photosynthesis is the process used by plants, algae, and some bacteria to convert sunlight, carbon dioxide, and water into food in the form of glucose and oxygen.  
> this process takes place mainly in the leaves of plants, where chlorophyll — the green pigment — captures the energy from sunlight.

#### 🌍 Translated Text (German)

> Photosynthese ist der Prozess, der von Pflanzen, Algen und einigen Bakterien verwendet wird, um Sonnenlicht, Kohlendioxid und Wasser in Form von Glukose und Sauerstoff in Nahrung umzuwandeln.  
> Dieser Prozess findet hauptsächlich in den Blättern von Pflanzen statt, wo Chlorophyll — das grüne Pigment — die Energie aus Sonnenlicht einfängt.

#### 🔊 Audio Output

The app uses **gTTS (Google Text-to-Speech)** to convert the translated text into speech in the selected language. For German, you’ll hear the explanation spoken in German.

---

## 🎓 Who Can Use This?

- Students with **dyslexia** or **reading disabilities**
- Parents supporting children's education
- Inclusive educators in digital classrooms
- NGOs and EdTech tools focused on accessibility

---

## 🛠️ How It Works

1. **Enter** a complex paragraph.
2. **Choose** your preferred explanation language.
3. **Optionally add** an image keyword (like "solar system").
4. Click **Generate Aids** – and get:
   - ✅ Simplified text
   - 🌍 Translated explanation
   - 🔊 Spoken version
   - 🖼️ Visual illustration (using Unsplash)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/eduaid.git
cd eduaid

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run eduaid.py
