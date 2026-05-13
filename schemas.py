from pydantic import BaseModel, Field
from typing import List, Literal

class Input_Schema(BaseModel):
    goal: str = Field(..., description="Client's fitness goal (e.g., fat loss, muscle gain, strength, endurance)")
    current_level: str = Field(..., description="Client's current fitness level (e.g., beginner, intermediate, advanced)")
    duration_time: int = Field(..., gt=0, description="Total workout duration in minutes")
    height: float = Field(..., gt=0, description="Client's height in centimeters")
    weight: float = Field(..., gt=0, description="Client's weight in kilograms")
    age: int = Field(..., gt=0, description="Client's age in years")
class Exercise(BaseModel):
    name: str = Field(..., description="Exercise name")
    sets: int = Field(..., gt=0, description="Number of sets")
    reps: int = Field(..., gt=0, description="Number of repetitions")
    rest: int = Field(..., ge=0, description="Rest time in seconds")


class Workout(BaseModel):
    title: str = Field(..., description="Workout title")
    level: Literal["beginner", "intermediate", "advanced"]
    goal: str = Field(..., description="Workout goal")
    estimated_duration: int = Field(
        ..., gt=0, description="Estimated duration in minutes"
    )
    exercises: List[Exercise] = Field(
        ..., 
        min_length=1,
        description="List of one or more exercises"
    )
    recommendations: List[str] = Field(..., description="Additional recommendations for the workout")