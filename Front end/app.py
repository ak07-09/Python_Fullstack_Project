import streamlit as st
import requests
from datetime import datetime

# Configuration
API_BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title="🚀 Prompt Builder",
    page_icon="✨",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prompt-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
    .success-msg {
        color: #28a745;
        font-weight: bold;
    }
    /* Streamlit-specific enhancements */
    .stButton>button {
        width: 100%;
    }
    .stTextArea {
        min-height: 150px;
    }
</style>
""", unsafe_allow_html=True)


def check_api_status():
    """Check if the backend API is running."""
    try:
        requests.get(f"{API_BASE_URL}/")
        return True
    except requests.exceptions.ConnectionError:
        return False


def enhance_prompt(user_input):
    """Call the API to enhance a prompt"""
    try:
        payload = {"user_input": user_input}
        response = requests.post(f"{API_BASE_URL}/build", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error enhancing prompt: {str(e)}")
        return None


def get_all_prompts():
    """Retrieve all prompts from API"""
    try:
        response = requests.get(f"{API_BASE_URL}/prompts")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching prompts: {str(e)}")
        return []


def get_random_prompt():
    """Get a random prompt from API"""
    try:
        response = requests.get(f"{API_BASE_URL}/prompts/random")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        # Returns None if no prompts are found, which is a 404
        return None


# Main app
def main():
    st.markdown('<h1 class="main-header">🚀 Prompt Builder</h1>', unsafe_allow_html=True)
    
    if not check_api_status():
        st.warning("🚨 The backend API is not running. Please start the backend server.")
        return
        
    # Sidebar
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choose a mode", 
                                ["Enhance Prompt", "View History", "Random Prompt"])
    
    if app_mode == "Enhance Prompt":
        render_enhancement_interface()
    elif app_mode == "View History":
        render_history_interface()
    elif app_mode == "Random Prompt":
        render_random_interface()


def render_enhancement_interface():
    st.header("✨ Prompt Enhancement")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        user_input = st.text_area(
            "Enter your basic prompt:",
            placeholder="e.g., gaming wallpaper, nature scene, coding concept...",
            height=100
        )
        
    with col2:
        st.info("💡 **Tips:**\n- Be descriptive but concise\n- Use specific keywords\n- Let the AI add the details!")
    
    if st.button("🚀 Enhance Prompt", type="primary"):
        if not user_input.strip():
            st.warning("Please enter a prompt to enhance")
            return
        
        with st.spinner("Enhancing your prompt..."):
            result = enhance_prompt(user_input)
            
            if result:
                st.success("✅ Prompt enhanced successfully!")
                
                st.markdown("### Enhanced Prompt")
                st.markdown(f'<div class="prompt-card">{result["prompt"]}</div>', 
                            unsafe_allow_html=True)
                
                # Show comparison
                st.subheader("Comparison")
                col1, col2 = st.columns(2)
                with col1:
                    st.info(f"**Original:** {user_input}")
                with col2:
                    st.success(f"**Enhanced:** {result['prompt']}")


def render_history_interface():
    st.header("📚 Prompt History")
    
    if st.button("🔄 Refresh History"):
        st.rerun()
    
    prompts = get_all_prompts()
    
    if not prompts:
        st.info("No prompts found. Start by enhancing some prompts!")
        return
    
    st.success(f"Found {len(prompts)} prompts in history")
    
    # Sort prompts by creation date (newest first)
    sorted_prompts = sorted(prompts, key=lambda p: p['created_at'], reverse=True)

    for prompt in sorted_prompts:
        with st.expander(f"Prompt #{prompt['id']} - {prompt['user_input'][:50]}..."):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Original Prompt**")
                st.text(prompt['user_input'])
            
            with col2:
                st.markdown("**Enhanced Prompt**")
                st.text(prompt['improved'])
            
            # Format the creation date
            creation_date = datetime.fromisoformat(prompt['created_at'].replace('Z', '+00:00'))
            st.caption(f"Created: {creation_date.strftime('%B %d, %Y at %I:%M %p')}")


def render_random_interface():
    st.header("🎲 Random Prompt")
    st.info("Get inspired with a random enhanced prompt from our database!")
    
    if st.button("🎯 Get Random Prompt", type="primary"):
        with st.spinner("Fetching random prompt..."):
            prompt = get_random_prompt()
            
            if prompt:
                st.balloons()
                st.markdown("### Your Random Prompt")
                st.markdown(f'<div class="prompt-card">{prompt["improved"]}</div>', 
                            unsafe_allow_html=True)
                
                st.info(f"**Original idea:** {prompt['user_input']}")
                creation_date = datetime.fromisoformat(prompt['created_at'].replace('Z', '+00:00'))
                st.caption(f"Created: {creation_date.strftime('%B %d, %Y at %I:%M %p')}")
            else:
                st.warning("No prompts found in the database. Create some first!")


if __name__ == "__main__":
    main()