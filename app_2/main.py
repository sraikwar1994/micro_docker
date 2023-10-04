"""
Main file
"""
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()


# Define a route using a decorator
@app.get("/")
def read_root():
    """

    :return:
    """
    return {"Hello": "World"}


# Define another route
@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    """

    :param item_id:
    :param query_param:
    :return:
    """
    return {"item_id": item_id, "query_param": query_param}


# This block allows running the application using "uvicorn main:app --reload"
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8002)
