# qna-llm-fall2024: 🎓 Q&A Chatbot for Creation & Evolution

Welcome to the Q&A Chatbot repository of Nayoung!

This project is dedicated to the Creation & Evolution course, a compulsory liberal elective at Handong Global University (HGU). 🚀
It was started in the 2024 fall semester, and most members were recruited from Professor Chun's Deep Learning course.
The chatbot answers questions based on topics related to Creationism or Intelligent Design 🧬 using the OpenAI API.

This repository aims to provide a deep understanding of fundamental LLM concepts and Retrieval-Augmented Generation (RAG). Follow the `0*-<topic>.ipynb` prefix for fundamental practices.

---

### 💡 Key Features

* 🤖 **AI-Powered Answers**: Leveraging the OpenAI API to provide intelligent responses.
* 📂 **Structured Repository**:
  - **basic/**: Practice notebooks for LLM fundamentals (e.g., persona, few-shot learning).
  - **rag/**: Notebooks for building a RAG system, including the `chroma_db` directory.
  - **result/**: Screenshots and comparison files (txt/md) showcasing responses from ChatGPT and the custom LLM.
  - **prototype.py**: Launch the chatbot UI with Streamlit.
* 📅 **Project Deadline**: December 31st, 2024.
* ⚙️ **Environment Setup**: Manage dependencies seamlessly with Conda and a yaml environment file.

---

### 🛠️ Setup Instructions

**Clone the Repository:**

1. `git clone <repository-url>`
2. `cd <repository-folder>`

**Activate Conda Environment:**

1. Install and activate the environment from the provided yaml file:
   ```bash
   conda env create -f environment.yaml
   conda activate llm
   ```

**Setup OpenAI API Key:**

1. Add your API key securely using the terminal:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

**Launch Chatbot UI:**

1. Run the following command to start the Streamlit app:
   ```bash
   streamlit run prototype.py
   ```
2. Open [http://localhost:8501](http://localhost:8501) in your browser and enter your OpenAI API key in the sidebar.

---

### 🧠 How It Works

This chatbot addresses topics related to Creationism and Intelligent Design (지적설계론) using the OpenAI GPT API to generate accurate, context-aware responses.

The repository is organized into three main directories:

1. **basic/**: Fundamentals of LLM practices (e.g., persona, few-shot learning).
2. **rag/**: Study and implementation of RAG systems, with a `chroma_db` directory for database-related tasks.
3. **result/**: Outputs and comparisons of chatbot responses.

The top-level file `prototype.py` enables launching the chatbot UI via Streamlit.

**Personal Focus Topic:**

As part of this project, my specific focus is **"9. 진화론을 반박하는 강력한 증거, 화석"**, exploring how fossil evidence can challenge evolutionary theory and support Creationism or Intelligent Design perspectives.

---

### 🎯 Objectives

The goal of this project is to:

* Develop a user-friendly chatbot for answering key questions about Creation & Evolution.
* Build technical expertise by applying LLM models to a practical project.
* Complete and deliver the project by December 31st, 2024.

---

### 📄 Dependencies

Ensure the following are installed:

* Python (>= 3.9)
* Conda (>= 4.10)
* OpenAI API Key

For all dependencies, refer to `environment.yaml`.

---

### 🚀 Future Improvements

1. Add a user-friendly UI for the chatbot.
2. Enhance the model to support multi-lingual answers.
3. Integrate additional resources for a broader knowledge base.

---

### 🤝 Acknowledgments

* **Professor Chun 🌟**:
  - Led the LLM study group with exceptional guidance.
  - Managed each member's progress, provided inspiration, and delivered outstanding lectures on LLM and RAG fundamentals.
  - Offered valuable outlines that shaped and streamlined the project's development.
* **Powered by OpenAI API.**
* **Project proudly developed for HGU Creation & Evolution Course.**
