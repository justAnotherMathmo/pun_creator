import re
from collections import defaultdict

# Uses https://en.wikipedia.org/wiki/Arpabet
# Text files from http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/

pron_dict = defaultdict(list)

with open('cmudict-0.7b','r') as pron_file:
    pron_text = pron_file.read()

    # Get rid of things that aren't words
    pron_text = re.sub(r';;;.*?\n', '', pron_text) # Comments
    pron_text = re.sub(r'^[^a-zA-Z].*?\n','',pron_text, flags=re.M) # Symbols

    regex_string = r"^([0-9A-Z'.]+)(?:\(([0-9]+)\))? ((?: [A-Z0-9]+)*)\n"
    for word_pron_string in re.findall(regex_string,
                                       pron_text,
                                       flags=re.M):
        word, extra_occurrence, pronunciation = word_pron_string
        pronunciation = pronunciation[1:] # We copy with leading space
        pron_dict[word] += [pronunciation]

    
def pattern_search(pattern):
    '''Returns all words containing "pattern" in their pronunciation
Give patten in form e.g. "EY B"'''
    words_with_pattern = []
    
    for word in pron_dict:
        has_pattern = 0
        for pron in pron_dict[word]:
            if pattern in pron:
                has_pattern = 1
                break
        if has_pattern:
            words_with_pattern += [word]
            continue
    return sorted(words_with_pattern)

# Search for Eero puns
print(pattern_search('EH1 R OW0'))
