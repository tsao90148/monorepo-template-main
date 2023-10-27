from fastapi import FastAPI, Body

app = FastAPI()

# GET ReST API curl 'http://localhost:8000/api'


@app.get("/api")  # transform func into rest api (get)
def first_api():
    return {"msg": "This is Get Rest API"}

# GET ReST API with path parameters curl 'http://localhost:8000/stuff/random_stuff'


@app.get("/stuff/{path_param}")
def first_api2(path_param: str):
    return {"msg": f"path used is {path_param}"}

# GET ReST API with query parameters curl 'http://localhost:8000/stuff/?name=cool_stuff'


@app.get("/stuff/")
def first_api3(name: str):
    return {"msg": f"category name of stuff is {name}"}

# GET ReST API with path parameters and query parameters curl 'http://localhost:8000/stuff/name_two/?id=5'


@app.get("/stuff/{category_name}/")
def first_api4(category_name: str, id: int):
    return {"msg": f"path or category name used is {category_name} and queried by id number: {id}"}

# Create a POST ReST API curl 'http://localhost:8000/stuff/create_stuff/' -d "{'name':'first', 'category':'random_stuff','id':'1'}"


@app.post("/stuff/create_stuff/")
def first_api5(new_stuff=Body()):
    print(new_stuff)
    return {"msg": new_stuff}

# Create a PUT ReST API curl -X PUT 'http://localhost:8000/stuff/update_stuff/first' -d "{'name':'updated_name', 'category':'new_category', 'id':1}"


@app.put("/stuff/update_stuff/{name}")
def first_api6(updated_stuff=Body()):
    return {"msg": f"Item is updated with data: {updated_stuff}"}


# Create a DELETE ReST API curl -X DELETE 'http://localhost:8000/stuff/delete_stuff/?id=1'
@app.delete("/stuff/delete_stuff/")
def first_api7(id: int):
    return {"msg": f"item with id number: {id} is deleted."}
