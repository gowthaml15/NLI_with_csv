from utils.imports import *

load_dotenv(".env")
os.environ["OPENAI_API_KEY"] = os.getenv('OpenAI-API-Key')

# Create a placeholder for chat messages
chat_messages = []

def get_response_llm(file, question):
    llm = OpenAI()
    df = SmartDataframe(file, config={"llm": llm})
    return df.chat(question)

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

        # Transition to chat mode
        st.header("Chat Mode")

    # Chat input
    user_input = st.text_area("You:", "", key="user_input")

    # Chat response
    if user_input:
        chat_messages.append(f"**You:** {user_input}")
        # Add your logic here to generate a chatbot response or any other interactions
        chat_messages.append(f"**Analyst:** {get_response_llm(df, user_input)}")

    # Show messages in the chat
    show_chat()

def remove_exports_chart():
    # Specify the path to the folder you want to remove
    folder_to_remove = "exports"

    try:
        # Attempt to remove the folder and its contents
        shutil.rmtree(folder_to_remove)
        print(f"The folder '{folder_to_remove}' has been successfully removed.")
    except Exception as e:
        print(f"An error occurred while removing the folder: {e}")


def show_chat():
    # Display chat messages with chat-like styling
    for message in chat_messages:
        if "**You:**" in message:
            st.markdown(f'<div style="text-align: right; color: #4184f3; padding: 5px;">{message}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="text-align: left; color: #4a4a4a; padding: 5px;">{message}</div>', unsafe_allow_html=True)
    
    remove_exports_chart()


if __name__ == "__main__":
    main()