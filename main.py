from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

otp_store = {}

class OTPRequest(BaseModel):
    phone: str

class OTPVerify(BaseModel):
    phone: str
    otp: str

@app.post("/send-otp")
def send_otp(request: OTPRequest):
    otp = str(random.randint(1000, 9999))
    otp_store[request.phone] = otp
    print(f"Sending OTP {otp} to {request.phone}")
    return {"message": "OTP sent successfully."}

@app.post("/verify-otp")
def verify_otp(request: OTPVerify):
    if otp_store.get(request.phone) == request.otp:
        return {"message": "OTP verified successfully."}
    raise HTTPException(status_code=400, detail="Invalid OTP")
