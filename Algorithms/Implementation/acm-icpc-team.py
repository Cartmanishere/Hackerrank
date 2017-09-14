#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
    topic_t = int(input().strip(), 2)
    topic.append(topic_t)
    
temp = []
max_topics = 0
for i in range(len(topic)):
    for j in range(i+1, len(topic)):
        ones = bin( topic[i] | topic[j] ).count('1')
        if ones >= max_topics:
            max_topics = ones

        
print(max_topics)
count = 0
for i in range(len(topic)):
    for j in range(i+1, len(topic)):
        ones = bin( topic[i] | topic[j] ).count('1')
        if ones == max_topics:
            count += 1
            
            
print(count)
           
