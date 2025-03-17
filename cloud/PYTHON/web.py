from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_html():
    html_content = """
    <html>
        <head>
            <title>FastAPI Web App</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f0f0f0;
                    margin: 0;
                    padding: 0;
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                .container {
                    text-align: center;
                    background-color: #ffffff;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    font-size: 48px;
                    color: #2c3e50;
                    margin-bottom: 20px;
                }
                p {
                    font-size: 20px;
                    color: #7f8c8d;
                }
                .footer {
                    margin-top: 30px;
                    font-size: 14px;
                    color: #bdc3c7;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to FastAPI!</h1>
                
                <div class="footer">
                    
                </div>
            </div>
        </body>
    </html>
    """
    return html_content
