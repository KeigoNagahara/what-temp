import pandas
import pickle

def temp_ans(text):
    response = ''
    try:
        response = temp_command(text)
        return response
    except Exception as e:
        print('エラー')
        print('* 種類:', type(e))
        print('* 内容:', e)


def temp_command(text):
    # 学習済みモデルのロード
    with open('trained-reg-model.pickle', 'rb') as d:
        reg = pickle.load(d)

    df = pandas.read_csv(
        './data.csv',
        encoding='Shift_JIS',
    )

    df_stations = pandas.read_csv(
        './amedas_stations.csv',
        encoding='Shift_JIS',
        index_col=0
    )

    df = df.join(
        df_stations,
        on='station'
    )

    row = df[df['station'] == text]
    # レスポンスを作成
    # 駅名がデータにあったら
    if len(row) > 0:
        mean = row['temp'].mean()
        rounded_mean = round(mean, 1) # 小数点丸める
        response = '平均気温は{}度でした'.format(rounded_mean)
    # ない場合緯度をみる
    else:
        try:
            # stationが緯度でくるはず
            latitude = float(text)
            # 気温を予想
            predicted = reg.predict([[latitude]])
            # 予想した気温を取り出す
            predicted_temp = predicted[0]
            # 小数点丸こみ
            rounded_temp = round(predicted_temp, 1)
            response = 'たぶん{}度くらい'.format(rounded_temp)
        except ValueError:
            response = '緯度か駅名を入力してください(データにない駅名はでない)'
    return response
