import importlib.util
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("main", ROOT / "conveyor_lane.py")
main = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(main)
sort_k_sorted = main.sort_k_sorted

# --- normal (4) ---
def test_example_1():
    arr = [2,6,3,12,56,8]
    assert sort_k_sorted(arr, 3) == [2,3,6,8,12,56]

def test_small_2():
    assert sort_k_sorted([3,1,2], 2) == [1,2,3]

def test_k_zero():
    assert sort_k_sorted([1,2,3,4], 0) == [1,2,3,4]

def test_reverse_with_k():
    assert sort_k_sorted([4,3,2,1], 3) == [1,2,3,4]

# --- edge (3) ---
def test_empty():
    assert sort_k_sorted([], 3) == []

def test_k_big():
    arr = [5,4,3,2,1]
    assert sort_k_sorted(arr, 10) == sorted(arr)

def test_duplicates():
    arr = [3,3,3,2,2,1]
    # Changed k=5 to match max displacement
    assert sort_k_sorted(arr, 5) == [1,2,2,3,3,3]

# --- complex (3) ---
def test_already_sorted_large_k():
    arr = list(range(50))
    assert sort_k_sorted(arr, 20) == list(range(50))

def test_random_like_fixed_compare_sorted():
    arr = [10, 12, 11, 13, 15, 14, 16, 18, 17, 19]
    assert sort_k_sorted(arr, 2) == sorted(arr)

def test_longer_case_compare_sorted():
    arr = [9,8,7,6,5,4,3,2,1,0]
    assert sort_k_sorted(arr, 9) == sorted(arr)
