

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    if(((s1*6-h1*30)-(m1/2)-(s1/120))>0):
        diff_h1 = 360 - ((s1/5-h1)*30-(m1/2)-(s1/120))
    else:
        diff_h1 = (-6*s1+h1*30)+(m1/2)+(s1/120)
    if(((6*s1-6*m1)-(s1/10))>0):
        diff_m1 = 360-((6*s1-6*m1)-(s1/10))
    else:
        diff_m1 = (-s1*6+m1*6)+(s1/10)
    
    
    time = (h2-h1)*3600 + (m2-m1)*60 + (s2-s1)
    
    h_velocity = 6-(1/120)
    m_velocity = 6-(1/10)
    
        
    if((h_velocity*time-diff_h1)>0):
        answer += max((h_velocity*time-diff_h1)//360,0)+1
        print(answer)
    elif((h_velocity*time-diff_h1)==0):
        answer += 1
        print(answer)
    if((m_velocity*time-diff_m1)>0):
        answer += max((m_velocity*time-diff_m1)//360,0)+1
        print(diff_m1)
        print(answer)
    elif(m_velocity*time-diff_m1==0):
        answer += 1
        print(answer)
    
    if(h2>=12 and h1<12):
        answer -= 1
    # if((h2==12) and (m2==0) and (s2==0)):
    #      answer += 1
    
    if(diff_h1==0 and diff_m1 ==0):
        answer -= 1
    return max(int(answer),0)
