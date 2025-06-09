# AnonymizerIA

AnonymizerIA is a powerful API service that helps you generate anonymized data for your database schemas. It provides a simple way to create realistic test data while maintaining referential integrity and data relationships.

## Features

- **Database Schema Parsing**: Upload your database structure in JSON format
- **Smart Data Generation**: Automatically generates realistic data based on column types
- **Referential Integrity**: Maintains relationships between tables through foreign keys
- **Customizable Output**: Control the number of rows generated per table
- **Multiple Data Types Support**:
  - Integers
  - Floating-point numbers
  - Strings (VARCHAR, TEXT)
  - Dates
  - Booleans
  - Foreign Keys

## Prerequisites

- Python 3.8+
- Django 4.0+
- Django REST Framework

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AnonymizerIA.git
cd AnonymizerIA
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .envExample .env
# Edit .env with your configuration
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## Project Structure

```
anonymizerIA/
├── src/
│   ├── Domain/
│   │   └── Database/
│   │       └── DatabaseSchema.py
│   ├── Applicaction/
│   │   └── Database/
│   │       └── GenerateAnonymizedData.py
│   └── Infrastructure/
│       └── Controllers/
│           └── GenerateDatabaseDataController.py
├── manage.py
├── requirements.txt
└── README.md
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.