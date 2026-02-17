from routes.order_route import route as order_route
from fastapi import FastAPI


app = FastAPI(debug=True) 
app.include_router(order_route)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)