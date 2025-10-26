➤AI PROMPT GENERATOR
An interactive web app built using Python, Streamlit, and OpenAI API, designed to generate optimized text prompts and AI-generated images based on user goals. This project helps creators, developers, and designers quickly craft effective prompts for writing, art, coding, and creative projects.

➤FEATURES
* Smart Prompt Generation: Uses OpenAI’s gpt-4o-mini model to generate structured, goal-oriented prompts.
* Prompt Variations: Produces multiple versions — Simple, Detailed, and Creative — to fit different use cases.
* AI Image Generation: Generates visuals using gpt-image-1, turning textual goals into concept art or idea sketches.
* User-Friendly Interface: Built fully with Streamlit — no frontend coding required.
* Secure Key Management: Uses python-dotenv to hide API keys safely.

➤PROJECT STRUCTURE
AI-Prompt-Generator/
│
├── app.py                        # Main Streamlit UI
├── utils/
│   └── prompt_generator.py       # Core prompt and image generation logic
├── .env                          # Stores OpenAI API key (excluded from Git)
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

➤SETUP INSTRUCTIONS
1. Create and activate a virtual environment: python -m venv venv source venv/bin/activate # for macOS/Linux venv\Scripts\activate # for Windows

2. Install all dependencies: pip install -r requirements.txt

3. Create a .env file in the project root directory and add your OpenAI API key: OPENAI_API_KEY=your_api_key_here

4. Run the app using Streamlit: streamlit run app.py
