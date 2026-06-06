import heapq

class Twitter:

    def __init__(self):
        self.time = 1 # Authoritative time for the tweets
        self.tweets = defaultdict(list) # Maps userId to a list of tweetId
        self.followers = defaultdict(set) # Maps userId to a set of followerId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followers[userId].add(userId)
        followSet = self.followers[userId] # set of all users userId follows
        
        res = []
        minHeap = []

        K = 10 # heapsize

        for user in followSet: # iterate through all the users userId follows
            tweets = self.tweets[user] # list of tweets made by user
            for n in range(len(tweets) - 1, -1, -1):
                tweet = tweets[n]
                if len(minHeap) < K:
                    heapq.heappush(minHeap, tweet) # adds the tweet to the heap and since the oldest tweets have the smallest times it keeps the oldest at the top
                elif tweet[0] > minHeap[0][0]:
                    heapq.heapreplace(minHeap, tweet)
                else:
                    break
        
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        res.reverse()
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

