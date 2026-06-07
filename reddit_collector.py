import praw
import time
from datetime import datetime

# Reddit API credentials
# Get these from https://www.reddit.com/prefs/apps
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
USER_AGENT = 'market_sentiment_researcher/1.0'

def connect_to_reddit():
    """Connect to Reddit API using PRAW"""
    try:
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT
        )
        print("Successfully connected to Reddit API")
        return reddit
    except Exception as e:
        print(f"Error connecting to Reddit: {e}")
        return None

def collect_from_subreddit(reddit, subreddit_name, limit=100):
    """Collect recent posts from a subreddit"""
    try:
        subreddit = reddit.subreddit(subreddit_name)
        posts = []
        
        print(f"Collecting posts from r/{subreddit_name}...")
        
        for post in subreddit.new(limit=limit):
            post_data = {
                'title': post.title,
                'text': post.selftext,
                'author': str(post.author),
                'subreddit': subreddit_name,
                'score': post.score,
                'comments': post.num_comments,
                'created': datetime.utcfromtimestamp(post.created_utc),
                'url': post.url
            }
            posts.append(post_data)
        
        print(f"Collected {len(posts)} posts from r/{subreddit_name}")
        return posts
    
    except Exception as e:
        print(f"Error collecting from r/{subreddit_name}: {e}")
        return []

def collect_comments(reddit, subreddit_name, limit=50):
    """Collect recent comments from a subreddit"""
    try:
        subreddit = reddit.subreddit(subreddit_name)
        comments = []
        
        print(f"Collecting comments from r/{subreddit_name}...")
        
        for comment in subreddit.comments(limit=limit):
            comment_data = {
                'text': comment.body,
                'author': str(comment.author),
                'subreddit': subreddit_name,
                'score': comment.score,
                'created': datetime.utcfromtimestamp(comment.created_utc)
            }
            comments.append(comment_data)
        
        print(f"Collected {len(comments)} comments from r/{subreddit_name}")
        return comments
    
    except Exception as e:
        print(f"Error collecting comments from r/{subreddit_name}: {e}")
        return []

def main():
    """Main function to run data collection"""
    print("Starting Reddit Market Sentiment Analyzer")
    print("=" * 50)
    
    # Connect to Reddit
    reddit = connect_to_reddit()
    if not reddit:
        print("Failed to connect to Reddit. Exiting.")
        return
    
    # List of subreddits to monitor
    subreddits = ['stocks', 'investing', 'wallstreetbets', 'finance', 'SecurityAnalysis']
    
    all_posts = []
    all_comments = []
    
    # Collect data from each subreddit
    for sub in subreddits:
        print(f"\nProcessing r/{sub}...")
        
        # Collect posts
        posts = collect_from_subreddit(reddit, sub, limit=50)
        all_posts.extend(posts)
        
        # Collect comments
        comments = collect_comments(reddit, sub, limit=50)
        all_comments.extend(comments)
        
        # Be respectful with API rate limits
        time.sleep(2)
    
    print("\n" + "=" * 50)
    print(f"Total posts collected: {len(all_posts)}")
    print(f"Total comments collected: {len(all_comments)}")
    print("=" * 50)
    
    # TODO: Send data to sentiment analyzer
    # TODO: Store data in database
    # TODO: Update dashboard

if __name__ == '__main__':
    main()
