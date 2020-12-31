import json
import urllib.request
tuling_key='8c918d2e025d4dc1ada1313094dc8e9d'
api_url = "http://openapi.tuling123.com/openapi/api/v2"
def get_message(message,userid):
    req = {
    "perception":
    {
        "inputText":
        {
            "text": message
        },
        "selfInfo":
        {
            "location":
            {
                "city": "嘉兴",
                "province": "浙江",
                "street": "昌盛南路1001号"
            }
        }
    },
    "userInfo":
    {
        "apiKey": tuling_key,
        "userId": userid
    }
    }
    req = json.dumps(req).encode('utf8')
    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    response_dic = json.loads(response_str)
    results_code = response_dic['intent']['code']
    print(results_code)
    if results_code == 4003:
        results_text = "4003:%s"%response_dic['results'][0]['values']['text']
    else:
        results_text = response_dic['results'][0]['values']['text']
    return results_text
