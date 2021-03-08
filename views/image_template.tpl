<html>
  <body>
    <h1>数字よみとり</h1>
    <form method="post" action="/start" enctype="multipart/form-data">
      駅名もしくは緯度を入れてください: <input type="text" name="input_text"><br>
      <input type="submit" value="送信">
    </form>
    <ul>
      <li>pybotからの応答メッセージ: {{!output_text}}</li>
    </ul>
  </body>
</html>
