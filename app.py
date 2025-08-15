from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-command', methods=['POST'])
def run_command():
    try:
        command = request.json.get('command')
        if not command:
            return jsonify({'error': 'No command provided'}), 400

        # コマンドを実行し、標準出力とエラーを取得
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=100 # タイムアウト設定
        )

        output = result.stdout
        error = result.stderr
        status_code = result.returncode

        response_data = {
            'output': output,
            'error': error,
            'status_code': status_code
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
