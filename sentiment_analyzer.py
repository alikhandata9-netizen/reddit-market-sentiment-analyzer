from textblob import TextBlob
import re

def analyze_sentiment(text):
    """
    Analyze sentiment of text using TextBlob
    Returns sentiment score between -1 (negative) and 1 (positive)
    """
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        
        if polarity > 0.1:
            return 'positive', polarity
        elif polarity < -0.1:
            return 'negative', polarity
        else:
            return 'neutral', polarity
    
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return 'neutral', 0

def extract_stock_symbols(text):
    """
    Extract stock ticker symbols from text
    Looks for patterns like AAPL, TSLA, MSFT, etc
    """
    try:
        # Pattern for stock symbols (1-5 uppercase letters)
        pattern = r'\b[A-Z]{1,5}\b'
        symbols = re.findall(pattern, text)
        
        # Common words to exclude
        exclude = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'CAN', 'ALL', 'HAS', 'WAS', 'GET']
        symbols = [s for s in symbols if s not in exclude]
        
        return list(set(symbols))  # Return unique symbols
    
    except Exception as e:
        print(f"Error extracting symbols: {e}")
        return []

def analyze_post(post_data):
    """
    Analyze a post with sentiment and stock symbols
    """
    text = post_data.get('title', '') + ' ' + post_data.get('text', '')
    
    # Get sentiment
    sentiment, score = analyze_sentiment(text)
    
    # Extract symbols
    symbols = extract_stock_symbols(text)
    
    # Create analyzed data
    analyzed = {
        **post_data,
        'sentiment': sentiment,
        'sentiment_score': score,
        'stock_symbols': symbols,
        'analyzed_at': str(__import__('datetime').datetime.now())
    }
    
    return analyzed

def analyze_comment(comment_data):
    """
    Analyze a comment with sentiment and stock symbols
    """
    text = comment_data.get('text', '')
    
    # Get sentiment
    sentiment, score = analyze_sentiment(text)
    
    # Extract symbols
    symbols = extract_stock_symbols(text)
    
    # Create analyzed data
    analyzed = {
        **comment_data,
        'sentiment': sentiment,
        'sentiment_score': score,
        'stock_symbols': symbols,
        'analyzed_at': str(__import__('datetime').datetime.now())
    }
    
    return analyzed

def batch_analyze(posts, is_comments=False):
    """
    Analyze multiple posts or comments
    """
    analyzed_items = []
    
    for item in posts:
        if is_comments:
            analyzed = analyze_comment(item)
        else:
            analyzed = analyze_post(item)
        
        analyzed_items.append(analyzed)
    
    return analyzed_items

# Example usage
if __name__ == '__main__':
    test_post = {
        'title': 'AAPL is crushing it! Great earnings',
        'text': 'I am very bullish on Apple. Stock is going to moon.',
        'subreddit': 'stocks',
        'score': 100
    }
    
    result = analyze_post(test_post)
    print(f"Sentiment: {result['sentiment']}")
    print(f"Score: {result['sentiment_score']}")
    print(f"Symbols: {result['stock_symbols']}")
