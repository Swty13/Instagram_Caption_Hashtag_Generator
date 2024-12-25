import streamlit as st
from PIL import Image
import os
from insta_caption_generator import generate_caption_and_hashtags
import base64

def add_bg_from_local():
    """Function to load and encode background image"""
    with open("3685080.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
        }}
        
        .uploadedImage {{
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        
        .custom-container {{
            background-color: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin: 1rem 0;
        }}
        
        .title {{
            color: #1E1E1E;
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 2rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }}
        
        .button {{
            background-color: #FF6B6B;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            border: none;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }}
        
        .button:hover {{
            background-color: #FF5252;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}

        .stSelectbox {{
            background-color: white;
            border-radius: 5px;
            margin-bottom: 1rem;
        }}

        .selectbox-container {{
            background-color: rgba(255, 255, 255, 0.8);
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def save_uploaded_file(uploaded_file, save_path="uploaded_images"):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = os.path.join(save_path, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

import json
import streamlit as st

def format_caption(response):
    """
    Extracts and formats a caption from a JSON response string,
    then displays it inside a styled Streamlit container.
    
    Parameters:
        response (str): JSON string containing a "Caption" key.
    """
    # Parse the JSON string into a dictionary
    response_dict = json.loads(response)
    
    # Extract the caption
    caption = response_dict["Caption"]
    
    # Replace literal \n with actual newlines
    formatted_caption = caption.replace('\\n', '\n')
    
    # Display styled container with formatted caption
    st.markdown("""
        <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h3 style='color: #1E1E1E; margin-bottom: 10px;'>📝 Your Generated Caption</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style='background-color: white; padding: 20px; border-radius: 10px; margin-top: 10px;'>
            <p style='font-size: 1.1rem; color: #1E1E1E; white-space: pre-wrap;'>{formatted_caption}</p>
        </div>
    """, unsafe_allow_html=True)


def main():
    # Add background image
    add_bg_from_local()
    
    # Title with custom styling
    st.markdown('<h1 class="title">✨ Instagram Caption Generator ✨</h1>', unsafe_allow_html=True)
    
    st.markdown("""
        <p style='text-align: center; font-size: 1.2rem; color: #666;'>
            Transform your images into engaging Instagram posts with AI-generated captions!
        </p>
    """, unsafe_allow_html=True)
    
    # Create columns for better layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Upload image section
        uploaded_image = st.file_uploader("📸 Upload your image", type=["jpg", "jpeg", "png"])
        
        # Style container for content type and tone
        st.markdown('<div class="selectbox-container">', unsafe_allow_html=True)
        
        # Content type selection with icon
        st.markdown("📑 **Content Category**")
        content_type = st.selectbox(
            "Select content type",
            ["Fashion 👗", "Food 🍽️", "Travel ✈️", "Lifestyle 🌟", 
             "Business 💼", "Fitness 💪", "Beauty 💄", "Other 🎯"],
            label_visibility="collapsed"
        )
        
        # Tone selection with icon
        st.markdown("🎭 **Caption Tone**")
        tone = st.selectbox(
            "Select caption tone",
            ["Professional 👔", "Casual 😊", "Funny 😄", 
             "Inspirational ✨", "Educational 📚"],
            label_visibility="collapsed"
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Additional description with styled input
        st.markdown("📝 **Additional Details**")
        additional_description = st.text_area(
            "Additional description (optional)",
            placeholder="Add any specific details you'd like to include in the caption...",
            height=100,
            label_visibility="collapsed"
        )
    
    with col2:
        # Display uploaded image
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            save_path = save_uploaded_file(uploaded_image)
            st.image(image, caption="Preview", use_container_width=True, clamp=True)
    
    # Generate button with custom styling
    if uploaded_image is not None:
        if st.button("🎨 Generate Caption", key="generate_button"):
            with st.spinner("✨ Creating your perfect caption..."):
                # Strip emojis from content_type and tone for processing
                clean_content_type = content_type.split()[0]
                clean_tone = tone.split()[0]
                
                caption = generate_caption_and_hashtags(
                    save_path, 
                    additional_description, 
                    content_type=clean_content_type, 
                    tone=clean_tone
                )
                format_caption(caption)

    else:
        st.info("👆 Upload an image to get started!")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    # Set page config
    st.set_page_config(
        page_title="Instagram Caption Generator",
        page_icon="✨",
        layout="wide"
    )
    main()