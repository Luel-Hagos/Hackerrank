#@Prince.com
def minion_game(s):
    v='AEIOU'
    st=0
    ke=0
#for more than single character
    ll=len(s)
    for i in range(ll):
        if s[i] in v:
            ke+=ll-i
        else:
            st+=ll-i
    
    if st>ke:
        print('Stuart',st)
    elif st<ke:
        print('Kevin',ke)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)