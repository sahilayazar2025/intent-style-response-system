import streamlit as st

#Detecting here
def detect_intent(query: str) -> str:
    q = query.lower()

    if any(word in q for word in ["explain", "define", "theory", "concept"]):
        return "Academic"
    elif any(word in q for word in ["error", "bug", "code", "python", "debug"]):
        return "Technical"
    elif any(word in q for word in ["joke", "funny", "meme"]):
        return "Entertainment"
    elif any(word in q for word in ["i feel", "help me", "advice", "stress"]):
        return "Personal"
    else:
        return "General"



# Responses by the Base 
BASE_RESPONSES = {
    "Academic": "This topic can be understood by breaking it down into its fundamentals.",
    "Technical": "This issue can be resolved by systematically debugging the problem.",
    "Entertainment": "This response is intended to be light-hearted and engaging.",
    "Personal": "Your feelings are valid, and reaching out for support can help.",
    "General": "Here is a clear and simple explanation."
}


# To style the templates
STYLE_TEMPLATES = {
    "Overconfident Genius": "Obviously, the correct answer is simple. {}",
    "Nervous Intern": "Umm… I might be mistaken, but {}",
    "Sarcastic Reviewer": "Oh great, another question. Anyway, {}",
    "Calm Professor": "Let’s go through this step by step. {}"
}


def apply_style(base_response: str, style: str) -> str:
    template = STYLE_TEMPLATES.get(style, "{}")
    return template.format(base_response)



# The interface for Streamlit 
st.title("Intent-Aware & Style-Adaptive Response System")

query = st.text_input("Enter your query:")

show_all = st.checkbox("Show response in all styles")

selected_style = st.selectbox(
    "Choose a response style",
    list(STYLE_TEMPLATES.keys())
)

if query:
    intent = detect_intent(query)
    base_response = BASE_RESPONSES[intent]

    st.write(f"**Detected Intent:** {intent}")

    if show_all:
        st.subheader("Responses in all styles:")
        for style in STYLE_TEMPLATES:
            styled_output = apply_style(base_response, style)
            st.markdown(f"**{style}:** {styled_output}")
    else:
        final_response = apply_style(base_response, selected_style)
        st.success(final_response)
