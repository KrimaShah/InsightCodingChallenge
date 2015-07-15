import operator

#Function to create dictionary for the words
def dictionary(words):
    count = {}
    output = open('tweet_output/ft1.txt','w')
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    for word,number in sorted(count.items(),key = operator.itemgetter(0)):       
        output.write(word)
        output.write('   %d\n'%number)
    output.close()

inp = open('tweet_input/tweets.txt')
tweets = inp.read().replace('\n',' ')
wordList = tweets.split(' ',len(tweets))
dictionary(wordList)
inp.close()