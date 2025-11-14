def can_break_string(s: str, word_dict: list) -> bool:
    n = len(s)
    word_set = set(word_dict)
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            substring = s[j:i]
            
            if dp[j] and substring in word_set:
                dp[i] = True
                break
                
    return dp[n]

word_dictionary_1 = ["apple", "pen"]
string_1 = "applepenapple"

word_dictionary_2 = ["cats", "dog", "sand", "and", "cat"]
string_2 = "catsandog"

word_dictionary_3 = ["a", "b", "c"]
string_3 = "abc"

print(f"Рядок: '{string_1}'. Можливо розбити: {can_break_string(string_1, word_dictionary_1)}")
print(f"Рядок: '{string_2}'. Можливо розбити: {can_break_string(string_2, word_dictionary_2)}")
print(f"Рядок: '{string_3}'. Можливо розбити: {can_break_string(string_3, word_dictionary_3)}")
