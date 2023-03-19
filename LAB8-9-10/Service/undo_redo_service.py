from typing import List

from Domain.undo_redo_operation import UndoRedoOperation


class UndoRedoService:

    def __init__(self):
        self.undo_list: List[UndoRedoOperation] = []
        self.redo_list: List[UndoRedoOperation] = []

    def do_undo(self):
        if self.undo_list:
            top_operation = self.undo_list.pop()
            self.redo_list.append(top_operation)
            top_operation.undo()

    def do_redo(self):
        if self.redo_list:
            top_operation = self.redo_list.pop()
            self.undo_list.append(top_operation)
            top_operation.redo()

    def add_to_undo(self, operation: UndoRedoOperation):
        self.undo_list.append(operation)
        self.redo_list.clear()
