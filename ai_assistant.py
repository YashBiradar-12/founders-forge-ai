import ollama
import streamlit as st

st.set_page_config(
    page_title="Startup Coach AI",
    page_icon="🚀",
    layout="wide"
)

with st.sidebar:
    st.header("🚀 Startup Coach AI")

    st.write("""
    Get guidance on:

    • Startup Ideas

    • Business Models

    • Marketing

    • Growth Strategy

    • Sales

    • Business Plans
    """)

st.title("🚀 Startup Coach AI")

st.caption(
    "Validate ideas, build businesses and think like a founder."
)

category = st.selectbox(
    "Choose a category",
    [
        "Startup Idea Validation",
        "Business Model",
        "Marketing",
        "Growth Strategy",
        "Business Plan Generator",
        "General Startup Advice"
    ]
)

question = st.text_area(
    "Describe your startup idea or challenge",
    height=150
)

def startup_coach(question, category):

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": f"""
                You are an experienced startup mentor.

                Category: {category}

                Rules:
                - Be practical.
                - Be realistic.
                - Give actionable advice.
                - Use bullet points.
                - Think like a founder.

                If generating a business plan,
                include:

                1. Problem
                2. Solution
                3. Target Audience
                4. Revenue Model
                5. Marketing Strategy
                6. Risks
                7. Next Steps
                """
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]

if st.button("🚀 Get Advice"):

    if question.strip():

        with st.spinner("Analyzing..."):
            answer = startup_coach(
                question,
                category
            )

        st.success("Analysis Complete")

        st.markdown("## 💡 Startup Coach Response")

        st.write(answer)