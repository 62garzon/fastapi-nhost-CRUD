from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from src.config import Config
from typing import Any, Optional, Dict
from src.auth.utils import encode_token


class GraphQLConnection:
    def __init__(self, auth_details: dict):
        token = encode_token(auth_details)

        self.transport = AIOHTTPTransport(url=Config.NHOST_HASURA_URL, headers={
            'Authorization': f'Bearer {token}'})
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    async def execute_query(self, query_str: str, variable_values: Optional[Dict[str, Any]] = None ):
        query = gql(
            query_str
        )
        result = await self.client.execute_async(query, variable_values=variable_values)
        return result
