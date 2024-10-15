from .schemas import Task, TaskCreateModel, TaskUpdateModel
from src.db.graphql_connection import GraphQLConnection
from datetime import datetime


class TaskService:
    async def get_all_tasks(self, auth_details: dict):
        graphql_connection = GraphQLConnection(auth_details)

        query_tasks = """
                query MyQuery {
                  tasks {
                    id,
                    title,
                    description,
                    is_completed,
                    created_at,
                    updated_at
                  }
                }
                """

        result = await graphql_connection.execute_query(query_tasks)
        result = result["tasks"]

        return result

    async def create_task(self, task_data: TaskCreateModel, auth_details: dict):
        graphql_connection = GraphQLConnection(auth_details)

        query_tasks = """
            mutation MyMutation($description: String!, $title: String!) {
              insert_tasks_one(
                object: {
                  title: $title,
                  description: $description
                }
              ) {
                        id
                        title
                        description
                        is_completed
                    }
            }
            """

        variables = {
            "title": f"{task_data.title}",
            "description": f"{'' if task_data.description is None else task_data.description}"
        }

        result = await graphql_connection.execute_query(query_tasks, variable_values=variables)
        result = result["insert_tasks_one"]
        return result

    async def get_task(self, task_id: int, auth_details: dict):
        graphql_connection = GraphQLConnection(auth_details)

        query_tasks = """
            query MyQuery($id: Int!) {
              tasks_by_pk(id: $id) {
                id
                description
                created_at
                is_completed
                title
                updated_at
              }
            }
        """

        variables = {
            "id": f"{task_id}"
        }

        result = await graphql_connection.execute_query(query_tasks, variable_values=variables)
        result = result["tasks_by_pk"]

        return result

    async def update_task(self, task_id: int, task_data: TaskUpdateModel, auth_details: dict):

        graphql_connection = GraphQLConnection(auth_details)

        query_tasks = """
            mutation UpdateQuery($id:Int!, $title:String!, $description: String = "", $is_completed: Boolean = false, $updated_at: timestamp = "") {
                update_tasks(
                _set: {title: $title, description: $description, is_completed: $is_completed, updated_at: $updated_at},
                where:{id:{_eq:$id}}){
                    affected_rows
                    returning {
                        created_at
                        description
                        id
                        is_completed
                        title
                        updated_at
                    }
                }
            }
        """

        variables = {
            "id": f"{task_id}",
            "title": f"{task_data.title}",
            "description": f"{'' if task_data.description is None else task_data.description}",
            "updated_at": datetime.utcnow().isoformat()
        }

        result = await graphql_connection.execute_query(query_tasks, variable_values=variables)

        if result["update_tasks"]["affected_rows"] == 1:
            result = result["update_tasks"]["returning"][0]
            return result
        else:
            return None

    async def delete_task(self, task_id: int, auth_details: dict):
        graphql_connection = GraphQLConnection(auth_details)

        query_tasks = """
            mutation MyMutation($id: Int!) {
              delete_tasks_by_pk(id: $id) {
                created_at
                description
                id
                is_completed
                title
                updated_at
              }
            }
        """

        variables = {
            "id": f"{task_id}"
        }

        result = await graphql_connection.execute_query(query_tasks, variable_values=variables)
        result = result["delete_tasks_by_pk"]

        return result
