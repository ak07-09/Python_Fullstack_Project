
# 🚀 **PROMPT BUILDER** 🛠️

## 📝 **Project Description**

The Prompt Builder API is a Python-based project that generates and improves text prompts using simple rule-based logic. It allows users to input minimal text (like "gaming wallpaper"), and the system expands it into a detailed, well-structured prompt. The goal of this project is to demonstrate how Python modules and API frameworks can be combined to create a useful, beginner-friendly tool for prompt generation and management.

---

## ✨ **Features**

- **Prompt Enhancement** 🪄: Takes a short input (e.g., “gaming wallpaper”) and expands it into a detailed, structured prompt using predefined rules and attributes.
- **Prompt Generation with Minimal Input** ✍️: Even if the user provides only one or two words, the system can build a creative, well-formed prompt.
- **Database Integration (Supabase)** 💾: Stores both original and improved prompts, and supports easy retrieval and management of them.
- **RESTful API Endpoints** 🌐:
    - `POST /build` → Accepts user input and returns an enhanced prompt.
    - `GET /prompts` → Fetches all stored prompts.
    - `GET /random` → Retrieves a random saved prompt (optional fun feature).
- **Category-based Expansion (Optional)** 🏷️: Adds thematic details based on category (e.g., gaming, coding, nature).
- **Validation & Error Handling** ✅: Ensures valid input (not empty) and provides clear error messages for invalid requests.
- **Interactive Documentation** 📖: Built-in Swagger UI via FastAPI, allowing users to test the API directly in the browser.
- **Lightweight & Beginner-Friendly** 🌱: Has a minimal setup that is easy to deploy, and is focused on clarity rather than complexity.

---

## 📂 **Project Structure**

# 🚀 **PROMPT BUILDER** 🛠️

## 📝 **Project Description**

The Prompt Builder API is a Python-based project that generates and improves text prompts using simple rule-based logic. It allows users to input minimal text (like "gaming wallpaper"), and the system expands it into a detailed, well-structured prompt. The goal of this project is to demonstrate how Python modules, data structures, and API frameworks can be combined to create a useful, beginner-friendly tool for prompt generation and management.

---

## ✨ **Features**

- **Prompt Enhancement** 🪄: Takes a short input (e.g., “gaming wallpaper”) and expands it into a detailed, structured prompt using predefined rules and attributes.
- **Prompt Generation with Minimal Input** ✍️: Even if the user provides only one or two words, the system can build a creative, well-formed prompt.
- **Database Integration (Supabase)** 💾: Stores both original and improved prompts, and supports easy retrieval and management of them.
- **RESTful API Endpoints** 🌐:
    - `POST /build` → Accepts user input and returns an enhanced prompt.
    - `GET /prompts` → Fetches all stored prompts.
    - `GET /random` → Retrieves a random saved prompt (optional fun feature).
- **Category-based Expansion (Optional)** 🏷️: Adds thematic details based on category (e.g., gaming, coding, nature).
- **Validation & Error Handling** ✅: Ensures valid input (not empty) and provides clear error messages for invalid requests.
- **Interactive Documentation** 📖: Built-in Swagger UI via FastAPI, allowing users to test the API directly in the browser.
- **Lightweight & Beginner-Friendly** 🌱: Has a minimal setup that is easy to deploy, and is focused on clarity rather than complexity.

---

## 📂 **Project Structure**


```

PROMPT BUILDER/
|
|---src/                 \# Core application logic
|    |---logic.py        \# Business logic for prompt operations
|    |---db.py           \# Database operations
|
|---api/                 \# Backend API
|    |---main.py         \# FastAPI endpoints
|
|---frontend/            \# Frontend application
|    |---app.py          \# Streamlit web interface
|
|---requirements.txt     \# Python dependencies
|---README.md            \# Project Documentation
|---.env                 \# Environment variables

```

---

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.8 or higher 🐍
- A Supabase account 🟢
- Git for cloning 🌳

