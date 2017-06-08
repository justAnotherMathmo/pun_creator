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

def generate_pattern(word):
    '''Gives the pronunciation for a word'''
    valid_prons = pron_dict[word.upper()]
    if len(valid_prons) == 0:
        raise ValueError(
            'The word {} does not exist in the dictionary'.format(word)
            )
    else:
        return valid_prons
    
##def pattern_search_base(pattern):
##    '''Returns all words containing "pattern" in their pronunciation
##Give patten in form e.g. "EY B"'''
##    words_with_pattern = []
##    
##    for word in pron_dict:
##        has_pattern = 0
##        for pron in pron_dict[word]:
##            if pattern in pron:
##                has_pattern = 1
##                break
##        if has_pattern:
##            words_with_pattern += [word]
##            continue
##    return sorted(words_with_pattern)

def pattern_search(regex):
    '''Returns all words whose pronunciation matches the regex
Give patten in form e.g. "EY B"'''
    words_with_pattern = []
    
    for word in pron_dict:
        has_pattern = 0
        for pron in pron_dict[word]:
            if re.search(regex, pron) is not None:
                has_pattern = 1
                break
        if has_pattern:
            words_with_pattern += [word]
            continue
    return sorted(words_with_pattern)

def word_search(word):
    '''Searches for the words that, when pronounced, contain input word'''
    pattern = generate_pattern(word)[0]
    return pattern_search(pattern)

# Search for Eero puns
# print(pattern_search_base('EH1 R OW0'))
# print(word_search('EROH'))
print(pattern_search('EH[0-9] R[0-9]{0,1} OW[0-9]'))
