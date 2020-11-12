import wolframalpha
#wolframalpha operation
def wolfram_try(question):    
    app_id = "AT3YLY-P2L67K557P"
    client = wolframalpha.Client(app_id) 
    res = client.query(question) 
    answer = next(res.results).text 
    return answer

#print(wolfram_try("5+10"))