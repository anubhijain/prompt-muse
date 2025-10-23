import streamlit as st
from utils.prompt_generator import PromptGenerator

st.set_page_config(page_title="AI Prompt Generator", page_icon="🤖")

st.title("🤖 AI Prompt Generator")

# Input fields
goal = st.text_area("Enter your goal", height=100, placeholder="e.g., Write a poem about space")
tone = st.selectbox("Select tone/style", ["professional", "casual", "funny", "poetic", "technical"])
style = st.text_input("Additional style (optional)", placeholder="e.g., rhyming, step-by-step")
output_format = st.text_input("Output format (optional)", placeholder="e.g., 4 stanzas, bullet points, JSON")

generator = PromptGenerator()

# Generate single prompt button
if st.button("Generate Prompt"):
    if not goal.strip():
        st.error("Please enter a goal")
    else:
        with st.spinner("Generating prompt..."):
            prompt = generator.generate(goal, tone, style, output_format)
        st.subheader("Generated Prompt")
        st.text_area("Prompt", value=prompt, height=200)

st.markdown("---")  # Divider

# Generate prompt variations button
if st.button("Generate Prompt Variations"):
    if not goal.strip():
        st.error("Please enter a goal")
    else:
        with st.spinner("Generating prompt variations..."):
            variations = generator.generate_variations(goal)
        st.subheader("Prompt Variations")
        st.text_area("Variations", value=variations, height=300)

st.markdown("---")  # Divider

# Generate image from prompt and display
if st.button("Generate Image Prompt and Visual"):
    if not goal.strip():
        st.error("Please enter a goal")
    else:
        with st.spinner("Generating prompt and image..."):
            prompt = generator.generate(goal)
            images = generator.generate_image(prompt)
        st.subheader("Generated Prompt")
        st.text_area("Prompt", value=prompt, height=200)
        st.subheader("Generated Images")
        for url in images:
            st.image(url)
