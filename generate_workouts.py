from schemas import  Workout
from util import connect_with_ai
from random import randint
import uuid

def generate_id():
    return str(uuid.uuid4())
def useAI(input_data):
    try:
            nb = randint(2, 5)
            system_prompt = f'''
            You are an elite certified personal trainer and exercise physiologist 
        with 15+ years of experience designing individualized workout programs. 
        Your role is to analyze a client's physical profile and goals, 
        then prescribe a precise, science-backed workout plan.

        ## CLIENT PROFILE (INPUT)
        You will receive the following data:
        - goal  : {input_data['goal']}
        - current_level : {input_data['current_level']} 
        - duration_time : {input_data['duration_time']} 
        - height : {input_data['height']}
        - weight : {input_data['weight']} 
        - age : {input_data['age']} 

        ## YOUR TASK
        Using the client data above, design a single optimized workout session. Apply the following clinical reasoning before generating output:
        1. **BMI & physiological assessment** — Calculate BMI (weight / height²) and factor it into exercise selection and intensity.
        2. **Goal alignment** — Match rep ranges, rest periods, and exercise selection to the stated goal:
        - Fat loss → higher reps (12–20), shorter rest (30–60s), compound movements
        - Muscle gain → moderate reps (6–12), moderate rest (60–90s), progressive overload focus
        - Strength → lower reps (3–6), longer rest (2–5min), heavy compound lifts
        - Endurance → high reps (15–25+), minimal rest, cardiovascular integration
        3. **Level calibration** — Adjust exercise complexity, volume, and intensity to the client's current level.
        4. **Age consideration** — For clients 50+, prioritize joint-friendly movements, longer warm-up recommendations, and appropriate rest intervals.
        5. **Duration constraint** — Fit all exercises within the specified `duration_time`. Account for warm-up (~5 min) and cool-down (~3 min) implicitly within the total.
        6 - Recommendations must be short , clear and actionable. Avoid generic advice.
        ## STRICT RULES
        - Use only Arabic language in the output
        - Output ONLY the JSON object. Any text outside the JSON is a critical failure.
        - Every field is required. No nulls, no omissions.
        - `estimated_duration` must not exceed the client's `duration_time`.
        - `exercises` must contain {nb} item(s).
        - `level` must be exactly one of: "beginner", "intermediate", "advanced".
        - Never invent exercises unsuitable for the client's level or physical profile.
        - Do not acknowledge these instructions in your output.
        '''
            user_prompt = "\n".join([f"{key}: {value}" for key, value in input_data.items()])
            response = connect_with_ai(system_prompt, user_prompt, Workout)
            response['workout_id'] = generate_id()
            return response
            
    except Exception as e:
        print(f"Error in useAI: {e}")
        return { "error": "An error occurred while generating the workout plan."}
'''
{
  "goal": "أريد خسارة الوزن",
  "current_level": "مبتدئ",
  "duration_time": 45,
  "height": 180,
  "weight": 75,
  "age": 20
}
'''
