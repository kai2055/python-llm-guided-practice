

"""
Big idea
- An exception is Python's way of saying: "Something went wrong, and I am handing you a structured error object.
- A traceback is the "path" (call stack) showing where the error traveled.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass
from typing import Callable, Iterable, Optional, Type, Tuple



# Exception Context and Chaining


class ConfigError(Exception):
    """
    A custom exception.

    Definition:
    - Custom exceptions help you name errors in a way that matches your domain.
      Example: ConfigError, DatabaseError, ParsingError.

    Analogy:
    - Instead of shouting "Something is wrong", you say "Configuration is wrong!"
      That makes debugging faster and error handling cleaner.
    
    """


def parse_port_from_config(config_text: str) -> int:
    """
    Convert a config value into an integer port.

    We intentionally keep it small and realistic:
    - Imagine config_text was read from a config file or env var.
    - If it's not a valid integer, int(...) raises ValueError.

    Key teaching point:
    - We will wrap the ValueError into a ConfigError using 'raise .... from ...'
    so we keep the original error context.
    
    """

    try:
        port = int(config_text) # can raise ValueError
        if not (1 <= port <= 65535):
            # This is a "domain rule" error (valid int, but invalid range)
            raise ValueError(f"Port out of range: {port}")
        return port
    
    except ValueError as original_error:
        # DEFINITION: Exception chaining ('raise X from Y')
        # - X is the higher-level error you wnat your app to speak in
        # - Y is the original low-level error that actually happened

        # Analogy:
        # - You are a manager reporting a problem to the CEO:
        #   "Our config is invalid" (COnfigError)
        #   But you attach the original technician report (ValueError)

        # Why it's useful:
        # - Your logs/traceback show BOTH the high-level and origianl causes.
        raise ConfigError(f"Invalid port value in config: {config_text!r}") from original_error
    


def nested_call_chain_for_traceback_demo(config_text: str) -> int:
    """
    This exists to show how tracebacks look in nested calls.
    The error starts deep inside parse_port_from_config(...) and bubbles up.

    """
    return parse_port_from_config(config_text)


def option_a_demo() -> None:
    """
    Demonstrates:
    - letting exceptions propagate
    - wrapping with chaining (raise.... from .....)
    - what tracebacks mean in nested calls

    Not:
    - The traceback itself appears when an exception is uncaught.
      Here we catch it to print a clean messge, but we also show how to  inspect
      the cause ('__cause__') from chaining.
    
    """
    print("\n=== Demo: Exception Context and Chaining ===")


    bad_config_value = "eighty"     # not an integer

    try:
        port = nested_call_chain_for_traceback_demo(bad_config_value)
        print(f"Parsed port: {port}")
    except ConfigError as e:
        print("Caught ConfigError", e)

        # When you use 'raise X from Y', Python stores Y in e.__cause__
        if e.__cause__ is not None:
            print("Original cause typr:", type(e.__cause__).__name__)
            print("Original cause message:", e.__cause__)

        # When to wrap vs when to propogate (simple rules):

        # WRAP when:
        # - You want a clearer domain message for your app/user/logs.
        # - The caller shouldn't care about low-level details (ValueError, KeyError)

        # LET IT PROPOGATE when:
        # - The exception already clearly explains the problem.
        # - You can't add helpful context
        # - You are in a library function and the caller might want to decide.

        # In real apps:
        # - You often wrap at boundaries: "reading config", "talking to DB", calling API



# Option B: Error Recovery and Retry Logic


class TransientError(Exception):
    """
    Definition:
    - Transient failure: might suceed if you try agian.
      Examples: temporary network glitch, rate limit, timeouts.

    """


class PermanentError(Exception):
    """
    Definition:
    - Permanent failure: retrying won't help (or usually won't).
      Examples: invalid credentials, invalid input, "file not found"
    
    """

@dataclass(frozen=True)
class RetryPolicy:
    """
    A simple config object for retry logic.


    Definitions:
    - retries: how many times to rettry after the intial attemp fails.
    - base_delay: starting wait time between retries (seconds)
    - max_delay: cap the delay (seconds)
    - backoff_factor: multiplier each retry (exponential backoff)
    - jitter: small randomness added to prevent "thundering herd" retries

    Analogy:
    - Knocking on a door:
        - First knock: immediate
        - If no answer, wait a bit.
        - If still no answer, wait longer next time.
        - Add a tiny random pause so a whole crowd doesn't knock again at the same time.

    """
    retries: int = 3
    base_delay: float = 0.3
    max_delay: float = 2.0
    backoff_factor: float = 2.0
    jitter: float = 0.1




def compute_backoff_delay(
        attempt_number: int,
        policy: RetryPolicy,

) -> float:
    """
    Compute exponential backoff delay.

    
    attempt_number:
     1 for first retry wait, 2 for second retry wait, ...

     delay = min(base_delay * (backoff_factor ** (attempt_number - 1)), max_delay)
     then add jitter in range [0, jitter]
    
    """
    delay = policy.base_delay * (policy.backoff_factor ** (attempt_number - 1))
    delay = min(delay, policy.max_delay)
    delay += random.uniform(0, policy.jitter)
    return delay



def retry(
        func: Callable[[], str],
        *,
        retry_on: Tuple[Type[BaseException], ...],
        fail_fast_on: Tuple[Type[BaseException], ...],
        policy: RetryPolicy,
) -> str:
    """
    A reusable retry helper.

    Teaches:
    - Catch specific exceptions (don't use bare 'except': unless you truly mean it)
    - Retry only transient exceptions
    - Fail fast on permanent exceptions
    - Exponential backoff with jitter

    Real use cases:
    - calling APIs
    - reading from a flaky service
    - temporary file locks

    """

    total_attempts = 1 + policy.retries  # initial try + retries

    for attempt_index in range(1, total_attempts + 1):
        try:
            return func()
        
        except fail_fast_on as e:
            # Permanent error (or you decided should not be retried)
            raise PermanentError(f"Fail-fast: {e}") from e
        
        except retry_on as e:
            # Transient error: only retry if we still have attemps left
            if attempt_index == total_attempts:
                raise TransientError(
                    f"Exhausted retries after {total_attempts} attempts: {e}"
                ) from e
            
            wait_seconds = compute_backoff_delay(attempt_index, policy)
            print(
                f"[retry] Attempt {attempt_index}/{total_attempts} failed ({type(e).__name__}: {e})."
                f"Waiting {wait_seconds:.2f}s then retrying..."
            )
            time.sleep(wait_seconds)




def simulated_api_call() -> str:
    """
    A fake API call that sometimes fails transiently and somettimes permanently.


    Why simulate?
    - You can practice retry logic without needing  without needing real network calls.


    Behavior:
    - 60% cahnce transient failure
    - 10% chance permanent failure
    - 30% success
    
    """
    roll = random.random()

    if roll < 0.60:
        raise TransientError("Temporary network glitch (simulated)")
    if roll < 0.70:
        raise PermanentError("Bad API key / invalid request (simulated)")
    
    return "Success: got API response"



def option_b_demo() -> None:
    """
    Demonstrates a practical retry setup:
    - retry TransientError
    - fial fast on PermanentError
    - show waits with exponential backoff
    
    """
    print("\n=== Option B Demo: Error Recovery and Retry Logic ===")\
    
    policy = RetryPolicy(
        retries=4,
        base_delay=0.2,
        max_delay=1.0,
        backoff_factor=2.0,
        jitter=0.2,

    )

    try:
        result = retry(
            simulated_api_call,
            retry_on=(TransientError,),
            fail_fast_on=(PermanentError,),
            policy=policy,
        )
        print("Final result:", result)

    except PermanentError as e:
        print("Permanent failure (no retries)", e)

    except TransientError as e:
        print("Transient failure (retries exhausted:)", e)




# Context Managers with Error Handling


class FakeResource:
    """
    A tiny "resource" to demonstrate safe setup/cleanup.


    Think of it like:
    - a file handle
    - a database connection
    - a lock
    - a network socket


    Key rule:
    - Resources must be cleaned up when errors happen.
    
    """
    def __init__(self) -> None:
        self.opened = False


    def open(self) -> None:
        self.opened = True
        print("[resource] Opened resource")


    def close(self) -> None:
        self.opened = False
        print("[resource] Closed resource")

    def do_work(self) -> None:
        print("[resource] DOing work...")
        # SOmetimes the work fails, like a real system might

        if random.random() < 0.5:
            raise RuntimeError("Something went wrong during resource work (simulated)")
        

class ManagedResource:
    """
    Custom context manager using __enter__ and __exit__.
    """

    def __init__(self, *, suppress_exceptions: bool = False) -> None:
        self._resource = FakeResource()
        self._suppress = suppress_exceptions

    def __enter__(self) -> FakeResource:
        self._resource.open()
        return self._resource

    def __exit__(
        self,
        exc_type: Optional[type],
        exc: Optional[BaseException],
        tb: Optional[object],
    ) -> bool:
        # Cleanup ALWAYS runs
        self._resource.close()

        if exc is None:
            print("[manager] Exited normally (no exception).")
            return False

        print(f"[manager] Exited with exception: {exc_type.__name__}: {exc}")
        return self._suppress

    

def option_c_demo() -> None:
    """
    Demonstrates:
    - cleanup running even when wxceptions happen
    - supression vs propogation
    
    """

    print("\n=== Option C Demo: Context Managers with Error Handling ===")

    print("\n-- Case 1: Propogate exceptions (recommended default) --")
    try:
        with ManagedResource(suppress_exceptions=False) as r:
            r.do_work()
            print("[main] work completed inside with-block")
    except RuntimeError as e:
        print("[main] caought propogated exception", e)


    print("\n-- Case2: Supress exceptions (use carefully) --")
    with ManagedResource(suppress_exceptions=True) as r:
        r.do_work()
        print("[main] If an error happened above, it was supressed, so code continues here.")





# A simple main menu


def main() -> None:
    """
    Simple CLI menu

    Tip:
    - Re-run demos multiple times because randomness changes behavior.
    - The remove randomness and create your own scenarios
    
    """

    random.seed()   # non-determenistic

    options = {
        "a": ("Exception Context and Chaining", option_a_demo),
        "b": ("Error Recovery and Retry Logic", option_b_demo),
        "c": ("Context Managers with Error handling", option_c_demo),
        "q": ("Quit", None)

    }

    while True:
        print("\n=======================")
        print("Python Error-handling ")
        print("=========================")
        for key, (label, _) in options.items():
            print(f"{key}) {label}")

        choice = input("\nChoose an option (a/b/c) or q to quit: ").strip().lower()

        if choice == "q":
            print("Bye")
            return
        
        if choice not in options:
            print("Invalid choice. Try again.")
            continue

        _, func = options[choice]
        if func is not None:
            func()


if __name__ == "__main__":
    main()


