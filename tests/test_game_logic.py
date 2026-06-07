import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, get_range_for_difficulty


# --- check_guess (pre-existing, corrected to unpack tuple) ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- get_range_for_difficulty (targets the new-game reset bug) ---
# Bug: new_game used hardcoded randint(1, 100) instead of calling
# get_range_for_difficulty, so Hard games would silently generate
# secrets above 50 and Easy games would generate secrets above 20.

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20  # was broken: hardcoded new_game used 100

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50  # was broken: hardcoded new_game used 100

def test_unknown_difficulty_defaults_to_normal():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100
