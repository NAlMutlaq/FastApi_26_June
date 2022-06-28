from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse

app = FastAPI()


# الصفحه الرئيسيه
@app.get('/')
def _():
    from datetime import datetime
    html_content = f"""
    <html>
        <head>
            <title> Main Page </title>
        </head>
        <body>
            <h1> Im In Main Page !!</h1>
            <h2> Question 1  (@app.get('/date') <a href='/date'> Go to Question 1 </a> </h2> 
            <h2> Question 1  @app.get('/date')  <a href='/random_using_get?x=10&y=20'> Go to Question 2 </a> </h2>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# API 
# صفحة التاريخ
@app.get('/date')
def _():
    from datetime import datetime
    html_content = f"""
    <html>
        <head>
            <title> date Page </title>
        </head>
        <body>
            <h1> Im In Question 1  Page !!</h1>
            <h2> TODAY DATE IS : <br> {datetime.now()}</h2>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# API
# صفحة رقم عشوائي
@app.get('/random_using_get')
def _(x :int , y:int):
    from datetime import datetime
    import random
    html_content = f"""
    <html>
        <head>
            <title> Main Page </title>
        </head>
        <body>
            <h1> Im In Question 2  Page !!</h1>
            <h2> the Enter Numbers is {x}  , {y} : <br> random numbers =  {random.randint(x,y)}</h2>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


# API POST 
# رقم عشوائي
@app.post('/random')
def _(x :int , y:int):
    if x  > y :
        x , y = y , x
    import random
    return random.randint(x,y)


if __name__ == '__main__':
    # uvicorn.run('Day3Questions:app' , reload=True , port = 9000)
    import os
    os.system("uvicorn Day3Questions:app --port 9000 --reload")