### **1. Clone the Project**
```bash
# Option 1: Clone with git
git clone <repo-url>
````

You can also download and extract the zip file.

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Setup Supabase Database**

1.  Create a new project in your Supabase account.
2.  Go to the **SQL Editor** and run the following command to create your table:

<!-- end list -->

```sql
create table if not exists prompts (
    id bigserial primary key,
    user_input text not null,
    improved text not null,
    created_at timestamp default current_timestamp
);
```

3.  Get your **Project URL** and **API Key** from the Supabase settings. 🔑

### **4. Configure Environment Variables**

Create a `.env` file in the root directory and add your Supabase credentials:

```ini
SUPABASE_URL=YOUR_SUPABASE_URL
SUPABASE_KEY=YOUR_SUPABASE_API_KEY
```

### **5. Run the Application**

#### **Streamlit Frontend**

```bash
streamlit run frontend/app.py
```

This app will open in your browser. 🖥️

#### **FastAPI Backend**

```bash
cd api
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. 🚀

-----

## 💡 **How to Use**

*This section will be updated with usage instructions.* 📝

-----

## 💻 **Technologies Used**

  - **Frontend**: Swagger UI (auto-generated by FastAPI for API testing) 🧪
  - **Backend**: FastAPI (Python framework for building APIs) ⚡
  - **Database**: Supabase (PostgreSQL) 🐘
  - **Language**: Python 🐍

### **Key Components**

1.  **`src/db.py`**: Handles all CRUD operations with Supabase. 🔄
2.  **`src/logic.py`**: Contains the core business logic and prompt processing. 🧠

-----

## ⚠️ **Troubleshooting**

**Common issues and solutions  listed here.** 🐛

### **1. Backend (FastAPI) Issues**

- **Issue: `404 Not Found` Error** 🌐
    - **Reason:** The API server might not be running or the URL in your frontend is incorrect.
    - **Solution:** - First, verify that your FastAPI server is active by running `uvicorn main:app --reload` in your terminal.
        - Then, check that the `API_BASE_URL` in your `app.py` file is correctly set to `http://localhost:8000`.

- **Issue: `ImportError: cannot import name 'PromptDatabaseManager' from 'src.db'`** 🐍
    - **Reason:** This error occurs when your `logic.py` file is trying to import a class that isn't defined in your `db.py` file.
    - **Solution:** Confirm that your `db.py` file has the `PromptDatabaseManager` class and that all your functions are properly placed as methods within that class. Also, check for any spelling errors.

- **Issue: `500 Internal Server Error`** 💥
    - **Reason:** This is a general error that indicates an unexpected problem within your backend code, such as a database connection failure, a wrong variable name, or a typo.
    - **Solution:** Inspect the terminal where your FastAPI server is running. The specific error message will be printed there, which will help you identify the line of code that caused the problem.

---

### **2. Frontend (Streamlit) Issues**

- **Issue: `Error: Streamlit requires raw Python (.py) files...`** 💻
    - **Reason:** You are not including the `.py` extension when you run the Streamlit command.
    - **Solution:** Use the correct command `streamlit run frontend/app.py` to specify the file's extension.

- **Issue: `ConnectionError`** 🔌
    - **Reason:** The Streamlit frontend cannot connect to your FastAPI backend server.
    - **Solution:** Ensure your backend server is running in a separate terminal window. Also, verify that the `API_BASE_URL` in your `app.py` is configured as `http://localhost:8000`.

---


-----

## 📈 **Future Enhancements**

  - **AI-powered Prompt Optimization**: Integrate NLP/AI models (e.g., GPT) to intelligently improve prompts beyond rule-based logic. 🤖
  - **User Authentication**: Add login/signup via Supabase Auth so users can save and manage their own prompt history. 🔒
  - **Frontend Interface**: Build a more custom web UI (e.g., React/Next.js) for a better user experience. ✨
  - **Prompt Categories & Customization**: Allow users to select themes and customize the style, tone, and detail level of generated prompts. 🎨
  - **Export Options**: Enable downloading prompts as text, JSON, or CSV for reuse in creative tools. 📥
  - **Search & Filter**: Add search functionality to find previously stored prompts by keyword, category, or date. 🔍
  - **Rate & Improve System**: Implement a system for users to upvote/downvote prompts to help improve the enhancement rules. 👍

-----

## 🤝 **Support**

If you encounter any issues or have questions, please feel free to reach out:

  - Email: `aravind.madishetty07@gmail.com` 📧

<!-- end list -->

```
```
