from Domain.entity import Entity
from Domain.undo_redo_operation import UndoRedoOperation
from Repository.repository import Repository


class UpdateOperation(UndoRedoOperation):

    def __init__(self,
                 repository: Repository,
                 old_entity: Entity,
                 updated_entity: Entity):
        self.repository = repository
        self.old_entity = old_entity
        self.updated_entity = updated_entity

    def undo(self):
        self.repository.update(self.old_entity)

    def redo(self):
        self.repository.update(self.updated_entity)
