# 🏋️ AI-Based Fitness Coaching Assistant

An intelligent, LLM-powered fitness coaching system that generates personalized workout plans based on a client's physical profile and goals.



## 🧠 How It Works

The system uses a **structured LLM pipeline**:

1. The user submits their profile as a JSON input
2. The LLM (acting as a certified personal trainer) reasons over the profile
3. A validated JSON workout plan is returned, strictly conforming to the output schema

```
User Profile (JSON)
      │
      ▼
  System Prompt (Trainer persona + schema rules)
      │
      ▼
  LLM (gemeni-2.5)
      │
      ▼
  Workout Plan (strict JSON output)
```


## 🚀 Quick Start

### 1. Prerequisites

- Python 3.9+

### 2. Installation

```bash
git https://github.com/Akchiche-Mohamed-Aymen/Ai_fitness_management_freelance.git
cd Ai_fitness_management_freelance
pip install -r requirements.txt
```


 
### 3. Set Your API Key
 
Create a `.env` file in the project root:
 
```bash
GEMINI_KEY = your-key-here
```
 
> 🔑 **Get your key:** Go to [Google AI Studio](https://aistudio.google.com/app/apikey) → **Create API key** → copy and paste it above.

## 🗂️ Project Structure

```
fitness-coaching-assistant/
├
├── schemas/
├── ai.py                         
├── generate_workouts.py                         
├── key.py                         
├── main.py                         # Entry point
├── util.py                         # reusable code
├── requirements.txt
└── README.md
```
### 4. Starting Running The APP
```bash
python -m uvicorn main:app --reload
```
## 🛣️ Roadmap

- **Phase 1** ✅ — LLM workout plan generation with strict JSON schema
- **Phase 2** — ML prediction models (injury risk, recovery time) + LLM explanations
- **Phase 3** — Unified REST API (FastAPI) wrapping both LLM and prediction layers
- **Phase 4** — Full coaching system: progress tracking, adaptive plan evolution, user history

