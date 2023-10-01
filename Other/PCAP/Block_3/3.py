#Which of the following expressions evaluate to True?

ord('x') - ord('X') == ord(' ')
"""In ACSII, the distance between the codepoints of upper and lowercase letters is always equal to 32
which is the codepoint of a space."""

chr(ord('k') + 2) == 'm'
"""ASCII alphabetic codepoints are ordered in the same order as the Latin alphabet, so ord('m') is greater by
2 than ord('k')"""