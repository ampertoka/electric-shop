from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Serve minimal static UI at /ui
static_dir = (Path(__file__).parent / "static")
app.mount("/ui", StaticFiles(directory=str(static_dir), html=True), name="ui")

dict_f = [{'name': 'cable', 'sechenie': '1.5', 'color': 'red', 'data': '26:09:2025'},
          {'name': 'cable', 'sechenie': '2.5', 'color': 'red', 'data': '26:09:2025'}]


@app.get('/cat')
def catalog():
    print('сказать повару: быстрее')
    return dict_f


@app.post('/cat/add')
def catalog_add():
    dict_f.append(
        {'name': 'cable', 'sechenie': '2.5', 'color': 'green', 'data': '26:09:2025'}
    )
    return dict_f


@app.delete('/cat/del')
def catalog_delete():
    del dict_f[0]
    return dict_f


@app.get('/cat/update')
def catalog_update():
    print(dict_f[-1])
    dict_f[-1]['color'] = 'black'
    print(dict_f[-1])
    return dict_f
