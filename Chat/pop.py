import requests,json


def getresponsegpt(question):
    urlgpt3_5="https://api.openai.com/v1/chat/completions" 
    
    headers_dict=dict()
    headers_dict['Content-Type']='application/json'
    headers_dict['Authorization']= 'Bearer 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'
    
    data_dict=dict()
    data_dict["model"] = "gpt-3.5-turbo"
    data_dict["messages"] =[{
    		"role": "user",
    		"content": question
    		}]
    
    data_dict=json.dumps(data_dict)
    
    response = requests.post(url=urlgpt3_5,headers=headers_dict,data=data_dict)
    response=response.json()
    required_ans=response['choices'][0]['message']['content']
    
    return required_ans



