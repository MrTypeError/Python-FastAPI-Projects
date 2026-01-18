from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books")
async def read_all_books():
    # return {'message' : 'Hello Sudip'}
    return BOOKS

# Path Parameters : These are the dynamic Parameters that are passed in the API calls to go to a dynamic location

# VVV IMP #
# We should always put the static call for any API call because if we don't keep it before the dynamic call then FastAPI will always call the dynamic call first.so the static call will never be executed.

# @app.get("/books/{dynamic_param}")
# async def list_all_books(dynamic_param : str):
#     return {'dynamic Param' : dynamic_param}

# @app.get("/books/{book_title}") # Here in the URL (http://127.0.0.1:8000/books/title%20two) " " -> %20 (this is a place holder for space in FastAPI)
# async def list_all_books():
#     return {'dynamic Param' : dynamic_param}


@app.get("/books/{book_title}")
async def list_all_books(book_title : str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold() :
            return book


# Query Parameters : This have name=value pairs 
# Example : Request -> 127.0.0.1:8000/books/?catagory=math 

@app.get("/books/")
async def read_catagory_by_query(catagory : str) :
    books_to_return = []

    for book in BOOKS:
        if book.get('title').casefold() == catagory.casefold() :
            books_to_return.append(book)
    return book


@app.get("/books/{book_author}/")
async def read_catagory_by_query(book_author : str , category : str) :
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold() :
            books_to_return.append(book)

    return books_to_return

# POST Request Method
@app.post("/book/create_book")
async def create_new_book(new_book=Body()) :
    BOOKS.append(new_book)

# PUT Request Method
@app.put("/book/update_book")
async def update_book(update_book = Body()):
    for i in range(len(BOOKS)) :
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i]=update_book

