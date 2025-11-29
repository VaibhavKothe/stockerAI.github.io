import streamlit as st
import requests
import json
import pandas as pd
from tools.get_data import fetch_data
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="Stock Market Analysis",
    page_icon="📈",
    layout="wide"
)

# Initialize session state
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = ""

# Create two main columns
input_col, result_col = st.columns([1, 1], gap="large")

with input_col:
    st.title("📊 Market Analysis")
    
    # Model selection
    llm_model = st.selectbox(
        "Select LLM Model",
        ["llama3.2"],
        index=0
    )
    
    # Date range selector in two columns
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input(
            "Start Date",
            datetime.now() - timedelta(days=30)
        )
    with col2:
        end_date = st.date_input("End Date", datetime.now())
    
    # Analysis type
    analysis_type = st.radio(
        "Analysis Type",
        ["Trend Analysis", "Technical Indicators", "Sentiment Analysis"],
        horizontal=False
    )
    
    # Custom prompt
    user_prompt = st.text_area(
        "Analysis Prompt:",
        value="Analyze the stock market data and provide key insights on trends and patterns. Include support/resistance levels and potential trading opportunities.",
        height=150
    )
    
    # Analyze button
    if st.button("🔍 Analyze Market Data", type="primary", use_container_width=True):
        with st.spinner("Analyzing market data..."):
            try:
                # Fetch data
                stock_data = fetch_data()
                
                # Prepare the prompt
                prompt = f"""
                {stock_data}
                
                Please analyze this stock market data and provide insights on:
                1. Overall market trend
                2. Key support and resistance levels
                3. Volume analysis
                4. Any significant patterns or anomalies
                5. Potential trading opportunities

                {user_prompt}

                Be concise and focus on actionable insights.
                """
                
                # Prepare the API request
                url = "https://3c10240322a1.ngrok-free.app/v1/chat/completions"
                headers = {"Content-Type": "application/json"}
                payload = {
                    "model": llm_model,
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": True
                }
                
                # Initialize response in session state
                st.session_state.analysis_result = ""
                
                # Make the API call
                with result_col:
                    with requests.post(url, headers=headers, json=payload, stream=True) as response:
                        if response.status_code == 200:
                            response_container = st.empty()
                            full_response = ""
                            
                            for line in response.iter_lines():
                                if line:
                                    decoded_line = line.decode('utf-8')
                                    if decoded_line.startswith("data: "):
                                        data_str = decoded_line.replace("data: ", "")
                                        if data_str.strip() == "[DONE]":
                                            break
                                            
                                        try:
                                            data_json = json.loads(data_str)
                                            token = data_json['choices'][0]['delta'].get('content', '')
                                            if token:
                                                full_response += token
                                                response_container.markdown(full_response + "▌")
                                        except json.JSONDecodeError:
                                            continue
                            
                            st.session_state.analysis_result = full_response
                            response_container.markdown(full_response)
                            st.session_state.analysis_done = True
                        else:
                            result_col.error(f"Error: {response.status_code}\n{response.text}")
                            st.session_state.analysis_done = False
                
            except Exception as e:
                result_col.error(f"An error occurred: {str(e)}")
    
    # Add some styling
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            margin: 10px 0;
        }
        .stTextArea [data-baseweb=base-input] {
            min-height: 100px;
        }
        </style>
    """, unsafe_allow_html=True)

with result_col:
    st.title("Analysis Results")
    
    # Display results area
    if st.session_state.analysis_done:
        # Add download button at the top
        st.download_button(
            label="📥 Download Analysis",
            data=st.session_state.analysis_result,
            file_name=f"market_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/markdown",
            use_container_width=True
        )
        
        # Display the analysis
        st.markdown("### Market Analysis Results")
        st.markdown(st.session_state.analysis_result)
    else:
        st.info("Your analysis will appear here after you click 'Analyze Market Data'.")
        st.markdown("""
        ### Example Analysis Will Show:
        - Market trend analysis
        - Key support/resistance levels
        - Volume and price action
        - Trading opportunities
        - Risk assessment
        """)