
## Deploy FastAPI App
- Go to https://fastapi.tiangolo.com/deployment/deta/
- Create an account
- Now, in the same directory of main.py >> create a file `requirements.txt` with:
    fastapi
- Run 

```
    curl -fsSL https://get.deta.dev/cli.sh | sh
```


- Close terminal , then
    deta --help
    deta login
    deta new
- You will see a JSON message similar to:

```
    {
            "name": "fastapideta",
            "runtime": "python3.7",
            "endpoint": "https://qltnci.deta.dev",
            "visor": "enabled",
            "http_auth": "enabled"
    }
 ```
 
- And now go to the `/docs` for your API, in the example above it would be `https://qltnci.deta.dev``/docs`.
