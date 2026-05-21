from pydantic import BaseModel, Field
from typing import List, Literal

class Input_Schema(BaseModel):
    goal: str = Field(..., description="Client's fitness goal (e.g., fat loss, muscle gain, strength, endurance)")
    currentLevel: str = Field(..., description="Client's current fitness level (e.g., beginner, intermediate, advanced)")
    weight: float = Field(..., gt=0, description="Client's weight in kilograms")
    age: int = Field(..., gt=0, description="Client's age in years")
class Exercise(BaseModel):
    name: str = Field(..., description="Exercise name")
    explanation: str = Field(..., description="Brief explanation of the exercise")
    sets: int = Field(..., gt=0, description="Number of sets")
    reps: int = Field(..., gt=0, description="Number of repetitions")
    rest: int = Field(..., ge=0, description="Rest time in seconds")


class Workout(BaseModel):
    title: str = Field(..., description="Workout title")
    level: Literal["مبتدئ" , "متوسط","متقدم"]
    goal: str = Field(..., description="Workout goal")
    estimatedDuration: int = Field(
        ..., gt=0, description="Estimated duration in minutes"
    )
    exercises: List[Exercise] = Field(
        ..., 
        min_length=1,
        max_length=5,
        description="List of one or more exercises"
    )
    recommendations: List[str] = Field(..., description="Additional recommendations for the workout")