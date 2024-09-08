import uvicorn

if __name__ == '__main__':
    uvicorn.run(app='main:fun', host="0.0.0.0", port=9000, reload=True)
