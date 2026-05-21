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
    allow_origins=['*'],          # or ["*"] for all
    allow_credentials=False,
    allow_methods=["POST"],            # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],            # Allow all headers
)
import json
@app.post("/plan_workout")
def plan_workout(input_data: Input_Schema):
    try:
        response  = useAI(input_data.model_dump())
        if isinstance(response, dict) and "error" in response:
            raise HTTPException(status_code=422, detail=response["error"])
        with open('response.json', 'w', encoding='utf-8') as f:
            json.dump(response, f, ensure_ascii=False, indent=4)
        return JSONResponse(status_code=200, content=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
#python -m uvicorn main:app --reload
#ngrok http 8000