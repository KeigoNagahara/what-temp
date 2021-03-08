from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle
import pandas

tg_date = '2018/9/1'

# 気温のデータ
df = pandas.read_csv(
    'data.csv',
    encoding='Shift_JIS',
)

# 駅でのデータ
df_stations = pandas.read_csv(
    'amedas_stations.csv',
    encoding='Shift_JIS',
    index_col=0
)

# 合体
df = df.join(
    df_stations,
    on='station'
)

# 気温と緯度でロジスティック回帰で学習
tg_df = df[df['date'] == tg_date] # 2018/9/1のデータのみつかう

reg = LinearRegression()
X = tg_df[['latitude']]
y = tg_df['temp']
reg.fit(X, y)
print('learnd')

with open('trained-reg-model.pickle', 'wb') as f:
    pickle.dump(reg, f)


# テスト
X_train, X_test, y_train, y_test = train_test_split(tg_df, y, random_state=0)
reg = LinearRegression()
X2_train = X_train[['latitude','altitude']]
X2_test = X_test[['latitude','altitude']]
reg.fit(X2_train, y_train)
y_pred2 = reg.predict(X2_test)
# 決定係数
print(r2_score(y_test, y_pred2))
