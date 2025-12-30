import json
import httpx
import streamlit as st

st.title("Imaging LLM Agent")

api_url = st.text_input("API URL", "http://127.0.0.1:8000/run")
text = st.text_area("Request", height=120)

if st.button("Run"):
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
                st.code(json.dumps(data, indent=2), language="json")
            except json.JSONDecodeError:
                st.error("Response was not valid JSON. Showing raw body:")
                st.code(r.text or "<empty body>")

    except httpx.RequestError as e:
        st.error(f"Request failed: {e}")
