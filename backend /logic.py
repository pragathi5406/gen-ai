ef calculate_financials(data):
    income = float(data.get("income", 0))
    expenses = float(data.get("expenses", 0))
    savings = float(data.get("savings", 0))
    age = int(data.get("age", 25))
    goal = data.get("goal", "General")

  
    monthly_savings = income - expenses
    savings_rate = (monthly_savings / income) * 100 if income > 0 else 0

   
    score = 0

    if savings_rate >= 40:
        score += 40
    elif savings_rate >= 20:
        score += 25
    else:
        score += 10

    if expenses < income * 0.6:
        score += 30
    else:
        score += 15

    if savings > income * 6:
        score += 30
    else:
        score += 10

    
    if age < 30:
        risk = "High"
    elif age < 50:
        risk = "Medium"
    else:
        risk = "Low"

   
    future_savings = savings + (monthly_savings * 60)

   
    sip = max(monthly_savings * 0.4, 0)

   
    if goal == "house":
        goal_advice = f"To buy a house, invest ₹{int(sip)} monthly for long-term growth."
    elif goal == "car":
        goal_advice = f"Save aggressively. Invest ₹{int(sip)} monthly for your car goal."
    elif goal == "retirement":
        goal_advice = f"Start early. Invest ₹{int(sip)} monthly for retirement."
    else:
        goal_advice = "Maintain a balanced saving and investment strategy."

  
    return {
        "monthly_savings": monthly_savings,
        "savings_rate": round(savings_rate, 2),
        "score": score,
        "risk": risk,
        "future_savings": int(future_savings),
        "sip": int(sip),
        "goal_advice": goal_advice
    }
