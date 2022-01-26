import json

"""
First I changed each query and each phrase into an array of words.
Then I used a sliding window to move through the array of query words and check if each phrase word was in the window.
There are 2 constraints that define a match:
    1. All phrase words must be present in the correct order
    2. There can be at most 1 extra word in the phrase
I called this extra word a 'bubble'. Since it can be anywhere in the phrase, but can only occur once, I defined it as 
a bool. When I start to search through the window, the bool is true meaning I am allowed to add a bubble into the phrase.
If I hit a mismatch and the bubble bool is True, I can overlook this mismatch because I am still allowed a bubble. If the
bubble bool is False, then I stop searching because there are now 2 extra words in the phrase.

At the start of the window search, I assume the match is found and then trip a flag if the phrase is a mismatch. I build
up a possible answer during the search and only keep it if the match is found.
"""

def phrasel_search(P, Queries):
    ans = []
    for query in Queries:
        query_words = query.split()

        query_ans = []
        for phrase in P:
            phrase_words = phrase.split()

            # Create sliding window the size of the number of words in the phrase
            window_start = 0
            window_end   = len(phrase_words) - 1
            while window_end < len(query_words):
                if phrase_words[0] == query_words[window_start]:
                    possible_answer = [query_words[window_start]]
                    phrase_i = 1
                    window_i = window_start + 1
                    bubble = True

                    # Assume the phrase will be a match when the search starts
                    # If it isn't a match this flag will trip
                    match = True 
                    while phrase_i < len(phrase_words) and match:
                        if phrase_words[phrase_i] == query_words[window_i]:
                            possible_answer.append(query_words[window_i])
                            phrase_i += 1
                            window_i += 1
                        elif bubble:
                            possible_answer.append(query_words[window_i])
                            window_i += 1
                            bubble = False
                        else:
                            match = False

                        # If the bubble occurs at the end of the query string,
                        # we could read past the end of the array. After we apply
                        # the bubble we need to check we don't fall off.
                        if window_i == len(query_words):
                            match = False
                    if match:
                        query_ans.append(" ".join(possible_answer))
                window_start += 1
                window_end   += 1
        ans.append(query_ans)
    return ans

if __name__ == "__main__":
    ## MY TESTING CODE
    test_files = ['sample.json', '20_points.json', '30_points.json', '50_points.json']
    for file in test_files:
        with open(file, 'r') as f:
            sample_data = json.loads(f.read())
            P, Queries = sample_data['phrases'], sample_data['queries']
            returned_ans = phrasel_search(P, Queries)
            print(f"Results for {file}")
            success = True
            for my_ans, solution in zip(returned_ans, sample_data['solution']):
                if set(my_ans) != set(solution):
                    print('!!!!!!!!!!! FAIL FAIL FAIL !!!!!!!!!!!!!!!')
                    print(my_ans)
                    print(solution)
                    success = False
            if success:
                print('============= ALL TEST PASSED SUCCESSFULLY ===============')

    ## ORIGINAL TESTING CODE
    # with open('50_points.json', 'r') as f:
    #     sample_data = json.loads(f.read())
    #     P, Queries = sample_data['phrases'], sample_data['queries']
    #     returned_ans = phrasel_search(P, Queries)
    #     print('============= ALL TEST PASSED SUCCESSFULLY ===============')