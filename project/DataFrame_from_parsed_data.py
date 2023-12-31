import pandas as pd
from Parse_html_python import likes, shared, time, views

df_all = {'likes': likes, 'time': time, 'views': views, 'shared': shared}
df_all = pd.DataFrame(df_all).sort_values('time', ascending=False).reset_index(drop=True)
df_all['time'] = pd.to_datetime(df_all['time'])
df_all['weekday'] = df_all['time'].dt.day_name(locale='ru_RU').astype('string')
df_all['weekday_number'] = df_all['time'].dt.dayofweek + 1

difference_time = df_all['time'].diff().dropna().dt.days
df_difference = {'diff_time': abs(difference_time), 'likes': likes[:-1]}
df_difference = pd.DataFrame(df_difference)

print(df_all.dtypes, df_difference.dtypes, sep="\n\n")
