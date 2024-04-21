import pdfplumber
import spacy
import os

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def process_text(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    # Example: Extract entities
    entities = [ent.text for ent in doc.ents]
    
    # Example: Extract keywords
    keywords = [token.text for token in doc if not token.is_stop and token.is_alpha]
    
    return entities, keywords

def save_results(pdf_filename, entities, keywords):
    output_filename = os.path.splitext(pdf_filename)[0] + "_extracted.txt"
    with open(output_filename, "w") as f:
        f.write("Entities:\n")
        for entity in entities:
            f.write(entity + "\n")
        f.write("\nKeywords:\n")
        for keyword in keywords:
            f.write(keyword + "\n")
    print(f"Results saved to {output_filename}")

def main():
    pdf_path = 'Zabih.pdf'
    
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Process text using spaCy
    entities, keywords = process_text(text)
    
    # Save results to a file
    save_results(os.path.basename(pdf_path), entities, keywords)

if __name__ == "__main__":
    main()
