from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load model once
tokenizer = AutoTokenizer.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
model = AutoModelForSeq2SeqLM.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")


def explain_topic(topic: str) -> str:
    try:
        input_text = f"Explain the concept of '{topic}' in simple words for a school student."

        inputs = tokenizer(input_text, return_tensors="pt")

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=150,
                do_sample=True,
                temperature=0.7,
                top_k=50,
                top_p=0.95
            )

        return tokenizer.decode(outputs[0], skip_special_tokens=True)

    except Exception as e:
        return f"⚠️ Error in Explanation: {e}"
