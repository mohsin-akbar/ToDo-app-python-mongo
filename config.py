import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://mohsin68:hyBFzFTQCObkXJKo@cluster0.yva9p9c.mongodb.net/")
