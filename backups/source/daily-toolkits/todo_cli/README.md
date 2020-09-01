# TODO CLI Features and Design

- Add todo item with start-time
todo item fields:

```sh
{
  "category":"todo category",
  "start_time":"",
  "description":"",
  "status":"default to start"
}

```

- List not completed todos

- complete todos

## TODO Basic Design

- todo entity

```json
{
  "category":"",
  "start_time":"",
  "description":"",
  "status":"",
  "id":""
}
```

- todo actions:

```sh
# create 
create todo item 
# delete
delete todo item
# update status
update to status to COMPLETED
status: COMPLETED,START,PROCESSING
```

- todo items save to json file

todo_item.json: json file format

```bash
{
 "todos":[todo_items]
}
```

current_id.json: the latest todo id 
