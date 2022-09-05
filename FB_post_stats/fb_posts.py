# using this link for reference https://www.dataquest.io/blog/analyze-facebook-data-python/

import pandas as pd

# read the json file into a data frame
df = pd.read_json("FB_post_stats/posts/your_posts_1.json")

# rename the timestamp column
df.rename(columns={'timestamp': 'date'}, inplace=True)

#drop some unnecessary columns
df = df.drop(['attachments', 'title', 'tags'], axis=1)

# making sure it's datetime format
pd.to_datetime(df['date'])

df.set_index('date')
df.resample('M') # trouble on this line, use this for help https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html?highlight=resample#pandas.DataFrame.resample
post_counts = df.size('posts')

print(post_counts)
#print(df.shape)
df.head(3)

print(df)