import numpy as np

def dictionary(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return len(count)
    
    
tweets = open('tweet_input/tweets.txt')
output = open('tweet_output/ft2.txt','w')
word_count = []

for tweet in iter(tweets):
     tweet_words =  tweet.split(' ',len(tweet)-1)
     word_count.append(dictionary(tweet_words))

for cnt in range(len(word_count)):
    output.write('%.3f\n'%np.median(word_count[0:cnt+1]))

tweets.close()
output.close()


    
