import json
import httpx
import streamlit as st

st.set_page_config(page_title="Imaging LLM Agent", layout="wide")

# Custom CSS for subtle animations and better styling
st.markdown("""
<style>
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .title-animate {
        animation: fadeIn 1.5s ease-out;
        font-size: 3em;
        font-weight: bold;
        color: #4F8BF9;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%;
        background-color: #4F8BF9;
        color: white;
        border-radius: 8px;
        height: 3em;
    }
</style>
<div class="title-animate">Imaging LLM Agent 🤖</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Configuration")
    api_url = st.text_input("API URL", "http://127.0.0.1:8000/run")
    text = st.text_area("Request", height=150, placeholder="Describe the imaging task...")
    
    run_clicked = st.button("Run Analysis")

with col2:
    st.subheader("Results")
    if run_clicked:
        with st.spinner("Processing request..."):
            try:
                r = httpx.post(api_url, json={"text": text}, timeout=120)

                st.write("HTTP status:", r.status_code)
                st.write("Content-Type:", r.headers.get("content-type", ""))

                # If not 2xx, just show raw text and stop
                if r.status_code < 200 or r.status_code >= 300:
                    st.error("Non-2xx response from API")
                    st.code(r.text or "<empty body>")
                else:
                    try:
                        data = r.json()
                        st.success("Analysis Complete")
                        
                        # Show the user's original request
                        st.markdown("### User Request")
                        st.info(text)

                        if isinstance(data, dict):
                            # Identify thinking/reasoning fields vs final output
                            thinking_keys = [k for k in data.keys() if any(x in k.lower() for x in ['thought', 'reasoning', 'plan'])]
                            output_keys = [k for k in data.keys() if k not in thinking_keys]

                            # Show thinking process in an expander
                            if thinking_keys:
                                with st.expander("🧠 Agent Thinking Process"):
                                    for key in thinking_keys:
                                        st.markdown(f"**{key.replace('_', ' ').title()}:**")
                                        st.write(data[key])

                            # Show final output
                            for key in output_keys:
                                st.markdown(f"### {key.title()}")
                                
                                val = data[key]
                                if isinstance(val, str):
                                    st.markdown(val)
                                else:
                                    st.write(val)
                        else:
                            st.write(data)

                    except json.JSONDecodeError:
                        st.error("Response was not valid JSON. Showing raw body:")
                        st.code(r.text or "<empty body>")

            except httpx.RequestError as e:
                st.error(f"Request failed: {e}")
    else:
        st.info("Enter a request and click 'Run Analysis' to see results here.")
