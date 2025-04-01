from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model():
    model_name = "meta-llama/Llama-3.2-3b"  # Updated to LLaMA 3.2 3B
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")
    return model, tokenizer

def classify_news_llama(headline, model, tokenizer):
    prompt = f"Classify the following news headline into a sector: {headline}\nSectors: Automobile, Banking, Technology, Healthcare, Energy\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output = model.generate(**inputs, max_length=50)
    classification = tokenizer.decode(output[0], skip_special_tokens=True)
    return classification.split("Answer:")[-1].strip()


model, tokenizer = load_model()


while True:
    news = input("Enter news headline (or type 'exit' to quit): ").lower() 
    if news == "exit":
        break
    print(f"{news} -> {classify_news_llama(news, model, tokenizer)}")
