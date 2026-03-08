from fastapi import FastAPI
import random
from typing import List

app = FastAPI()



def generate_flight_task(
    min_points: int = 3, 
    max_points: int = 10, 
    max_distance: float = 50.0
) -> List[List[float]]:
    num_points = random.randint(min_points, max_points)
    mission = []
    
    for _ in range(num_points):
        distance = round(random.uniform(1.0, max_distance), 2)
        cargo = _generate_valid_cargo()
        
        mission.append([distance, cargo])
        
    return mission

task = generate_flight_task()

def _generate_valid_cargo() -> int:
    if random.random() < 0.5:
        return random.randint(1, 7)
    else:
        n = random.randint(1, 7)
        return 8 * (2 ** n) - 8


@app.get("/ppo_it_final")
async def root():
    global task
    return task

@app.get("/regenerate_task")
async def regen():
    global task
    task = generate_flight_task()
    return {"message": "Task regenerated", "task": task}