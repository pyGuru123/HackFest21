width = 5
s='😈🦹🦹🦹😈'
a='😡'
u='😱'
f='😴'
#tophead
print((a*14).center(width*4))
for i in range((width-1)//2):
    print((a*width*3).center(width*4))
print((a*3).center(width+2)+(a*3).center(width*7))
#two_pillars
for i in range(width*2-2):
    print((f*2).center(width+1)+(f*2).center(width*9-4))
#speakerrs
print((u*4).center(width+1)+(u*4).center(width*8-5))
for i in range(width-2):
    print(s.center(width+1)+s.center(width*7-1))
print((u*4).center(width+1)+(u*4).center(width*8-5))
