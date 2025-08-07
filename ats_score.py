def calculate_ats_score(resume_text, keywords):
    matched_keywords = [kw for kw in keywords if kw.lower() in resume_text.lower()]
    score = int((len(matched_keywords) / len(keywords)) * 100)
    return score
