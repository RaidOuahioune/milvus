import abc
from pymilvus import Collection
class BaseSchema(abc.ABC):
    """_summary_
    You must write all the collection attrubutes in this class like this 
    ```python
     book_id = FieldSchema(
      name="id",
      dtype=DataType.INT64,
      is_primary=True,
    )
    ```
    """
    @abc.abstractstaticmethod
    def collection()->Collection:
        pass