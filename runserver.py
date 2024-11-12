import uvicorn

if __name__ == '__main__':
    uvicorn.run(app="main:fun", host="127.0.0.1", port=9000, reload=True, access_log=False)
