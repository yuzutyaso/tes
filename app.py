from flask import Flask, render_template

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# トップページへのルーティング
@app.route('/')
def home():
    # templatesフォルダ内のindex.htmlをレンダリングして返す
    return render_template('index.html')

# アプリケーションを起動
if __name__ == '__main__':
    # デバッグモードを有効にして、ホストをすべてのIPアドレスからアクセス可能に設定
    app.run(debug=True, host='0.0.0.0')
