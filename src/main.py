from fastapi import FastAPI

app = FastAPI()


@app.get("/calculator")
def calculator(
    num1: float,
    num2: float,
    operator: str
):
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 == 0:
            return {"error": "Cannot divide by zero"}
        result = num1 / num2

    elif operator == "**":
        result = num1 ** num2    

    elif operator == "%":
        if num2 == 0:
            return{"error": "Cannot use modulus with zero"}    
        result = num1 % num2
    else:
        return {"error": "Invalid operator"}

    return {
        "num1": num1,
        "num2": num2,
        "operator": operator,
        "result": result
    }