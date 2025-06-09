import requests
import json
from pprint import pprint

def test_database_generation():
    # API endpoint
    url = "http://localhost:8000/database/generate/"
    
    # Example database schema
    schema = {
        "tables": [
            {
                "name": "customers",
                "columns": [
                    {
                        "name": "id",
                        "data_type": "int",
                        "is_primary_key": True,
                        "is_nullable": False
                    },
                    {
                        "name": "first_name",
                        "data_type": "varchar(50)",
                        "is_nullable": False
                    },
                    {
                        "name": "last_name",
                        "data_type": "varchar(50)",
                        "is_nullable": False
                    },
                    {
                        "name": "email",
                        "data_type": "varchar(100)",
                        "is_nullable": False
                    },
                    {
                        "name": "phone",
                        "data_type": "varchar(20)",
                        "is_nullable": True
                    },
                    {
                        "name": "address",
                        "data_type": "text",
                        "is_nullable": True
                    }
                ]
            },
            {
                "name": "orders",
                "columns": [
                    {
                        "name": "id",
                        "data_type": "int",
                        "is_primary_key": True,
                        "is_nullable": False
                    },
                    {
                        "name": "customer_id",
                        "data_type": "int",
                        "is_foreign_key": True,
                        "referenced_table": "customers",
                        "referenced_column": "id",
                        "is_nullable": False
                    },
                    {
                        "name": "order_date",
                        "data_type": "date",
                        "is_nullable": False
                    },
                    {
                        "name": "total_amount",
                        "data_type": "decimal(10,2)",
                        "is_nullable": False
                    },
                    {
                        "name": "status",
                        "data_type": "varchar(20)",
                        "is_nullable": False
                    }
                ]
            }
        ]
    }
    
    # Test parameters
    params = {
        "rows_per_table": 5  # Generate 5 rows per table for testing
    }
    
    try:
        # Make the API request
        response = requests.post(url, json=schema, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Get the generated data
            generated_data = response.json()
            
            # Print the results
            print("\n=== Generated Data ===")
            for table_name, rows in generated_data.items():
                print(f"\n{table_name.upper()} Table:")
                print("-" * 50)
                for row in rows:
                    pprint(row)
                print("-" * 50)
            
            # Validate the data
            validate_generated_data(generated_data, schema)
        else:
            print(f"Error: {response.status_code}")
            print(response.json())
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {str(e)}")

def validate_generated_data(generated_data, schema):
    """Validate the generated data against the schema."""
    print("\n=== Validation Results ===")
    
    # Check if all tables are present
    schema_tables = {table["name"] for table in schema["tables"]}
    generated_tables = set(generated_data.keys())
    
    if schema_tables == generated_tables:
        print("✓ All tables are present")
    else:
        print("✗ Missing tables:", schema_tables - generated_tables)
    
    # Validate each table's data
    for table_name, rows in generated_data.items():
        print(f"\nValidating {table_name}:")
        
        # Get table schema
        table_schema = next(t for t in schema["tables"] if t["name"] == table_name)
        
        # Check if all required columns are present
        schema_columns = {col["name"] for col in table_schema["columns"]}
        for row in rows:
            row_columns = set(row.keys())
            if schema_columns != row_columns:
                print(f"✗ Column mismatch in {table_name}")
                print(f"  Missing: {schema_columns - row_columns}")
                print(f"  Extra: {row_columns - schema_columns}")
                break
        else:
            print("✓ All columns are present")
        
        # Validate foreign key relationships
        for column in table_schema["columns"]:
            if column.get("is_foreign_key"):
                ref_table = column["referenced_table"]
                ref_column = column["referenced_column"]
                
                # Get all valid foreign key values
                valid_values = {row[ref_column] for row in generated_data[ref_table]}
                
                # Check if all foreign key values are valid
                invalid_values = set()
                for row in rows:
                    if row[column["name"]] not in valid_values:
                        invalid_values.add(row[column["name"]])
                
                if invalid_values:
                    print(f"✗ Invalid foreign key values in {column['name']}: {invalid_values}")
                else:
                    print(f"✓ Foreign key {column['name']} is valid")

if __name__ == "__main__":
    test_database_generation() 