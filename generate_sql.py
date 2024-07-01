from src import create_app
from src.models import db

app = create_app()

with app.app_context():
    with open('setup.sql', 'w') as f:
        for table in db.metadata.sorted_tables:
            create_table_sql = str(table.to_metadata(db.metadata).create(db.engine, checkfirst=True)).strip()
            f.write(create_table_sql + ";\n")
