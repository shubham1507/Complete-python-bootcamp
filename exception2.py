"""
exception_demo.py
Run this file directly:  python exception_demo.py
It will demonstrate handling of common Python exceptions with clear output.
"""

from typing import Any, Dict, List

def demo_attribute_error() -> None:
    print("\n[AttributeError] Demo:")
    try:
        text = "hello"
        # str has no .append(); this will raise AttributeError
        text.append("world")
    except AttributeError as e:
        print("  -> Caught AttributeError:", e)
    else:
        print("  -> No error")
    finally:
        print("  -> Finished AttributeError demo")

def demo_value_error() -> None:
    print("\n[ValueError] Demo:")
    try:
        # invalid literal for int()
        num = int("abc")
        print("  -> Converted:", num)
    except ValueError as e:
        print("  -> Caught ValueError:", e)
    finally:
        print("  -> Finished ValueError demo")

def demo_index_error() -> None:
    print("\n[IndexError] Demo:")
    try:
        items: List[int] = [1, 2, 3]
        print(items[5])  # out of range
    except IndexError as e:
        print("  -> Caught IndexError:", e)
    finally:
        print("  -> Finished IndexError demo")

def demo_type_error() -> None:
    print("\n[TypeError] Demo:")
    try:
        result = "hello" + 5  # str + int not allowed
        print("  -> Result:", result)
    except TypeError as e:
        print("  -> Caught TypeError:", e)
    finally:
        print("  -> Finished TypeError demo")

def demo_zero_division_error() -> None:
    print("\n[ZeroDivisionError] Demo:")
    try:
        x = 10 / 0
        print("  -> Result:", x)
    except ZeroDivisionError as e:
        print("  -> Caught ZeroDivisionError:", e)
    finally:
        print("  -> Finished ZeroDivisionError demo")

def demo_key_error() -> None:
    print("\n[KeyError] Demo:")
    try:
        user: Dict[str, Any] = {"name": "Shubham", "role": "DevOps"}
        print("  -> Age:", user["age"])  # missing key
    except KeyError as e:
        print("  -> Caught KeyError:", e)
        # Safer alternative using dict.get()
        print("  -> Safer: user.get('age') ->", user.get("age", "not provided"))
    finally:
        print("  -> Finished KeyError demo")

def demo_file_not_found_error() -> None:
    print("\n[FileNotFoundError] Demo:")
    try:
        with open("missing.txt", "r", encoding="utf-8") as f:
            data = f.read()
            print("  -> File content length:", len(data))
    except FileNotFoundError as e:
        print("  -> Caught FileNotFoundError:", e)
        print("  -> Tip: Check path or create the file before reading.")
    finally:
        print("  -> Finished FileNotFoundError demo")

# ---------- Bonus: Safe helper functions that avoid exceptions ----------

def safe_int(value: str, default: int = 0) -> int:
    """Convert string to int safely; return default on ValueError."""
    try:
        return int(value)
    except ValueError:
        return default

def safe_get(seq: List[Any], index: int, default: Any = None) -> Any:
    """Safe list indexer; returns default if out-of-range."""
    try:
        return seq[index]
    except IndexError:
        return default

def safe_div(a: float, b: float, default: float | None = None) -> float | None:
    """Safe division; returns default if divide-by-zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return default

def safe_read(path: str, default: str = "") -> str:
    """Safe file reader; returns default string if file missing."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return default

# -----------------------------------------------------------------------

def main() -> None:
    print("=== Exception Handling Mega Demo ===")

    demo_attribute_error()
    demo_value_error()
    demo_index_error()
    demo_type_error()
    demo_zero_division_error()
    demo_key_error()
    demo_file_not_found_error()

    print("\n[Bonus] Using safe helper functions (no exceptions thrown):")
    print("  -> safe_int('42') =", safe_int("42"))
    print("  -> safe_int('abc', default=-1) =", safe_int("abc", default=-1))
    print("  -> safe_get([10, 20, 30], 5, default='NA') =", safe_get([10, 20, 30], 5, default="NA"))
    print("  -> safe_div(10, 0, default=float('inf')) =", safe_div(10, 0, default=float('inf')))
    print("  -> len(safe_read('missing.txt')) =", len(safe_read("missing.txt")))

    print("\n=== Done ===")

if __name__ == "__main__":
    main()
