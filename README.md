# NLI_with_csv
This repository contains a Streamlit app that allows users to upload a CSV file, display its top 5 rows, and interact with a chatbot powered by LangChain.

## Getting Started

### Prerequisites

Make sure you have [Anaconda](https://www.anaconda.com/products/distribution) installed.


### Installation

1. Clone the repository:
``` git clone https://github.com/gowthaml15/NLI_with_csv.git ```

2. Navigate to the project directory:
``` cd NLI_with_csv ```

3. Create a Conda environment:
``` conda create --name NLI_with_csv python=3.10```

4. Activate the Conda environment:
``` conda activate NLI_with_csv ```

5. Install the required packages:
``` pip install -r requirements.txt ```

### Usage
1. Run the Streamlit app:
``` streamlit run src/main.py ```

2. Open your web browser and go to **http://localhost:8501** to interact with the app.

### Folder Structure
Explain the structure of your project's folders and briefly describe the purpose of each major folder.
```
/streamlit-chat-app
│
├── main.py      # Streamlit app code
├── utils/       # Utility functions or modules
├── uploads/     # Folder for uploaded files
├── .env         # Environment variable configuration
├── README.md    # Project documentation
└── ...
```