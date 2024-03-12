# json_array_to_csv

This is a simple python script to convert a json array in `data.json` to a csv file called `output.csv`

NOTICE: Should have made `data.json` and `output.csv` as arguments but I'm lazy

## Usage

Create `data.json` and fill it with your data

```zsh
cp data.json.example data.json
```

```zsh
python script.py
```

## Example

```json
[
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Jane",
        "age": 25,
        "city": "Los Angeles"
    }
]
```

```csv
name,age,city
John,30,New York
Jane,25,Los Angeles
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
