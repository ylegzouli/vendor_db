import os
import json
import zipfile
from datetime import datetime
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine

from src.config import Config

from typing import Optional, List, Any
from pydantic import BaseModel

class Store(BaseModel):
    name: Optional[str] = None
    icon: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    categories: Optional[List[str]] = None
    email: Optional[List] = None
    instagram: Optional[str] = None
    linkedin: Optional[str] = None
    facebook: Optional[str] = None
    phone: Optional[List] = None
    nb_employee: Optional[Any] = None
    ca: Optional[str] = None
    adress: Optional[str] = None
    source: Optional[str] = None
    create_at: Optional[str] = None
    location: Optional[str] = None
    country_code: Optional[str] = None

    def to_text(self):
        """Converts the store to a text representation for embedding."""
        if len(self.description) > 0:
            return self.description
        else:
            return "NO DESCRIPTION"


class Projects(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    project: str
    message_stack_json: str
    selected_message: str


class ProjectManager:
    def __init__(self):
        config = Config()
        sqlite_path = config.get_sqlite_db()
        self.project_path = config.get_projects_dir()
        self.engine = create_engine(f"sqlite:///{sqlite_path}")
        SQLModel.metadata.create_all(self.engine)


    def get_project_list(self):
        with Session(self.engine) as session:
            projects =  session.query(Projects).all()
            return [project.project for project in projects]


    def create_project(self, project: str):
        with Session(self.engine) as session:
            project_state = Projects(project=project, message_stack_json=json.dumps([]), selected_message=json.dumps([]))
            session.add(project_state)
            session.commit()

    def delete_project(self, project: str):
        with Session(self.engine) as session:
            project_state = session.query(Projects).filter(Projects.project == project).first()
            if project_state:
                session.delete(project_state)
                session.commit()


    def new_message(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return {
            "source": "",
            "message": None,
            "timestamp": timestamp
        }

    def add_message_to_project(self, project: str, data: dict):
        with Session(self.engine) as session:
            project_state = session.query(Projects).filter(Projects.project == project).first()
            if project_state:
                message_stack= data
                # message_stack = json.loads(project_state.message_stack_json)
                # message_stack.append(data)
                project_state.message_stack_json = json.dumps(message_stack)
                session.commit()
            else:
                message_stack= data
                project_state = Projects(project=project, message_stack_json=json.dumps(data))
                session.add(project_state)
                session.commit()


    def get_messages(self, project: str):
        with Session(self.engine) as session:
            project_state = session.query(Projects).filter(Projects.project == project).first()
            if project_state:
                return json.loads(project_state.message_stack_json)
            return None


    def get_stores(self, project: str) -> List[Store]:
        with Session(self.engine) as session:
            project_state = session.query(Projects).filter(Projects.project == project).first()
            if project_state:
                message_stack = json.loads(project_state.message_stack_json)
                return [Store.model_validate(store) for store in message_stack['message']]
            return []


    def add_store_to_project(self, project_name: str, store: Store):
        with Session(self.engine) as session:
            project = session.query(Projects).filter(Projects.project == project_name).first()
            if project:
                message_stack = json.loads(project.message_stack_json)
                message_stack['message'].append(store.model_dump())
                project.message_stack_json = json.dumps(message_stack)
                session.commit()


    def delete_store_from_project(self, project_name: str, store_name: str):
        with Session(self.engine) as session:
            project = session.query(Projects).filter(Projects.project == project_name).first()
            if project:
                message_stack = json.loads(project.message_stack_json)
                message_stack['message'] = [store for store in message_stack['message'] if store['name'] != store_name]
                project.message_stack_json = json.dumps(message_stack)
                session.commit()


    def store_to_selected(self, project_name, store_name):
        with Session(self.engine) as session:
            project = session.query(Projects).filter(Projects.project == project_name).first()
            if project:
                message_stack = json.loads(project.message_stack_json)
                stores =  [Store.model_validate(store) for store in message_stack['message']]
            else:
                stores = []
            selected_stack = json.loads(project.selected_message)
            for store in stores:
                if store.name == store_name:
                    selected_stack.append(store.model_dump())
            project.selected_message = json.dumps(selected_stack)
            session.commit()


    def get_selected_stores(self, project: str) -> List[Store]:
        with Session(self.engine) as session:
            project_state = session.query(Projects).filter(Projects.project == project).first()
            if project_state:
                selected_stack = json.loads(project_state.selected_message)
                return [Store.model_validate(store).model_dump() for store in selected_stack]
            return []

    def delete_selected_store(self, project_name: str, store_name: str):
        with Session(self.engine) as session:
            project = session.query(Projects).filter(Projects.project == project_name).first()
            if project:
                # Load the list of selected stores from the project's selected_message field
                selected_stores = json.loads(project.selected_message)
                # Filter out the store to delete based on its name
                updated_selected_stores = [store for store in selected_stores if store['name'] != store_name]
                # Update the project's selected_message field with the new list of stores
                project.selected_message = json.dumps(updated_selected_stores)
                session.commit()

    # def add_message_from_devika(self, project: str, message: str):
    #     new_message = self.new_message()
    #     new_message["message"] = message
    #     self.add_message_to_project(project, new_message)
        
    # def add_message_from_user(self, project: str, message: str):
    #     new_message = self.new_message()
    #     new_message["message"] = message
    #     new_message["from_devika"] = False
    #     self.add_message_to_project(project, new_message) 

    # def get_latest_message_from_user(self, project: str):
    #     with Session(self.engine) as session:
    #         project_state = session.query(Projects).filter(Projects.project == project).first()
    #         if project_state:
    #             message_stack = json.loads(project_state.message_stack_json)
    #             for message in reversed(message_stack):
    #                 if not message["from_devika"]:
    #                     return message
    #         return None

    # def validate_last_message_is_from_user(self, project: str):
    #     with Session(self.engine) as session:
    #         project_state = session.query(Projects).filter(Projects.project == project).first()
    #         if project_state:
    #             message_stack = json.loads(project_state.message_stack_json)
    #             if message_stack:
    #                 return not message_stack[-1]["from_devika"]
    #         return False

    # def get_latest_message_from_devika(self, project: str):
    #     with Session(self.engine) as session:
    #         project_state = session.query(Projects).filter(Projects.project == project).first()
    #         if project_state:
    #             message_stack = json.loads(project_state.message_stack_json)
    #             for message in reversed(message_stack):
    #                 if message["from_devika"]:
    #                     return message
    #         return None

    # def get_all_messages_formatted(self, project: str):
    #     formatted_messages = []
        
    #     with Session(self.engine) as session:
    #         project_state = session.query(Projects).filter(Projects.project == project).first()
    #         if project_state:
    #             message_stack = json.loads(project_state.message_stack_json)
    #             for message in message_stack:
    #                 if message["from_devika"]:
    #                     formatted_messages.append(f"Devika: {message['message']}")
    #                 else:
    #                     formatted_messages.append(f"User: {message['message']}")
                        
    #         return formatted_messages

    # def get_project_path(self, project: str):
    #     return os.path.join(self.project_path, project.lower().replace(" ", "-"))
    
    # def project_to_zip(self, project: str):
    #     project_path = self.get_project_path(project)
    #     zip_path = f"{project_path}.zip"

    #     with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    #         for root, dirs, files in os.walk(project_path):
    #             for file in files:
    #                 relative_path = os.path.relpath(os.path.join(root, file), os.path.join(project_path, '..'))
    #                 zipf.write(os.path.join(root, file), arcname=relative_path)
                    
    #     return zip_path
    
    # def get_zip_path(self, project: str):
    #     return f"{self.get_project_path(project)}.zip"