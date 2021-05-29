def multi_bracket_validation(input):
    level = 1
    sum = 0
    for i in input :
        if i == '[':
            sum+=1*level
            level*=10

        if i == '(':
            sum+=2*level
            level*=10
        if i == '{':
            sum+=3*level
            level*=10

        if i == ']':
            level/=10
            sum-=1*level

        if i == ')':
            level/=10
            sum-=2*level

        if i == '}':
            level/=10
            sum-=3*level

    if sum == 0 :
        return True
    return False

print (multi_bracket_validation('(){}[[]]'))

print('ok')
