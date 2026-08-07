from agno.knowledge.embedder.sentence_transformer import SentenceTransformerEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.docling_reader import DoclingReader
from agno.vectordb.lancedb import LanceDb, SearchType

# Настраиваем локальный эмбеддер
embedder = SentenceTransformerEmbedder(id="all-MiniLM-L6-v2")
# Настраиваем векторную базу данных
vector_db = LanceDb(
	table_name="docling_documents",
	uri="knowledge",
	search_type=SearchType.hybrid,
	embedder=embedder
)

# Создаем объект базы знаний
knowledge = Knowledge(vector_db=vector_db)

from pathlib import Path

def ingest_documents():
	for file in Path("znania").rglob("*"):
		if file.is_file():
			knowledge.insert(
				name=file.name,
				path=str(file),
				reader=DoclingReader(output_format="markdown"),
				skip_if_exists=True
			)


ingest_documents()
