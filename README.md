-----

## Image Story Weaver

An interactive web application that leverages **Google's Gemini 2.0 Flash** model to generate descriptive captions and creative short stories from uploaded images.

-----

### ✨ Features

  * **Image Upload:** Easily upload your favorite images in JPG, JPEG, or PNG formats.
  * **Intelligent Captioning:** Gemini 2.0 Flash analyzes your image and generates a concise, relevant caption.
  * **Creative Story Generation:** Gemini 2.0 Flash takes the generated caption and weaves a unique, imaginative short story inspired by the image.
  * **User-Friendly Interface:** Built with Streamlit for a simple and intuitive user experience.

-----

### 🚀 Getting Started

You can the project [HERE](image-story-weaver.streamlit.app) image-story-weaver.streamlit.app. Follow these steps to set up and run the project locally.

#### Prerequisites

  * Python 3.9+ installed on your system.
  * A Google Gemini API Key. You can obtain one from [Google AI Studio](https://aistudio.google.com/).

#### 1\. Clone the Repository

```bash
git clone https://github.com/JayGupta2003/image-story-weaver.git
cd image-story-weaver
```


#### 2\. Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`
```

#### 3\. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4\. Run the Application

```bash
streamlit run app.py
```

Your default web browser should automatically open the application at `http://localhost:8501/`.

-----

### 💻 How to Use

1. **Enter Your Google API KEY for Gemini**:  Enter your API KEY and press enter to apply.
1.  **Upload an Image:** Click the "Choose an image..." button and select a JPG, JPEG, or PNG file from your computer.
2.  **View Caption:** Once uploaded, the application will display your image and automatically generate a descriptive caption using Gemini.
3.  **Read Your Story:** After the caption appears, Gemini will then craft a creative short story inspired by the image and its caption. The story will be displayed below.

-----

### 📄 Code Structure

  * `app.py`: The main Streamlit application script containing the UI, Gemini API calls, and image processing logic.
  * `requirements.txt`: Lists all necessary Python dependencies.

-----

### 🤝 Contributing

Contributions are welcome\! If you have suggestions for improvements, new features, or bug fixes, feel free to open an issue or submit a pull request.

-----

### 📜 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

-----

### 🙏 Acknowledgements

  * **Google Gemini API:** For powerful multimodal and text generation capabilities.
  * **Streamlit:** For simplifying web application development in Python.
