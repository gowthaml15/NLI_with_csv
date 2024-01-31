from utils.imports import *
import streamlit as st
from streamlit_chat import message


load_dotenv("src/.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OpenAI-API-Key")


# Initialize session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []



# Sidebar - user can choose model and upload a CSV file
st.sidebar.title("Sidebar")

# Update this section
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# CSV handling logic - Update this section
if uploaded_file is not None:
    print(uploaded_file)
    df = pd.read_csv(uploaded_file)
    # You can use the DataFrame 'df' in your chat logic or display it as needed
    st.table(df.head())
    # Update this section with your desired save path
    save_path = "src/uploads/data.csv"
    st.sidebar.write(f"CSV file saved at: {save_path}")

    # Save the DataFrame to CSV
    df.to_csv(save_path, index=False)


# Generate a response function
def generate_response(prompt):
    # Generate response
    agent = create_csv_agent(
        OpenAI(temperature=0),
        os.path.join(os.getcwd(),"src/uploads/data.csv"),
        # verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    return agent.run(prompt)

# Container for chat history
response_container = st.container()
# Container for text box
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("You:", key='input', height=100)
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        output = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)


if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
