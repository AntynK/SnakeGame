import pickle

from game.restricted_unpickler import RestrictedUnpickler
from game.constants import SAVE_FILE_PATH


class Score:
    def __init__(self) -> None:
        self._current_score = 0
        self._record_score = 0
        self.load()

    def add(self, value: int):
        """Add value to score.

        Arg:
            value: Number which will be added to current score.
        Raises:
            TypeError: If value is not int type.
        """

        if not isinstance(value, int):
            raise TypeError(f"Arg value can be int, not: {type(value)}.")
        self._current_score += value
        if self._record_score < self._current_score:
            self._record_score = self._current_score

    def get_current(self) -> int:
        return self._current_score

    def get_record(self) -> int:
        return self._record_score

    def reset(self):
        self._current_score = 0

    def save(self):
        with open(SAVE_FILE_PATH, "wb") as file:
            pickle.dump(self._record_score, file)

    def load(self):
        try:
            with open(SAVE_FILE_PATH, "rb") as file:
                self._record_score = RestrictedUnpickler(file).load()
        except (OSError, pickle.UnpicklingError):
            self._record_score = 0
            self.save()
