s = "the sky is blue"
# Split the sentence into words, reverse the order of words, and join them back together
for i in s.split()[::-1]:
    print(i, end=' ')
