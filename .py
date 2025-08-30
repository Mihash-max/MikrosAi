# Install spaCy if not already installed:
# pip install spacy
# python -m spacy download en_core_web_sm

import spacy

# Load small English model
nlp = spacy.load("en_core_web_sm")

# Example text
text = "Apple is looking at buying OpenAI in San Francisco for $10 billion."

# Process text
doc = nlp(text)

# Print tokens
print("Tokens:")
for token in doc:
    print(token.text, "->", token.pos_)

# Print named entities
print("\nNamed Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)
