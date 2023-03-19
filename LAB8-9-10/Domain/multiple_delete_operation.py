from Domain.entity import Entity
from Domain.undo_redo_operation import UndoRedoOperation
from Repository.repository import Repository


class MultipleDeleteOperation(UndoRedoOperation):
    def __init__(self,
                 repository: Repository,
                 obiecte_sterse: list[Entity]):
        self.repository = repository
        self.obiecte_sterse = obiecte_sterse

    def undo(self):
        for entity in self.obiecte_sterse:
            self.repository.create(entity)

    def redo(self):
        for entity in self.obiecte_sterse:
            self.repository.delete(entity.id_entity)
