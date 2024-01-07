



def createLongestPrefixTable(query):
    longestPrefix = [0]*len(query)
    j = 0
    for i in range(1, len(query)):
        # print(query[j], query[i])
        if query[j] == query[i]:
            longestPrefix[i] = j+1
            j = j + 1

        else:
            if j>0:
                j = j-1
                j = longestPrefix[j]
                while j>0 and not query[j] == query[i]:
                    j = j - 1
                    j = longestPrefix[j]
                
                longestPrefix[i] = j

    return longestPrefix



def knuffMorrisPratt(string, query):
    longestPrefix = createLongestPrefixTable(query)
    # print(longestPrefix)
    currPos = 0
    length = len(string)
    ans = []
    queryLen = len(query)

    i = 0
    j = 0
    M = queryLen
    N = length
    pat = query
    txt = string
    lps = longestPrefix

    # i and j are current index of the text and query respectively.
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            i += 1
            j += 1

        """
        reached end of query, we found a match and align previously matched suffix(which is a substring of the entire matched  query) to its prefix. 
        By setting j, 
        we are matching the next character in question  string[i] (incremented previously by 1) to query[j] . 
        The previous 1...j-1 items is guaranteed to match since the 1...j-1 is the prefix of that matches to the
        previous suffix of provided string
        """
        if j == M:
            ans.append(str(i-j))
            j = lps[j-1]
 
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters, m
            # they will match anyway
            """
            What this is doing is setting j to an index in the query where query_0...index-1 is the prefix that matches the suffix of the matched substring 
            between the query and the provided string(exclude the character that did not match). Because we know that the suffix have been matched, and if there is
            a prefix, i.e. j!=0, there we can skip the other character align the prefix and the suffix to find a new possible match. By setting j to that index, 
            the previous characters are already matched(suffix and prefix), and the next character is the one that is mismatched, and we see if it matches with query[j]
            the while loop continues...
            """
            if j != 0:
                j = lps[j-1]
            #Else if j == 0 , that means we didn't have any match in the string to the pattern, or no prefix exist for the matched suffix.
            else:
                i += 1
    
    return ans
    
       


while True: 

    try:
        query = input()
        string = input()
        ans = knuffMorrisPratt(string, query)
        print(" ".join(ans))
    except EOFError:
        break
  




    # while currPos < length and length-currPos>=queryLen:
        
    #     matched = 0
    #     found = True
        
    #     for i in range(currPos, length):
    #         if i-currPos >= queryLen:
    #             break
    #         if string[i] == query[i-currPos]:
    #             matched = matched + 1
    #         else:      
    #             break
    #     if matched < queryLen:
    #         found=  False

    #     if found == True:
    #         ans.append(str(currPos))
              
    #     if matched == 0:
    #         currPos = currPos+1
    #     else:
    #         #if there is a suffix, align the prefix of the query string with the suffix of the matched string
    #         currPos = currPos + (matched - longestPrefix[matched-1])
        # print(currPos)