#!/user/bin/env python
# -*- coding: utf-8 -*-


def levenshtein(first, second):

    first = first.decode('utf-8')
    second = second.decode('utf-8')

    print len(first) , len(second)
    if len(first) > len(second):
        first, second = second, first

    print len(first) , len(second)

    if len(first) == 0:
        levres = len(second)
    if len(second) == 0:
        levres = len(first)

    print 'hello world~'
    # too short
    # if len(second) == 1 and (second not in first):
    #     return 0.0

    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [range(second_length) for x in range(first_length)] 
    #print distance_matrix
    for i in range(1,first_length):
        for j in range(1,second_length):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion,deletion,substitution)
    #print distance_matrix
    levres = distance_matrix[first_length-1][second_length-1]
    #print float(levres), len(first)
    #return levres
    print levres,len(second)
    return 1- float(levres)/len(second)



if __name__ == "__main__":
    
    print levenshtein('怎样 挑选 显 腿长的 高跟鞋？漂亮 的长腿 穿出来！','123 穿1237')
    #print levenshtein('今天下午的出来','怎样挑选显腿长的高跟鞋？漂亮的长腿穿出来！')
    #print levenshtein('怎样挑选显腿长的高跟鞋？漂亮的长腿穿出来！','长高跟鞋穿出来')






