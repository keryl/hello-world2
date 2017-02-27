def replicate_recur(times, data):
 
 
        ret.append(data)
 
        t -= 1
 
        if t == 0:
            return ret
        else:
            helper(t)
 
    helper(times)
 
    return ret
 
def replicate_iter(times, data):
 
    if type(times) is not int or not (type(data) is int or type(data) is str):
        raise ValueError('ValueError')
 
    if times <= 0:
        return []
 
    ret = []
 
    for i in range(times):
 
        ret.append(data)
 
    return ret    if type(times) is not int or not (type(data) is int or type(data) is str):
        raise ValueError('ValueError')
 
    if times <= 0:
        return []
 
    ret = []
 
    def helper(t):

