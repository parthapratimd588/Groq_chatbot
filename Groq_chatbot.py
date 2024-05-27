from groq import Groq
import streamlit as st

GROQ_API_KEY = "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"

client = Groq(
    api_key = GROQ_API_KEY,
)

system_prompt = f"""Share your response in case study writing format. Format is given below. \
\n\nFormat Style:\n
1) Introduction :\n
2) About:\n
3) Pros:atleast mandatorily give one pros\n
4) Cons:\n
5) How to avoid cons:\n
6) Conclusion:\n
7) Helpful Suggestions:\n
8) Helpful Websites:\n
"""
query = st.text_input("Input here", placeholder = "Ask me!")

if query:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": query,
            }
        ],
        model="gemma-7b-it",
    )

    response = chat_completion.choices[0].message.content

    st.markdown(":blue[Query:]")
    st.markdown(query)
    st.markdown(":green[Response: ]")
    st.markdown(response)