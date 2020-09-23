
def _helper(s_str,l_str):
    ss_str,ll_str = s_str,l_str
    i = j = 0
    _res = ""
    # print '## ',s_str,l_str
    while i < len(s_str) and j < len(l_str):
        if l_str[j] == s_str[i]:    
            _comm = ""
            while i < len(s_str) and j < len(l_str) and l_str[j] == s_str[i]:
                _comm = _comm + s_str[i]
                # print '^^  ',_comm
                i = i + 1
                j = j + 1
            if len(_comm) > len(_res): _res = _comm
            print '^  ',_comm
            _comm = ""
        elif i  < len(s_str)-2 and s_str[i+1] == l_str[j]:
            i = i+1
        elif j  < len(l_str)-2 and l_str[j+1] == s_str[i]:
            j = j+1
        else:
            i = i+ 1
            j = j + 1   
    print '## ',ss_str,ll_str 
    if len(ll_str)>1: _res2 = _helper(ss_str, ll_str[1:])
    if len(ss_str)>1: _res1 = _helper(ss_str[1:], ll_str)
    if len(_res1) > len(_res): _res = _res1
    if len(_res2) > len(_res): _res = _res2
    print '## final ',_res
    return _res

while True:
    try:
        l_str = raw_input()
        s_str = raw_input()
        if len(s_str) > len(l_str): s_str,l_str = l_str,s_str
        real_res = _helper(s_str,l_str)
        print '***  ',real_res
    except:
        break