import time
import matplotlib.pyplot as plt

try:
            class TrieNode:
                def __init__(self):
                    self.children=[None]*26
                    self.isEndOfWord=False
            class Trie:
                def __init__(self):
                    self.root=self.getNode()
                def getNode(self):
                    return TrieNode()
                def _charToIndex(self,ch):
                    return ord(ch)-ord('a')
                def insert(self,node):
                    tnode=self.root
                    length=len(node)
                    for i in range(length):
                        index=self._charToIndex(node[i])
                        if not tnode.children[index]:
                            tnode.children[index]=self.getNode()
                        tnode=tnode.children[index]
                    tnode.isEndOfWord=True
               
                def displayContacts(self,curr,str_prefix):
                   
                    if curr.isEndOfWord:
                         print(str_prefix,dict.get(str_prefix))
                       
                   
                       
                    l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                    i=0
                    while(i<len(l)):
                        index=self._charToIndex(l[i])
                        next_node=curr.children[index]
                        if(next_node!=None):
                            self.displayContacts(next_node,str_prefix+l[i])
                        i=i+1
                def search(self,n,contact,str):
                    prev_node=self.root
                    prefix=""
                    length=len(str)
                    i=0
                    while(i<length):
                        prefix=prefix+(str[i])
                        #print(prefix)
                        lastChar=self._charToIndex(prefix[i])
                        curr=prev_node.children[lastChar]
                        if curr==None:
                            print("\nsuggestions based on "+prefix+" are: 0\n")
                            i=i+1
                            break
                        print("\nsuggestions based on "+prefix+' are: ')
                        self.displayContacts(curr,prefix)
                        prev_node=curr
                        i=i+1
                    while(i<length):
                        prefix=prefix+str[i]
                        print("\nsuggestions based on "+prefix+" are: 0")
                        i=i+1
            dict={"triveni":9089264902,
                  "trisha":6457897349,
                  "dhana":7895938597,
                  "dhanalakshmi":9993894845,
                  "meghana":9903243847,
                  "moksha":8579438759,
                  "priyanka":837864500,
                  "priya":982570938,
                  "kousalya":893489800,
                  "sahithi":874587589,
                 "monika": 7863948795,
                 "gagana":9048397329,
                  "venkataramakrishnaprasadsharma":76277382988,
                 "dhanraj": 736482794,
                 "himaja":9928387837,
                  "kavya":7674839989,
                 "divya":87349848789,
                 "hima":8738487484,
                 "ratna":9829389783,
                 "soundarya":9929738724,
                 "karthikeya":9327676764,
                 "keethika":7823387233,
                 "rithik":8989267837,
                 "ramu":9289738738,
                 "asha":7273897387,
                 "bhavana":9002378373,
                 "charan":9097686378,
                 "fathima":893678028,
                 "jyothi":7878962690,
                 "laya":9192867473,
                 "navya":6293898398,
                 "sowmya":827398783,
                 "yamuna":892893898,
                 "zakir":902893898};
            t=Trie()
            c=0
            l=[]
            count=[]
            print("               CONTACT BOOK APPLICATION")
            while(1):
             
                print("1.Insert\n2.Search\n3.Full contact list\n4.graph\n5.exit")
                k=int(input('enter choice: '))
                if k==1:
                    p=int(input('enter no.of contacts to insert: '))
                    for i in range(p):
                        s=input('enter %d name: '%(i+1))
                        v=int(input('enter ph.no: '))
                       
                        dict[s]=v
                    key = dict.keys()
                    for node in key:
                        t.insert(node)
                elif k==2:
                    strlenlist=[]
                    timelist=[]
                    strlenlist1=[]
                    timelist1=[]
                    strlenlist3=[]
                    timelist3=[]
                   
                    key = dict.keys()
                    for node in key:
                        t.insert(node)
                    string = ["t","tri","trive","thriv"]
                    string1=["dhana","monika","priya","sowm","zakir","bhavana","dhanraj","gagana","navya","laya","himaja","kousalya","soundarya","karthik","rithik"]
                   
                    for k1 in range(len(string)):
                            t1=time.time()
                            t.search(len(key),key,string[k1])
                            t2=time.time()
                            timelist.append(t2-t1)
                            strlenlist.append(len(string[k1]))
                    for k2 in range(len(string1)):
                            t1=time.time()
                            t.search(len(key),key,string1[k2])
                            t2=time.time()
                            timelist1.append(t2-t1)
                            strlenlist1.append(len(string1[k2]))

                    string3=["v","ve","venk","venkat","venkatara","venkataramak","venkataramakris","venkataramakrishna","venkataramakrishnapra","venkataramakrishnaprasadsha","venkataramakrishnaprasadsharma"]
                   
                    for k3 in range(len(string3)):
                            t1=time.time()
                            t.search(len(key),key,string3[k3])
                            t2=time.time()
                            timelist3.append(t2-t1)
                            strlenlist3.append(len(string3[k3]))
                   
                elif k==3:
                        for f in dict:
                             print("Name: "+str(f).capitalize()+"\tPh. no.: "+str(dict[f]))
                elif k==4:
                    print("Execution time in sec:")
                    plt.title("Time complexity - Performance Analysis",color="blue")
                    plt.plot(strlenlist,timelist,marker='o',linewidth=2,color="green")
                    plt.xlabel('Prifix string length',color="blue")
                    plt.ylabel('Time taken to perform search operation',color="blue")
                    plt.show()
                   
                    plt.title("Time complexity - Performance Analysis",color="blue")
                    plt.plot(strlenlist1,timelist1,linewidth=2,color="green")
                    plt.xlabel('Prefix string length',color="blue")
                    plt.ylabel('Time taken to perform search operation',color="blue")
                    plt.show()
                   
                   
                    plt.title("Time complexity - Performance Analysis",color="blue")
                    plt.plot(strlenlist3,timelist3,marker='o',linewidth=2,color="green")
                    plt.xlabel('Prefix string length',color="blue")
                    plt.ylabel('Time taken to perform search operation',color="blue")
                    plt.show()
                   
                   
                   
                elif k==5:
                    break
                elif k==6:
                        key = dict.keys()
                        for node in key:
                            t.insert(node)
                        st=input('\nEnter key to search: ')
                        t.search(len(key),key,st)
                        print()
                else:
                    print("choose correct option......")
                    print()
except:
       print("error occured try again")
