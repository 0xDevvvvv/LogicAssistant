import requests # type: ignore
from prompts import sysprompts,sysprompts_json
import json
from dotenv import load_dotenv
import os


load_dotenv()
GROQ_KEY = os.getenv('GROQ_KEY')
GROQ_URL = os.getenv('GROQ_URL')

    
def send_request(system_prompt, user_content):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {GROQ_KEY}'}
    
    r = requests.post(GROQ_URL, json={
        "model": "llama-3.3-70b-versatile",
        
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]
    }, headers=headers)

    response_json = r.json()
    
    if 'choices' in response_json and len(response_json['choices']) > 0:
        content = response_json['choices'][0]['message']['content']
        print(content)
        return content
    else:
        return("")
    
def send_request_json(sysprompt,user_content):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {GROQ_KEY}'}
    print("hereeeeeeeeeeee")
    r = requests.post(GROQ_URL, json={
        "temperature":1.5,
        "model": "llama-3.3-70b-versatile",
        "response_format":{ "type": "json_object" },
        "messages": [
            {"role": "system", "content": sysprompt},
            {"role": "user", "content": user_content}
        ]
    }, headers=headers)

    response_json = r.json()
    print(response_json)
    if 'choices' in response_json and len(response_json['choices']) > 0:
        content = response_json['choices'][0]['message']['content']
        print(content)
        return content
    else:
        return("")

def generateType_json(content):
    t = send_request(sysprompts[4],content)
    print(t)
    explanation = ""
    if int(t)<=4:
        print("here I am")
        match int(t):
            case 0:
                 explanation = send_request_json(sysprompts_json[0],content)
            case 1:
                explanation = send_request_json(sysprompts_json[1],content)
            case 2:
                explanation =  send_request_json(sysprompts_json[2],content)
            case 3:
                explanation =  send_request_json(sysprompts_json[3],content)
            case 4:
                explanation = json.dumps({"line":1,"comment":"Well done"})
            case _:
                explanation = json.dumps({"line":1,"comment":"No suggestion"})
    else:
        explanation = send_request_json(sysprompts_json[0],content)
    print(explanation)
    return explanation
    


def generateType(content):
    t = send_request(sysprompts[4],content)
    print(t)
    explanation = ""
    if int(t)<=4:
        print("here I am")
        match int(t):
            case 0:
                 explanation = send_request(sysprompts[0],content)
            case 1:
                explanation = send_request(sysprompts[1],content)
            case 2:
                explanation = send_request(sysprompts[2],content)
            case 3:
                explanation = send_request(sysprompts[3],content)
            # case 4:
            #     explanation = send_request(sysprompts[5],content)
            case _:
                explanation = "Well Done!"
            
    else:
        explanation = send_request(sysprompts[0],content)
    return explanation
    

        
def prompts(type,content):
    # split content into lines
    lines = content.strip().split("\n")
    explanation = ""

    match type:
        case 0:
            explanation = send_request(sysprompts[0],content)
        case _:
            explanation = generateType(content)
    

    # if lines[0].startswith("#") or lines[0].startswith("//") or lines[0].startswith("/*"):
    #     explanation = send_request(sysprompts[0], lines[0])
    #     content = "\n".join(lines[1:]) 
    #analysis = send_request(sysprompts[1], content)
    #print(f"""Explanation : {explanation.strip()}\n\nAnalysis: {analysis.strip()}""") if explanation else analysis
    #return f"""Explanation : {explanation.strip()}\n\nAnalysis: {analysis.strip()}""" if explanation else analysis

    return explanation if explanation else ""



'''def prompts(content):
    headers = { 'Content-Type': 'application/json','Authorization' : f'Bearer {GROQ_KEY}'}
    r = requests.post(GROQ_URL,
                      json={
            "model": "llama-3.3-70b-versatile",
            "messages": [{
                "role": "system",
                "content": "You are a coding assistant that only provides the user with logic wise hints towards the solution, no direct solutons should be given,responses should be intended for the user to analyse and then understand what approach should be taken No real coding help should be provided. The response should be no more than 2 lines only giving information that teases the brain of the user.Help the user to build logic by himself not with your use. The question is Binary Search.The response should only be 2 lines."
            },{
                "role": "user",
                "content": content}]
    },
    headers=headers )
    response_json = r.json()

    # Extract and print the 'content' field from the first choice
    if 'choices' in response_json and len(response_json['choices']) > 0:
        content = response_json['choices'][0]['message']['content']
        print(content)
        return content
        
    else:
        return(print("No content found in the response."))'''