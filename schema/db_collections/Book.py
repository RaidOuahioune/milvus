from pymilvus import CollectionSchema, FieldSchema, DataType,Collection
import BaseSchema
class Book(BaseSchema):
    
    
    book_id = FieldSchema(
      name="id",
      dtype=DataType.INT64,
      is_primary=True,
    )
    name = FieldSchema(
      name="name",
      dtype=DataType.VARCHAR,
      max_length=200,
      default_value="Unknown"
    )
    word_count = FieldSchema(
      name="word_count",
      dtype=DataType.INT64,
      default_value=0
    )
    intro = FieldSchema(
      name="intro",
      dtype=DataType.FLOAT_VECTOR,
      dim=2
    )
    schema = CollectionSchema(
      fields=[book_id, name, word_count, intro],
      description="Test book search",
      enable_dynamic_field=True
    )
    collection_name = "books"
    @staticmethod 
    def collection(alias="default")->Collection:
        collection = Collection(
        name=Book.collection_name,
        schema=Book.schema,
        using=alias,
        shards_num=2
      )
        return collection
Book.collection()