import pandas as pd

df = pd.DataFrame({
    "미국": [2.1, 2.2, 2.3],
    "한국": [0.4, 0.5, 0.45],
    "중국": [10, 13, 15]
},
    index=[2000, 2010, 2020]
)
df.index = [2001, 2002, 2003]
df.columns = ['일본', '필리핀', '러시아']
# print(df)


df = pd.DataFrame({
    "년도": [2000, 2010, 2020],
    "미국": [2.1, 2.2, 2.3],
    "한국": [0.4, 0.5, 0.45],
    "중국": [10, 13, 15]
})
df = df.set_index('년도')
# print(df)

# df = df.reset_index('년도')
# print("\n", df)

df.index.name = '연도'
# print(df)

# print(df.loc[2000]['미국'])
# print(df['미국'][2000])

df['일본'] = [1, 2, 3]
# print(df)

del df['일본']
print(df)
