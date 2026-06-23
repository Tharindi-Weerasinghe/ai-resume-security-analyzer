import re
import spacy

nlp = spacy.load("en_core_web_sm")

BAD_WORDS = [
    "skills", "references", "education", "certifications", "learning",
    "analytical skills", "active learner", "communication", "teamwork",
    "projects", "professional profile", "profile", "sql", "linux",
    "socket programming"
]

def clean_text(value):
    value = value.replace("\n", " ").strip()
    value = re.sub(r"\s+", " ", value)
    return value

def is_bad_entity(value):
    lower = value.lower()

    if len(value) < 3:
        return True

    if "@" in lower:
        return True

    if "linkedin.com" in lower or "github.com" in lower or "www." in lower:
        return True

    for word in BAD_WORDS:
        if word in lower:
            return True

    return False

def extract_candidate_name(text):
    lines = text.split("\n")

    for line in lines[:10]:
        line = clean_text(line)

        if not line:
            continue

        if "@" in line or "http" in line or "www" in line:
            continue

        words = line.split()

        if 2 <= len(words) <= 4:
            if all(word.replace(".", "").isalpha() for word in words):
                return line

    return "Not detected"

def extract_entities(text):
    doc = nlp(text)

    entities = {
        "PERSON": [],
        "ORG": [],
        "GPE": []
    }

    candidate_name = extract_candidate_name(text)

    if candidate_name != "Not detected":
        entities["PERSON"].append(candidate_name)

    for ent in doc.ents:
        if ent.label_ in entities:
            cleaned = clean_text(ent.text)

            if not is_bad_entity(cleaned):
                if cleaned not in entities[ent.label_]:
                    entities[ent.label_].append(cleaned)

    return entities