from typing import Dict, List, Any
import random
import string
from datetime import datetime, timedelta
from anonymizerIA.src.Domain.Database.DatabaseSchema import DatabaseSchema, Table, Column
from anonymizerIA.src.Infrastructure.Repositories.GeminiAIRepository import GeminiAIRepository

class GenerateAnonymizedData:
    def __init__(self, schema: DatabaseSchema):
        self.schema = schema
        self.generated_data = {}
        self.gemini_repo = GeminiAIRepository()
        
    def generate(self, rows_per_table: int = 100) -> Dict[str, List[Dict[str, Any]]]:
        # First pass: Generate data for all tables
        for table in self.schema.tables:
            self.generated_data[table.name] = []
            for _ in range(rows_per_table):
                row_data = self._generate_row_data(table)
                self.generated_data[table.name].append(row_data)
        
        # Second pass: Resolve foreign key relationships
        self._resolve_foreign_keys()
        
        return self.generated_data
    
    def _generate_row_data(self, table: Table) -> Dict[str, Any]:
        row_data = {}
        for column in table.columns:
            if column.is_primary_key:
                row_data[column.name] = self._generate_primary_key(table.name, column)
            else:
                row_data[column.name] = self._generate_value(column, table)
        return row_data
    
    def _generate_primary_key(self, table_name: str, column: Column) -> Any:
        # Generate a unique ID for the primary key
        if not hasattr(self, '_id_counters'):
            self._id_counters = {}
        if table_name not in self._id_counters:
            self._id_counters[table_name] = 0
        self._id_counters[table_name] += 1
        return self._id_counters[table_name]
    
    def _generate_value(self, column: Column, table: Table) -> Any:
        if column.is_foreign_key:
            return None  # Will be resolved in second pass
        
        context = {
            'table_name': table.name,
            'is_foreign_key': column.is_foreign_key,
            'referenced_table': column.referenced_table
        }
        
        return self.gemini_repo.generate_realistic_data(
            column_name=column.name,
            data_type=column.data_type,
            context=context
        )
    
    def _resolve_foreign_keys(self):
        relationships = self.schema.get_foreign_key_relationships()
        for table_name, foreign_keys in relationships.items():
            for fk in foreign_keys:
                column = fk['column']
                ref_table = fk['referenced_table']
                ref_column = fk['referenced_column']
                
                # Get all possible values from referenced table
                ref_values = [row[ref_column] for row in self.generated_data[ref_table]]
                
                # Update foreign key values in the current table
                for row in self.generated_data[table_name]:
                    if row[column] is None:  # Only update if not already set
                        row[column] = random.choice(ref_values) 