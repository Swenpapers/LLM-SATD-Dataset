
import json
import os
import csv
import tokenize
from io import StringIO

json_dir = '~/SATD_Transfomer/promptset_as_json'
output_csv = 'comments_with_api_calls.csv'
error_log = 'error_log.csv'

api_keywords = {
    "OpenAI": ["openai", "OpenAI", "openai.Completion.create", "openai.ChatCompletion.create", "openai.Completion", "openai.ChatCompletion"],
    "Anthropic": ["anthropic", "Claude", "anthropic.Completion.create", "claude.Completion"],
    "Cohere": ["cohere", "cohere.Client", "cohere.generate", "cohere.chat", "cohere.summarize"],
    "LangChain": ["langchain", "LLMChain", "PromptTemplate", "HumanMessage", "AIMessage", "BaseTool", "@tool", "langchain.llms"]
}

def detect_api_calls(file_contents):
    detected_apis = []
    for api, keywords in api_keywords.items():
        if any(keyword in file_contents for keyword in keywords):
            detected_apis.append(api)
    return detected_apis if detected_apis else ["Unknown"]

def extract_single_line_comments(file_contents, file_name):
    comments = []
    try:
        tokens = tokenize.generate_tokens(StringIO(file_contents).readline)
        for token_type, token_string, _, _, _ in tokens:
            if token_type == tokenize.COMMENT:  
                comments.append(token_string)
    except Exception as e:
        print(f"Error processing {file_name}: {e}")
        log_error(file_name, str(e))
    return comments if comments else ["No_Comments_in_this_file"]

def log_error(file_name, error_message):
    with open(error_log, mode='a', newline='', encoding='utf-8') as log_file:
        log_writer = csv.writer(log_file)
        log_writer.writerow([file_name, error_message])

with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(["File Path", "Comment", "API Call Types"])  # Write header row
    for json_file in os.listdir(json_dir):
        if json_file.endswith(".json"):
            json_file_path = os.path.join(json_dir, json_file)
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                file_contents = data["File Contents"]

                comments = extract_single_line_comments(file_contents, json_file)

                api_call_types = detect_api_calls(file_contents)
                api_call_types_str = ", ".join(api_call_types)  
                
                for comment in comments:
                    writer.writerow([
                        json_file_path,
                        comment.replace('\n', ' ').replace('\r', ''),  
                        api_call_types_str
                    ])

print(f"CSV file has been created: {output_csv}")
print(f"Error log has been created: {error_log}")
