from utils.imports import *


load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OpenAI-API-Key')


def get_response_llm(file, question):
    agent = create_csv_agent(
    OpenAI(temperature=0),
    file,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)
    return agent.run(question)

# Create a placeholder for chat messages
# Create a placeholder for chat messages
chat_messages = []

def main():
    st.title("Talk with your CSV")

    # Sidebar for file upload
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

    # If a file is uploaded
    if uploaded_file is not None:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)

        # Display the top 5 rows in a compact table
        st.table(df.head())

        # Show messages in the chat
        show_chat()

        # Generate a unique filename with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_filename = f"uploaded_file_{timestamp}.csv"
        save_path = os.path.join("uploads",unique_filename)
        df.to_csv(save_path, index=False)

        # Transition to chat mode
        st.header("Chat Mode")

    # Chat input
    user_input = st.text_area("You:", "", key="user_input")

    # Chat response
    if user_input:
        chat_messages.append(f"**You:** {user_input}")
        # Add your logic here to generate a chatbot response or any other interactions
        chat_messages.append(f"**Analyst:** {get_response_llm(save_path,user_input)}")

    # Show messages in the chat
    show_chat()

def show_chat():
    # Display chat messages with chat-like styling
    for message in chat_messages:
        if "**You:**" in message:
            st.markdown(f'<div style="text-align: right; color: #4184f3; padding: 5px;">{message}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="text-align: left; color: #4a4a4a; padding: 5px;">{message}</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()