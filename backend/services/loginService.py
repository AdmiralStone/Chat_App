import random

def login(postParams):
    try:
        if(postParams['userObj']['loginType'] == 0): #Login As Guest
            postParams['userObj']['userName'] = postParams['userObj']['userName'] + '#' + str(random.randint(999,9999))
        else:
            raise Exception("Internal Server Error(sLoginService-L10)")
        return postParams
    except Exception as e:
        print(e)
        raise Exception(e)


