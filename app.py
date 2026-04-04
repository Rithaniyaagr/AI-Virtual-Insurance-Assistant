# app.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI(title="AI Gig Worker Insurance System 🚀")

# -------------------------------
# CORS
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# LOAD DATASET
# -------------------------------
DATA_PATH = "members_full.csv"

df = pd.read_csv(DATA_PATH)

# Clean data
df.fillna(0, inplace=True)

# 🔥 FIX: ensure member_id is integer
df['member_id'] = df['member_id'].astype(int)

print("✅ Dataset Loaded:", len(df), "records")


# -------------------------------
# CORE LOGIC FUNCTIONS
# -------------------------------

def calculate_premium(row):
    premium = row.get('premium_paid', 0)

    if row.get('avg_rainfall_region', 0) > 70:
        premium += 10
    if row.get('avg_aqi_region', 0) > 200:
        premium += 15
    if row.get('natural_disaster_risk', 0) > 6:
        premium += 20
    if row.get('previous_claims', 0) > 2:
        premium += 25

    return int(premium)


def calculate_claim_probability(row):
    score = 0

    score += row.get('previous_claims', 0) * 10
    score += row.get('natural_disaster_risk', 0) * 5
    score += row.get('avg_aqi_region', 0) / 10
    score += row.get('avg_rainfall_region', 0) / 5

    return round(min(score, 100), 2)


def calculate_fraud_risk(row):
    score = 0

    if row.get('previous_claims', 0) > 3:
        score += 40

    if row.get('days_since_last_claim', 999) < 30:
        score += 30

    if row.get('claim_amount_last', 0) > 10000:
        score += 30

    return min(score, 100)


def calculate_worker_scores(row):
    return {
        "app_usage_score": min(10, int(row.get('app_usage_score', 5))),
        "feedback_score": min(10, int(row.get('feedback_score', 5))),
        "loyalty_score": min(10, int(row.get('loyalty_score', 5)))
    }


def calculate_risk_level(prob, fraud):
    if prob > 70 or fraud > 70:
        return "High"
    elif prob > 40:
        return "Medium"
    return "Low"


def auto_claim_logic(row):
    if row.get('avg_rainfall_region', 0) > 85:
        return {"payout": 300, "reason": "Heavy Rain"}
    elif row.get('avg_aqi_region', 0) > 350:
        return {"payout": 200, "reason": "Severe Pollution"}
    elif row.get('natural_disaster_risk', 0) > 8:
        return {"payout": 500, "reason": "Natural Disaster"}
    return {"payout": 0, "reason": "No Trigger"}


def explain_risk(row, prob, fraud):
    reasons = []

    if row.get('previous_claims', 0) > 2:
        reasons.append("Frequent claims")

    if row.get('avg_aqi_region', 0) > 200:
        reasons.append("High pollution")

    if row.get('natural_disaster_risk', 0) > 6:
        reasons.append("Disaster-prone area")

    if fraud > 60:
        reasons.append("High fraud risk")

    return reasons


def calculate_days_left(row):
    try:
        end_date = pd.to_datetime(row.get('policy_end_date'))
        return int((end_date - pd.Timestamp.now()).days)
    except:
        return 0


# -------------------------------
# API ENDPOINTS
# -------------------------------

@app.get("/")
def home():
    return {"message": "AI Insurance Backend Running 🚀"}


@app.get("/member/{member_id}")
def get_member(member_id: int):
    print("🔍 Searching ID:", member_id)

    member = df[df['member_id'] == member_id]

    if member.empty:
        raise HTTPException(status_code=404, detail="Member not found")

    row = member.iloc[0].to_dict()

    # Calculations
    predicted_premium = calculate_premium(row)
    claim_prob = calculate_claim_probability(row)
    fraud_risk = calculate_fraud_risk(row)
    worker_scores = calculate_worker_scores(row)
    risk_level = calculate_risk_level(claim_prob, fraud_risk)
    auto_claim = auto_claim_logic(row)
    reasons = explain_risk(row, claim_prob, fraud_risk)
    days_left = calculate_days_left(row)

    return {
        **row,
        "predicted_premium": predicted_premium,
        "claim_probability": claim_prob,
        "fraud_risk_score": fraud_risk,
        "risk_level": risk_level,
        "worker_scores": worker_scores,
        "auto_claim": auto_claim,
        "risk_reasons": reasons,
        "days_left": days_left
    }


@app.get("/risk/{member_id}")
def risk_details(member_id: int):
    member = df[df['member_id'] == member_id]

    if member.empty:
        raise HTTPException(status_code=404, detail="Member not found")

    row = member.iloc[0].to_dict()

    prob = calculate_claim_probability(row)
    fraud = calculate_fraud_risk(row)

    return {
        "claim_probability": prob,
        "fraud_risk_score": fraud,
        "risk_level": calculate_risk_level(prob, fraud),
        "reasons": explain_risk(row, prob, fraud)
    }


@app.get("/claim/{member_id}")
def claim(member_id: int):
    member = df[df['member_id'] == member_id]

    if member.empty:
        raise HTTPException(status_code=404, detail="Member not found")

    row = member.iloc[0].to_dict()

    return auto_claim_logic(row)


@app.get("/premium/{member_id}")
def premium(member_id: int):
    member = df[df['member_id'] == member_id]

    if member.empty:
        raise HTTPException(status_code=404, detail="Member not found")

    row = member.iloc[0].to_dict()

    return {
        "predicted_premium": calculate_premium(row)
    }