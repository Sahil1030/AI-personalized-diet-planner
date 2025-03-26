# AI-Personalize-Diet-Planner

## Description

**AI-Personalize-Diet-Planner** is a Streamlit-based web application that generates a **strict vegetarian Indian diet plan** based on user inputs such as height, weight, gender, and any allergies or medical conditions. It uses **Groq's AI** to personalize the diet plan, ensuring a balanced and nutritious meal recommendation.

## Features

- **User Input:** Accepts height, weight, gender, and medical conditions/allergies.
- **AI-Generated Diet Plans:** Uses Groq’s AI to create personalized meal plans.
- **Streamlit Interface:** Simple and interactive UI for user-friendly experience.
- **Customizable & Expandable:** Can be improved further with additional diet rules.

## Technologies Used

- **Python 3.12.4**
- **Streamlit** (for interactive UI)
- **Groq API** (for AI-powered diet planning)
- **dotenv** (for environment variable management)

## Installation

### **1. Clone the Repository**

```
git clone https://github.com/Sahil1030/AI-personalize-diet-planner.git
cd AI-personalize-diet-planner
```

### **2. Install Dependencies**

Ensure you have Python 3.12.4 installed, then run:

```
pip install -r requirements.txt
```

### **3. Set Up API Key**

Create a `.env` file in the project directory and add:

```
GROQ_API_KEY=your_api_key_here
```

### **4. Run the Application**

```
streamlit run FitApp.py
```

This will open the Streamlit interface in your browser.

## Usage

1. Enter your **height, weight, gender, and any allergies/medical conditions**.
2. Click the **"Generate Diet Plan"** button.
3. View your **personalized vegetarian diet plan**.

## Requirements

The application requires the following dependencies, which are listed in the `requirements.txt` file:

```
streamlit
python-dotenv
groq
```

## Contributing

Feel free to submit **pull requests** or report issues in the GitHub repository.

## License

This project is licensed under the **MIT License**.

