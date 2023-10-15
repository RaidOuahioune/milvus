from pymilvus import connections
from dotenv import load_dotenv




import os
load_dotenv()




class Db:
    """
    initialize the database object only when u need to redine the schema    
    """

    def __init__(self,alias="default") -> None:
        connections.connect(
        alias=alias,
        user=os.getenv("MILVUS_USERNAME"),
        password=os.getenv("MILVUS_PASSWORD"),
        host=os.getenv("MILVUS_HOST"),
        port=os.getenv("MILVUS_PORT")
        ) 
       
            
            
        