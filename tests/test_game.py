import pytest
from shut_the_box.game import remove_numbers, is_win, play_turn, NoPossibleMoveError

def test_remove_numbers():
    remaining = {1, 2, 3, 4, 5}
    result = remove_numbers(remaining, {2, 4})

    assert result == {1, 3, 5}
    assert remaining == {1, 2, 3, 4, 5}

def test_is_win():
    assert is_win(set()) == True
    assert is_win({1}) == False
    assert is_win({1, 2, 3}) == False


def test_play_turn():
    remaining = {1, 2, 3, 4}
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr("shut_the_box.game.roll_dice", lambda: 5)
    monkeypatch.setattr("shut_the_box.game.possible_moves",lambda remaining, target: [{1, 4}, {2, 3}])
    monkeypatch.setattr("builtins.input", lambda _: "0")
    result = play_turn(remaining)

    assert result == {2, 3}

    monkeypatch.undo()

def test_no_possible_move():
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr("shut_the_box.game.roll_dice", lambda: 12)
    monkeypatch.setattr("shut_the_box.game.possible_moves",lambda remaining, target: [])

    with pytest.raises(NoPossibleMoveError):
        play_turn({1, 2, 3})

    monkeypatch.undo()