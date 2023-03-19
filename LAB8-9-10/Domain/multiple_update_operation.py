from Domain.entity import Entity
from Domain.undo_redo_operation import UndoRedoOperation
from Repository.repository import Repository


class MultipleUpdateOperation(UndoRedoOperation):
    def __init__(self,
                 repository: Repository,
                 old_obj_list: list[Entity],
                 new_obj_list: list[Entity]):
        self.repository = repository
        self.old_obj_list = old_obj_list
        self.new_obj_list = new_obj_list

    def undo(self):
        for entity in self.old_obj_list:
            self.repository.update(entity)

    def redo(self):
        for entity in self.new_obj_list:
            self.repository.update(entity)
