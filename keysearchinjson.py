d1={
    "Messages": [
        {
            "MessageID": "test",
            "Description": "PlaceHolder for Description",
            "LongDescription": "PlaceHolder for Description",
            "Message": "\"Test\"",
            "MessageSeverity": "OK",
            "NumberOfArgs": 2,
            "ParamTypes": [
                "str",
                "str"
            ],
            "ArgDescriptions": [
                "Placeholder for Description"
            ],
            "ArgLongDescriptions": [
                "Placeholder for LongDescription"
            ],
            "Resolution": "None",
            "Oem": {
                "EventSteps": [
                    {
                        "Command": "POST",
                        "URI": "URI",
                        "Data": "'{JSON DATA}'"
                    }
                ]
            }
        }
    ]
}

search='URI'
def finding(d1,search):
    if isinstance(d1,dict):
        for ele in d1:
            if ele==search:
                return d1[ele]
            else:
                res=finding(d1[ele],search)
                if res!=None:
                    return res
        return None
    elif isinstance(d1,list) or isinstance(d1,tuple):
        for ele in d1:
            res=finding(ele,search)
            if res!=None:
                return res
        return None
    else:
        return None
        
res=finding(d1,search)
print(res)