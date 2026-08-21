def is_pangram(sentence: str) -> bool:
    lower_sentence = sentence.lower()
    char_set = set(lower_sentence)
    ordered_char_list = list(char_set)
    ordered_char_list.sort()
    if "a" in ordered_char_list:
        a_ind = ordered_char_list.index("a")
        if len(ordered_char_list[a_ind:]) >= 26:
            alphabet_list = ordered_char_list[a_ind:a_ind+26]
            return alphabet_list == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
    return False
    

print("Enter a sentence:")
sentence = input()
if is_pangram(sentence):
    print("That sentence is a pangram")
else:
    print("That sentence is NOT a pangram")