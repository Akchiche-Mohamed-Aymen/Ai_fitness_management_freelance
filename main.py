from generate_workouts import useAI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from schemas import Input_Schema
app = FastAPI(
    title="Weight Change Prediction API",
    description="AI-powered fitness weight recommendation system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/plan_workout")
def plan_workout(input_data: Input_Schema):
    try:
        response , content = useAI(input_data.model_dump())
        if isinstance(response, dict) and "error" in response:
            raise HTTPException(status_code=422, detail=response["error"])
        return JSONResponse(status_code=200, content={"response": response, "content": content})
    except Exception as e:
        print(f"[ERROR] Workout planning failed: {e}")
        raise HTTPException(status_code=500, detail="Workout planning failed due to an internal error.")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
#python -m uvicorn main:app --reload
