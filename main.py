import uvicorn


host="127.0.0.1"
port=8081
app_name="app.api.endpoints:app"



if __name__ == '__main__':
    uvicorn.run(app_name, host=host, port=port)