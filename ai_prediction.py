from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def predict(glucose,
            haemoglobin,
            cholesterol
            ):
    prompt = f"""

    Analyze the following patient health data.

    Glucose : {glucose}
    Haemoglobin : {haemoglobin}
    Cholesterol : {cholesterol}

    Give short health remarks.
    Mention possible risks if any.
    Keep answer within 3 lines.

    """
    
    try:
        response = model.generate_content(
            prompt
        )

        return response.text
    
    except:

        remarks = []

        if glucose < 70:
            remarks.append("Low Blood Sugar")
        elif glucose > 125:
            remarks.append("High Diabetes Risk")

        if haemoglobin < 12:
            remarks.append("Possible Anemia")

        if cholesterol > 200:
            remarks.append("High Cholesterol")

        if len(remarks) == 0:
            return "Health Parameters Normal"
    
        return ",".join(remarks)

