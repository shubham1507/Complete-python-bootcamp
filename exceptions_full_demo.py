"""
exceptions_full_demo.py

Run:
    python exceptions_full_demo.py

This single script demonstrates:
1) Handling common built-in exceptions with try/except/else/finally
2) Defining and using custom (user-defined) exceptions
3) Re-raising exceptions to propagate errors after partial handling
"""

from __future__ import annotations
from typing import Any, Dict, List


# ==============================
# 1) Built-in exception handling
# ==============================

def demo_builtins() -> None:
    print("\n=== 1) Built-in Exceptions Demo ===")

    # AttributeError
    try:
        s = "hello"
        s.append("world")  # str has no attribute 'append'
    except AttributeError as e:
        print("[AttributeError] ->", e)
    finally:
        print("  finished AttributeError example")

    # ValueError
    try:
        n = int("abc")
    except ValueError as e:
        print("[ValueError] ->", e)
    finally:
        print("  finished ValueError example")

    # IndexError and TypeError together
    try:
        items: List[int] = [10, 20, 30]
        x = items[5] / "a"  # may throw IndexError first
        print(x)
    except IndexError as e:
        print("[IndexError] ->", e)
    except TypeError as e:
        print("[TypeError] ->", e)
    finally:
        print("  finished IndexError/TypeError example")

    # ZeroDivisionError
    try:
        _ = 5 / 0
    except ZeroDivisionError as e:
        print("[ZeroDivisionError] ->", e)
    finally:
        print("  finished ZeroDivisionError example")

    # KeyError
    try:
        user: Dict[str, Any] = {"name": "Shubham", "role": "DevOps"}
        print("age:", user["age"])
    except KeyError as e:
        print("[KeyError] ->", e, "| safer:", user.get("age", "not provided"))
    finally:
        print("  finished KeyError example")

    # FileNotFoundError
    try:
        with open("missing.txt", "r", encoding="utf-8") as f:
            _ = f.read()
    except FileNotFoundError as e:
        print("[FileNotFoundError] ->", e)
    finally:
        print("  finished FileNotFoundError example")


# ==================================
# 2) Custom (user-defined) exceptions
# ==================================

class BankingError(Exception):
    """Base class for banking-related errors."""
    pass

class InsufficientFundsError(BankingError):
    def __init__(self, balance: float, amount: float):
        super().__init__(f"Attempted to withdraw {amount}, but balance is {balance}.")
        self.balance = balance
        self.amount = amount

class UnauthorizedAccessError(BankingError):
    def __init__(self, message: str = "Unauthorized action"):
        super().__init__(message)

class InvalidAmountError(BankingError):
    def __init__(self, amount: float):
        super().__init__(f"Invalid amount: {amount}. Amount must be positive.")
        self.amount = amount


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError(amount)
        self.balance += amount
        print(f"[Deposit] New balance: {self.balance:.2f}")

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"[Withdraw] New balance: {self.balance:.2f}")
        return self.balance


def demo_custom_exceptions() -> None:
    print("\n=== 2) Custom Exceptions Demo (Banking) ===")
    acct = BankAccount("Shubham", balance=500.0)

    # Happy path
    acct.deposit(250)

    # Invalid amount
    try:
        acct.deposit(-10)
    except InvalidAmountError as e:
        print("[InvalidAmountError]", e)

    # Insufficient funds
    try:
        acct.withdraw(2000)
    except InsufficientFundsError as e:
        print("[InsufficientFundsError]", e)

    # Successful withdraw
    acct.withdraw(300)


# =========================================
# 3) Re-raising exceptions (propagating up)
# =========================================

def risky_parse_and_divide(num_str: str, denom: int) -> float:
    """
    Parse num_str into int, divide by denom.
    Demonstrates catching, logging, then re-raising to caller.
    """
    try:
        n = int(num_str)  # can raise ValueError
        return n / denom  # can raise ZeroDivisionError
    except ValueError as e:
        print("[risky_parse_and_divide] Logging ValueError:", e)
        # Re-throw so callers can handle appropriately
        raise
    except ZeroDivisionError as e:
        print("[risky_parse_and_divide] Logging ZeroDivisionError:", e)
        # Wrap into a more domain-specific error if you want
        raise


def demo_reraise() -> None:
    print("\n=== 3) Re-raise Demo ===")
    cases = [("100", 5), ("abc", 5), ("42", 0)]
    for s, d in cases:
        try:
            result = risky_parse_and_divide(s, d)
        except Exception as e:
            print(f"  case ({s!r}, {d}) -> handled by caller:", type(e).__name__, "->", e)
        else:
            print(f"  case ({s!r}, {d}) -> result:", result)


# =========
# Utilities
# =========

def safe_read(path: str, default: str = "") -> str:
    """Example utility that handles a built-in exception internally (no raise)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return default


def main() -> None:
    print("==== Exceptions: Built-ins + Custom + Re-raise (Single Script) ====")
    demo_builtins()
    demo_custom_exceptions()
    demo_reraise()

    print("\n=== Utility example (no exception thrown to caller) ===")
    print("safe_read('missing.txt') ->", repr(safe_read("missing.txt")))
    print("\nDone.")


if __name__ == "__main__":
    main()
