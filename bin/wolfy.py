import wolframalpha
#wolframalpha operation
def wolfram_try(question):    
    app_id = "AT3YLY-P2L67K557P"
    client = wolframalpha.Client(app_id) 
    res = client.query(question) 
    answer = next(res.results)["subpod"]["plaintext"]
    return answer

#print(wolfram_try("define nuance"))