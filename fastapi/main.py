from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI Backend</title>
        <style>
            :root {
                /* FastAPI의 상징적인 틸(Teal) 컬러 사용 */
                --primary-color: #009485;
                --bg-color: #f4f7f6;
                --text-color: #333;
                --card-bg: #ffffff;
            }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: var(--bg-color);
                color: var(--text-color);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: var(--card-bg);
                padding: 3rem;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 450px;
                width: 100%;
                border-top: 6px solid var(--primary-color);
            }
            .logo-text {
                font-size: 3rem;
                margin-bottom: 0.5rem;
            }
            h1 {
                color: var(--primary-color);
                margin: 0.5rem 0 1rem;
                font-size: 2rem;
            }
            p {
                color: #666;
                line-height: 1.6;
                margin-bottom: 2rem;
            }
            .btn {
                background-color: var(--primary-color);
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 30px;
                font-size: 1rem;
                font-weight: bold;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
                text-decoration: none;
                display: inline-block;
            }
            .btn:hover {
                background-color: #007f72;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(0, 148, 133, 0.3);
            }
            .code-box {
                background: #eee;
                padding: 5px 10px;
                border-radius: 4px;
                font-family: monospace;
                color: #d63031;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo-text">⚡</div>

            <h1>FastAPI Server</h1>

            <p>
                현재 Python <span class="code-box">FastAPI</span> 백엔드 서버에<br>
                직접 접속하셨습니다.
            </p>


        </div>
    </body>
    </html>
    """

@app.get("/health")
def health_check():
    return {"status": "ok"}
