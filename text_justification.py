"""
Psuedo-code for the algorithm referenced from:
https://walkccc.github.io/CLRS/Chap15/Problems/15-4/
"""

def extra_characters(line_limit, text_list, aDict):
    with open("results", "w", encoding="utf-8") as file:
        for i in range(0, len(text_list)):
            aDict[(i, i)] = line_limit - len(text_list[i])
            for j in range(i + 1, len(text_list)):
                value = aDict.get((i, j - 1)) - len(text_list[j])-1
                if value < 0:
                    # aDict[(i, j)] = -1
                    break
                elif (value >= 0 and j==(len(text_list)-1)):
                    aDict[(i, j)] = 0
                else:
                    aDict[(i, j)] = value
    return aDict


def cost_of_n_words(text_list, aDict, power):
    cost_dictionary = {}
    for i in range(0, len(text_list)):
        for j in range(i, len(text_list)):
            if (aDict.get((i, j)) is not None):
                cost_dictionary[(i, j)] = aDict.get((i, j)) ** power
    # for key,value in cost_dictionary.items():
    #     print(key,",",value)
    return cost_dictionary

def cost_at_line(text_list, aDict, cost_at_word,parent_pointers):
    cost_at_word[-1]=0
    for i in range(0,len(text_list)):
        cost_at_word[i]=float("inf")
        for j in range(0, i):
            # cost_at_word.get(i - 1) is not None
            if(aDict.get((j,i)) is not None):
                # print("cost_at_word[i-1]+aDict[(i,j)] = ",cost_at_word[i-1]+aDict[(i,j)])
                # print("cost_at_word[j] = ",cost_at_word[j])
                if cost_at_word[j-1]+aDict[(j,i)]<cost_at_word[i]:
                    cost_at_word[i]=cost_at_word[j-1]+aDict[(j,i)]
                    parent_pointers[i]=j
    # for key,value in parent_pointers.items():
    #     print(key,",",value)


def print_text(parent_pointers,list_of_words):
    nth_word=len(list_of_words)-1
    print_list=[]
    while(nth_word!=0):
        x=parent_pointers[nth_word]
        # print(parent_pointers[nth_word])
        aList=[]
        for i in range(x,nth_word):
            aList.append(list_of_words[i])
        print_list.append(aList)
        nth_word=x
    print_list.reverse()
    for i in print_list:
        s=""
        for j in i:
            s+=j+" "
        # print(len(s))
        print(s)

def main():
    line_limit = 100
    power=1
    list_of_words = []
    with open("sample_text.txt", "r", encoding="utf-8") as file:
        for i in file:
            for j in i.split():
                list_of_words.append(j)
    # print(list_of_words)
    extra_chars = {}
    extra_chars = extra_characters(line_limit, list_of_words, extra_chars)
    cost_dictionary = cost_of_n_words(list_of_words,extra_chars,power)
    cost_at_word={}
    parent_pointers={}
    cost_at_line(list_of_words,cost_dictionary,cost_at_word,parent_pointers)
    print_text(parent_pointers,list_of_words)



if __name__ == '__main__':
    main()
