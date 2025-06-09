from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
import json

from anonymizerIA.src.Domain.Database.DatabaseSchema import DatabaseSchema, Table, Column
from anonymizerIA.src.Applicaction.Database.GenerateAnonymizedData import GenerateAnonymizedData

class GenerateDatabaseDataController(APIView):
    @csrf_exempt
    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            # Parse the database schema from the request
            schema_data = json.loads(request.body)
            schema = self._parse_schema(schema_data)
            
            # Get the number of rows to generate per table (default: 100)
            rows_per_table = int(request.query_params.get('rows_per_table', 100))
            
            # Generate the anonymized data
            generator = GenerateAnonymizedData(schema)
            generated_data = generator.generate(rows_per_table)
            
            return Response(status=200, data=generated_data)
            
        except json.JSONDecodeError:
            return Response(status=400, data={'error': 'Invalid JSON format'})
        except Exception as e:
            return Response(status=500, data={'error': str(e)})
    
    def _parse_schema(self, schema_data: dict) -> DatabaseSchema:
        tables = []
        
        for table_data in schema_data.get('tables', []):
            columns = []
            for column_data in table_data.get('columns', []):
                column = Column(
                    name=column_data['name'],
                    data_type=column_data['data_type'],
                    is_nullable=column_data.get('is_nullable', True),
                    is_primary_key=column_data.get('is_primary_key', False),
                    is_foreign_key=column_data.get('is_foreign_key', False),
                    referenced_table=column_data.get('referenced_table'),
                    referenced_column=column_data.get('referenced_column')
                )
                columns.append(column)
            
            table = Table(
                name=table_data['name'],
                columns=columns
            )
            tables.append(table)
        
        return DatabaseSchema(tables=tables) 