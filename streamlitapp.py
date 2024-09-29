import streamlit as st
import requests
import json

# Streamlit app title
st.title("Blog Generator with AWS Lambda")

# Input form for the blog topic
blog_topic = st.text_input("Enter the blog topic:")


if st.button("Generate Blog"):
    if blog_topic:
        # Define the API Gateway URL (replace with your actual URL)
        api_url = "https://29wadwilv8.execute-api.us-east-1.amazonaws.com/dev/blog-generation"

        # Create the request payload
        payload = {
            "blog_topic": blog_topic
        }

        try:
            # Send POST request to the API Gateway
            response = requests.post(api_url, json=payload)

            # Check if the response is successful
            if response.status_code == 200:
                response_data = response.json()
                
                # Check if the blog is present in the response
                if 'blog' in response_data:
                    generated_blog = response_data['blog']
                    
                    # Display the generated blog
                    st.subheader("Generated Blog:")
                    st.write(generated_blog)
                else:
                    st.error("Blog content not found in the response.")

            else:
                st.error(f"Error: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"Error generating blog: {e}")
    else:
        st.error("Please enter a blog topic!")
