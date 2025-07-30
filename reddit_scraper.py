import praw
import pandas as pd
import time

# Reddit credentials
reddit = praw.Reddit(
    client_id="WFl_UVug9CzIVO-7NbCE9w",
    client_secret="VFgWSP_6HRXCUgHDPJd9718kEDtAvQ",
    user_agent="reedditScraper by harry_25625"
)

def fetch_posts_with_comments(subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.hot(limit=limit):
        post.comments.replace_more(limit=0)
        comments = [comment.body for comment in post.comments.list() if comment.body != "[deleted]"]
        posts.append({
            'title': post.title,
            'selftext': post.selftext,
            'comments': " || ".join(comments[:20]),  # Limit to first 20 comments
            'created': post.created_utc,
            'score': post.score,
            'url': post.url
        })
        time.sleep(1)  # Respect API limits

    return pd.DataFrame(posts)

# Multiple subreddits
subreddits = ['depression', 'Anxiety', 'mentalhealth', 'SuicideWatch']
df_all = pd.DataFrame()

for sub in subreddits:
    print(f"Scraping r/{sub}")
    df = fetch_posts_with_comments(sub, limit=300)
    df['subreddit'] = sub
    df_all = pd.concat([df_all, df], ignore_index=True)

# Save dataset
df_all.to_csv("mental_health_dataset.csv", index=False)
print("✅ Dataset saved.")
