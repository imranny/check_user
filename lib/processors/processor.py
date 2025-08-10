from typing import Literal
from schemas.database import UsersStageDB


def calculate_age_class(age: int) -> Literal["child", "adolescent", "adult"]:
    if age < 18:
        return "child"
    elif 18 <= age < 30:
        return "adolescent"
    else:
        return "adult"

def user_to_json(user_db: UsersStageDB) -> dict:
    return {
        "id": user_db.id,
        "name": user_db.name,
        "age": user_db.age,
        "sex": user_db.sex,
        "job": user_db.job,
        "age_class": calculate_age_class(user_db.age)
    }