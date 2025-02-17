import io
import requests
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from langchain_huggingface import HuggingFacePipeline

def extract_code_from_local_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading local code file: {e}"

def extract_code_from_web_file(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error reading web code file: {e}"

def main():
    print(r"""
                                                                          
@@@  @@@  @@@ @@@  @@@@@@@   @@@@@@@@  @@@@@@@   @@@   @@@@@@   @@@  @@@  
@@@  @@@  @@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@@@@@@  @@@@ @@@  
@@!  @@@  @@! !@@  @@!  @@@  @@!       @@!  @@@  @@!  @@!  @@@  @@!@!@@@  
!@!  @!@  !@! @!!  !@!  @!@  !@!       !@!  @!@  !@!  !@!  @!@  !@!!@!@!  
@!@!@!@!   !@!@!   @!@@!@!   @!!!:!    @!@!!@!   !!@  @!@  !@!  @!@ !!@!  
!!!@!!!!    @!!!   !!@!!!    !!!!!:    !!@!@!    !!!  !@!  !!!  !@!  !!!  
!!:  !!!    !!:    !!:       !!:       !!: :!!   !!:  !!:  !!!  !!:  !!!  
:!:  !:!    :!:    :!:       :!:       :!:  !:!  :!:  :!:  !:!  :!:  !:!  
::   :::     ::     ::        :: ::::  ::   :::   ::  ::::: ::   ::   ::  
 :   : :     :      :        : :: ::    :   : :  :     : :  :   ::    :

Created by Alican Kiraz

    """)
    print("\nPlease specify the source of the code file.")
    source_type = input("Local or Web? (Local/Web): ").strip().lower()
    code_text = ""
    if source_type.startswith("l"):
        file_path = input("Enter the local code file path (e.g., /path/to/file.swift or /path/to/file.cs): ").strip()
        code_text = extract_code_from_local_file(file_path)
    elif source_type.startswith("w"):
        code_url = input("Enter the code file URL: ").strip()
        code_text = extract_code_from_web_file(code_url)
    else:
        print("Invalid choice! Please specify 'Local' or 'Web'.")
        return
    if code_text.startswith("Error"):
        print(code_text)
        return
    quant_choice = input("Do you want to use quantization? (No/4bit/8bit): ").strip().lower()
    print("\nWhich Seneca LLM version would you like to use?")
    print("1. AlicanKiraz0/Seneca-x-DeepSeek-R1-Distill-Qwen-32B-v1.3-Safe")
    print("2. AlicanKiraz0/SenecaLLM-x-Llama3.1-8B")
    model_choice = input("Enter 1 or 2: ").strip()
    if model_choice == "1":
        model_name = "AlicanKiraz0/Seneca-x-DeepSeek-R1-Distill-Qwen-32B-v1.3-Safe"
    elif model_choice == "2":
        model_name = "AlicanKiraz0/SenecaLLM-x-Llama3.1-8B"
    else:
        print("Invalid choice! Defaulting to 'AlicanKiraz0/SenecaLLM-x-Llama3.1-8B'.")
        model_name = "AlicanKiraz0/SenecaLLM-x-Llama3.1-8B"
    print("\nLoading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    try:
        if quant_choice in ["4bit", "4", "fourbit"]:
            model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", load_in_4bit=True)
        elif quant_choice in ["8bit", "8", "eightbit"]:
            model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", load_in_8bit=True)
        else:
            model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
    except Exception as e:
        print(f"Error loading model: {e}")
        return
    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_new_tokens=256, temperature=0.2, repetition_penalty=1.2, no_repeat_ngram_size=2, do_sample=True, top_p=0.9, top_k=40)
    llm = HuggingFacePipeline(pipeline=pipe)
    system_instruction = """[System note]
You are a strict application security auditor. Your task is to analyze the provided source code for potential security vulnerabilities, such as SQL injections, insecure API usage, hardcoded credentials, improper error handling, and other security misconfigurations. Do not provide additional commentary beyond the security analysis. If no vulnerabilities are found, simply state "No security vulnerabilities found."
[/System note]
"""
    user_message = f"""[User message]
Below is the source code extracted from a file:

--- CODE START ---
{code_text}
--- CODE END ---

Perform a comprehensive security analysis of the above code. Identify any potential vulnerabilities, risky coding practices, or security misconfigurations that could lead to exploitation. Provide your analysis in English. If no issues are found, state "No security vulnerabilities found."
[/User message]
"""
    prompt = system_instruction + "\n" + user_message
    response = llm.invoke(prompt)
    print("\n[/User message]\nAnalysis Results:\n")
    print(response.strip())
    print("\ncreated by alican kiraz")

if __name__ == "__main__":
    main()
