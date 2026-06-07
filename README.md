# Reddit Market Sentiment Analyzer

A tool for analyzing investor sentiment on Reddit financial communities.

## What is this?

This project collects and analyzes public discussions from Reddit investing communities to track how sentiment changes around stocks and markets. It's designed for academic research on investor behavior and online communities.

## How it works

1. Monitors subreddits like r/stocks, r/investing, r/wallstreetbets, r/finance
2. Collects posts and comments about stocks
3. Analyzes sentiment (positive/negative/neutral)
4. Tracks which stocks are being discussed
5. Identifies trends and sentiment shifts
6. Stores data for research analysis

## Why build this?

Understanding how investors talk about stocks on social media is valuable for:
- Academic research on investor behavior
- Understanding online community dynamics
- Studying how sentiment spreads across communities
- Analyzing what drives investment decisions

## Technology

- Python 3.10+
- PRAW (Python Reddit API Wrapper)
- PostgreSQL for data storage
- VADER for sentiment analysis
- Flask/FastAPI for dashboard

## Features (planned)

- Real-time monitoring of multiple subreddits
- Sentiment analysis on posts and comments
- Stock ticker extraction and tracking
- Trend detection and alerts
- Historical data queries
- Research dashboard
- Data export for analysis

## Setup

```bash
# Clone the repo
git clone https://github.com/[your-username]/reddit-market-sentiment-analyzer.git

# Install dependencies
pip install -r requirements.txt

# Configure Reddit API credentials
# (more details in documentation)

# Run the collector
python reddit_collector.py
```

## Project Structure

```
reddit-market-sentiment-analyzer/
├── reddit_collector.py      # Collects data from Reddit
├── sentiment_analyzer.py    # Analyzes sentiment
├── data_processor.py        # Processes and aggregates data
├── api_handler.py          # Handles Reddit API connection
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Data Sources

- r/stocks
- r/investing
- r/wallstreetbets
- r/finance
- r/SecurityAnalysis

## Important Notes

- **Read-only**: This tool only reads public data, never posts or comments
- **Research only**: Data is used for academic research purposes
- **Respectful**: Respects Reddit's rate limits and terms of service
- **Transparent**: All code is open source

## Status

Currently in development. Working on core data collection and sentiment analysis modules.

## License

MIT License

## Contact

For questions about this project, see the GitHub issues section.
