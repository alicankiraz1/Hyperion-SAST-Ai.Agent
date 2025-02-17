# Hyperion-SAST-Ai.Agent
<img src="https://github.com/alicankiraz1/Hyperion-SAST-Ai.Agent/blob/main/Hyperion.png" width="440" height="440">

Hyperion conducts static source code analysis on the code you share—either from the web or locally—using specialized versions of SenecaLLMs fine-tuned for cybersecurity.


## Features

- **Static Code Analysis:** Scans application code to detect potential security vulnerabilities.
- **Input Sources:** Can receive source code from local files or via the web.
- **Quantization Options:** Supports 4-bit or 8-bit quantization modes to optimize model performance.
- **Seneca LLM Integration:** Offers the ability to choose between two different Seneca LLM models.
- **Console-Based Interface:** A user-friendly interface that can be easily managed via the command line.

## Requirements

- Python 3.7 or higher
- The following Python packages:
  - transformers
  - langchain-huggingface
  - requests
  - PyPDF2 (if you will be working with PDF files)
 
## PoC

<img src="https://github.com/alicankiraz1/Hyperion-SAST-Ai.Agent/blob/main/Hyperion-PoC.gif" width="512" height="384">


## Installation

1. **Installing Dependencies**

   You can install the required packages by running the following command in the terminal or command line:

   ```bash
   pip install transformers langchain-huggingface requests PyPDF2
   ```
   
2. **Downloading the Project Files**

  You can access the project files by cloning the repository or downloading it as a zip file.

   ```bash
    git clone https://github.com/kullaniciadi/hyperion-sast-ai-agent.git
    cd hyperion-sast-ai-agent
   ```

## License
This project is licensed under the MIT License.



