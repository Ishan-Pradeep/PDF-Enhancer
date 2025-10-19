import streamlit as st
from ppt_enhancer.parser import parse_pptx
from ppt_enhancer.designer import design_slides
from ppt_enhancer.generator import generate_pptx
import tempfile, os

st.set_page_config(page_title="AI Presentation Enhancer", page_icon="💡")
st.title("💡 AI Presentation Enhancer")
st.write("Upload your PowerPoint and let AI make it visually professional!")

uploaded_file = st.file_uploader("Upload a .pptx file", type=["pptx"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pptx") as tmp:
        tmp.write(uploaded_file.read())
        input_path = tmp.name

    st.info("Processing your slides... ⏳")
    slides = parse_pptx(input_path)
    designed = design_slides(slides)
    output_path = os.path.join(tempfile.gettempdir(), "enhanced.pptx")
    generate_pptx(designed, output_path)

    st.success("✅ Enhancement complete!")
    with open(output_path, "rb") as f:
        st.download_button("⬇️ Download Enhanced PowerPoint", f, file_name="enhanced.pptx")
