# AIInterviewer - AI-Based Streamlit Application

AIInterviewer is an interactive Streamlit application powered by Python, Langchain framework, and OpenAI. This application takes a job description as input and conducts a simulated technical interview by asking relevant questions. It then provides feedback on the interview performance.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **AI-Generated Questions:** Utilizes OpenAI to generate technical questions based on the given job description.
- **Interactive Interview:** Simulates a real interview experience by posing questions to the user.
- **Feedback:** Provides detailed feedback on the interview performance, highlighting strengths and areas for improvement.

## Demo

Check out the live demo: [AIInterviewer Demo](https://ainterviewer.streamlit.app/)

## Installation

1. Clone the repository:

    ```bash
    https://github.com/AIOnGraph/GPT_INTERVIEWER.git
    cd GPT_INTERVIEWER
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    # or
    .\venv\Scripts\activate  # For Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run Home.py
    ```

2. Open your browser and navigate to [http://localhost:8000](http://localhost:8000).

3. Input the job description and start the interview.

## Configuration

- **OpenAI API Key:** To use the Application, you need to obtain an API key. Set your API key in the Side Bar of Streamlit.

## Dependencies

- Python 3.8
- Langchain framework
- Streamlit
- OpenAI GPT-3.5

For a detailed list of dependencies, refer to the `requirements.txt` file.

## Contributing

We welcome contributions to AIInterviewer! If you'd like to contribute, feel free to fork the repository and make your changes. Create a pull request, and we'll review your contribution. Thank you for considering contributing to our project!
## License

This project is licensed under the [MIT License](https://github.com/AIOnGraph/GPT_INTERVIEWER/blob/main/LICENSE.txt).
