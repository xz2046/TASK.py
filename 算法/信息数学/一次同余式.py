def exgcd(a,b,arr):#利用拓展欧几里得定理求乘法逆元
    if b == 0:
        arr[0] = 1
        arr[1] = 0 
        return a
    r = exgcd(b,a%b,arr)
    tmp = arr[0]
    arr[0] = arr[1]
    arr[1] = tmp - int(a/b)*arr[1]
    return r   


def Get_Mi(m_list,M): #求出 M / mi
    M_list=[]
    for mi in m_list:
        M_list.append(M//mi)
    return M_list

def Get_ei_list(M_list,m_list):#获取乘法逆元
    ei_list=[]
    for i in range(len(M_list)):
        ei_list.append(Get_ei(M_list[i],m_list[i]))
    return ei_list
   
def Get_ei(a,b):
    # 计算ei
    
   
    arr = [0,1,]
    r = exgcd(a,b,arr)
    if r == 1:
        return int ((arr[0] % b + b )%b)
    else :
        return -1
    

def crt(a_list,m_list):
    # 计算中国剩余定理，返回计算结果
    
    M = 1
    sum1 = 0
    for i in range(len(m_list)):
        M = M * m_list[i]
    M_list=(Get_Mi(m_list,M))
    ei_list=(Get_ei_list(M_list,m_list))
    for i in range (len(m_list)):
        sum1= sum1+ M_list[i] * ei_list[i] * a_list[i]
    return sum1 % M
    # **************end*************#
    
if __name__=='__main__':
    a_list= list(map(int,input().split(",")))
    m_list= list(map(int,input().split(",")))
    print(crt(a_list,m_list))

