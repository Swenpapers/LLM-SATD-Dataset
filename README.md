# LLM-SATD-Dataset

## 📖 Overview
This repository contains a dataset of **Self-Admitted Technical Debt (SATD)** found in open-source **LLM-based projects**. 
## 📖 Abstract
Large Language Models (LLMs) are increasingly integrated into software systems through APIs such as **OpenAI**, enabling developers to leverage advanced AI capabilities with minimal infrastructure. However, these integrations introduce **unique technical debt challenges**, particularly **Self-Admitted Technical Debt (SATD)**, where developers explicitly acknowledge unresolved issues in their code.  

This study presents the **first empirical investigation into LLM-specific SATD**, examining:
- The **new technical debt challenges** introduced by LLMs.
- The **problem areas** where LLM-based systems accumulate debt.
- Potential **strategies to mitigate** LLM-specific SATD.  

We analyzed **93,142 Python files** across prominent LLM APIs and found a **notable prevalence of SATD**:
- **54.49%** of SATD instances originate from OpenAI-based integrations.
- **12.35%** of SATD instances stem from the use of the **LangChain framework**.  

Our findings highlight that **prompt design** is the **primary contributor** to LLM-specific SATD, with:
- **6.61%** of debt related to **prompt configuration and optimization issues**.
- Additional SATD arising from **hyperparameter tuning** and **LLM-framework integration**.  

Furthermore, we analyzed **prompt engineering techniques** to determine which are most prone to SATD:
- **Instruction-based prompts** accounted for **38.60%** of SATD cases, primarily due to issues with clarity and verbosity.
- **Few-shot prompting** contributed to **18.13%** of SATD cases, highlighting the challenges in selecting high-quality examples.  


## 📊 Citation
If you use this dataset in your research, please cite the **anonymous repository**:

🔗 **[Anonymous GitHub](https://anonymous.4open.science/r/LLM-SATD-Dataset/)**

## 📜 License
This dataset is released under the **MIT License** and is available for research and educational purposes.


