from itertools import combinations_with_replacement
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
letVal = {'a' : 1,'b' :3,'c' :3,'d' :2,'e' :1,'f' :4,'g' :2,'h' :4,'i' :1,'j' :8,'k' :5,'l' :1,'m' :3,'n' :1,'o' :1,'p' :3,'q' :10,'r' :1,'s' :1,'t' :1,'u' :1,'v' :4,'w' :4,'x' :8,'y' :4,'z' :10,' ' :0}
numLetters = {'a':9,'b' :2,'c' :2,'d' :4,'e' :12,'f' :2,'g' :3,'h' :2,'i' :9,'j' :1,'k' :1,'l' :4,'m' :2,'n' :6,'o' :8,'p' :2,'q' :1,'r' :6,'s' :4,'t' :6,'u' :4,'v' :3,'w' :3,'x' :1,'y' :3,'z' :1,' ' :2}
target = 46
handLength = 7
hc = 0

def checkHand(hand):
    global hc, numLetters, letVal

    hands = ''.join(hand)
    goodHand = True
    for i in hand:
        if(numLetters[i] < hands.count(i)):
            goodHand = False
            break
    if(goodHand):
        value = 0
        for i in hand:
            value = value + letVal[i]
        if(value == target):
            hc = hc + 1

allHands = list(combinations_with_replacement(letters,handLength))
for hand in allHands:
    checkHand(hand)

print(hc)