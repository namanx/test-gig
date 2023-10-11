import heapq
 
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
         
    def __lt__(self, nxt):
        return self.freq < nxt.freq
    
         
def printNodes(node, val=''):
    newVal = val + str(node.huff)
    
    if(node.left):
        printNodes(node.left, newVal)

    if(node.right):
        printNodes(node.right, newVal)

    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
 
 
chars = []
freq = []


n = int(input("Enter Number of Characters: "))
for i in range(n):
    chars.append(input("Character: "))
    freq.append(int(input("Frequence: ")))

l = [[chars[i], freq[i]] for i in range(n)]
print("\nCharacter : Frequence ", *l)

# list containing unused nodes
nodes = []
 
# converting characters and frequencies into huffman tree nodes
for x in range(n):
    heapq.heappush(nodes, node(freq[x], chars[x]))
 
while len(nodes) > 1:
    # sort all the nodes in ascending order based on their frequency
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
 
    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1
 
    # combine the 2 smallest nodes to create new node as their parent
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
 
    heapq.heappush(nodes, newNode)
 
print("\nHuffman code: ")
printNodes(nodes[0])

