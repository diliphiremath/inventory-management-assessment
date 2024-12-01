# Inventory Management Backend Assessment

A backend assessment for managing inventory, including functionality to save, retrieve, and search inventory items.

---

## Running the Application with Docker

### Prerequisites
- **Docker** installed on your system.

### Steps
1. Run the following script to start the application:
   ```bash
   ./scripts/run-local

# Steps to Run the Application Locally

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Apply database migrations:**
   ```bash
   python manage.py migrate

4. **Start the Server:**
    To start the server, run the following command:

    ```bash
    python manage.py runserver



## API Routes

| Route                             | Method | Description                                                                 |
|-----------------------------------|--------|-----------------------------------------------------------------------------|
| `/inventory/save`                 | POST   | Validates and saves a JSON request into `Batch`, `Item`, and `Properties` tables. |
| `/inventory/get_object/:object_id` | GET    | Retrieves an object using the specified `object_id`.                       |
| `/inventory/search/?key=:key&value=:value` | GET    | Filters or searches objects using the provided `key` and `value` parameters. |

## Sample request

```json
{
  "batch_id": "71a8a97591894dda9ea1a372c89b7987",
  "objects": [
    {
      "object_id": "d6f983a8905e48f29ad480d3f5969b52",
      "data": [
        {
          "key": "type",
          "value": "shoe"
        },
        {
          "key": "color",
          "value": "purple"
        }
      ]
    },
    {
      "object_id": "1125528d300d4538a33069a9456df4e8",
      "data": [
        {
          "key": "fizz",
          "value": "buzz"
        }
      ]
    }
  ]
}
```

## Testing

```bash
    python manage.py test
