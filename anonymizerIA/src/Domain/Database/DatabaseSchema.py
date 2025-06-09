from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Column:
    name: str
    data_type: str
    is_nullable: bool
    is_primary_key: bool
    is_foreign_key: bool
    referenced_table: str = None
    referenced_column: str = None

@dataclass
class Table:
    name: str
    columns: List[Column]

@dataclass
class DatabaseSchema:
    tables: List[Table]
    
    def get_table(self, table_name: str) -> Table:
        for table in self.tables:
            if table.name == table_name:
                return table
        return None
    
    def get_foreign_key_relationships(self) -> Dict[str, List[Dict[str, str]]]:
        relationships = {}
        for table in self.tables:
            table_relationships = []
            for column in table.columns:
                if column.is_foreign_key:
                    table_relationships.append({
                        'column': column.name,
                        'referenced_table': column.referenced_table,
                        'referenced_column': column.referenced_column
                    })
            if table_relationships:
                relationships[table.name] = table_relationships
        return relationships 