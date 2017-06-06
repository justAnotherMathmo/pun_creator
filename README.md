# Notes

Uses the arpabet here:Uses https://en.wikipedia.org/wiki/Arpabet
Text files from http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/

Sometimes the arpabet link and text file values might be slightly different, namely sometimes the sounds end in different numbers (e.g. OW0 in cmudict is OW1 in wikipedia)


# Extensions
Precompute pronunciation table.
Score puns by associating to each word a score (say, log(1+(#occurrences in some text))) and give their ranking, to filter out obscure words. Perhaps also penalize for being too long/having a contraction/etc. Do this once and then refer to this database instead of the current one.
Look at similar sounds and generate puns based on those as well (if scoring is implementing, penalize the score).
Look not just at pronunciation, but also containment within word.
