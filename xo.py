class Solution:
    def count_XO(self, string):
            #type string: string
            #return type: boolean
            
            #TODO: Write code below to returnn a boolean value with the solution to the prompt.
            #string= string.upper()
            x=0
            o=0
            for i in string:
                if i=='X':
                    x+=1
                elif i=='O':
                     o+=1
            if(x==o):
                 return True
            else:
                 return False                
def main():
    input1=input()
    tc1 = Solution()
    ans = tc1.count_XO(input1)
    print(ans)

if __name__ == "__main__":
    main()
    