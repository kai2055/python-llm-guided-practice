
"""
LAZY vs EAGER LOGGING FORMATTING

- One of the most impactful micro-optimisations in production
Python.


WHY LOGGING?
--------------
"Lazy formatting" appears in several Python contexts (generators,
itertools, etc.), but the canonical, production-relevant home for
the lazy/eager distinction is the logging module.

It is the *only* place in the standard library where a framework
*owns* the string-building step and can skip it entirely based on a 
runtime condition (the active log level). That makes the cose
difference real, measurable, and something linters actually warn about.

Other lazy patterns (generators, lambdas) exist too, but they are
either contrived or solve a different problem (memory, iteration).
Logging is where this distincion has:
    1. A real performance consequence (shown below)
    2. An official recommendation (Python docs, PEP 8 style guides)
    3. A linter rule (flake8-logging-format, pylint W1201/W1202)

"""

import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)



# Eager Formatting (the bad pattern)

def eager_example():
    """String is built BEFORE the logger decides if it will be used."""
    user = {'id': 42, 'name': 'Flyin Monk', 'roles': list(range(100))}

    # THe f-string runs unconditionally - even if DEBUG is diasbled in prod
    logger.debug(f"User loaded: {user}")
    logger.debug("User loaded:" + str(user))



# Lazy formatting (the good pattern)


def lazy_example():
    """String is built ONLY IF the log level is active"""
    user = {'id': 42, 'name': 'Flyin Monk', 'roles':list(range(100))}

    # % placeholders: the logger skips formatting entirely whn level is off
    logger.debug("User loaded: %s", user)
    logger.info("User id=%d name=%s", user['id'], user['name'])




# Why it works: the logger's internal check

def explain_internals():
    """
    Pseudocode of what logging.Logger.debug() actually does:
        
        def debug(self, msg, *args):
            if self.isEnabledFor(DEBUG):        # <- level check FIRST
                self._log(DEBUG, msg, args)     # <- only NOW: msg %s args


            With EAGER formatting:
                logger.debug(f"x={expensive()}")
                # expensive() and f-string run BEFORE isENabledFor() is checked.
                # The string object is fully contructed and then silently thrown away.


            With LAZY formatting:
                logger.debug(f"x={expensive()}")
                # If DEBUG is off -> isEnabled() returns False immediately
                # expendive() is never called. msg % args never runs.


            This is why the distinction only "has teeth" inside the logging module:
            the framework controls when (and whether) the formatting happens.
            With a plain print() or an f-string outside logging, there is no
            framework to intercept - lazy patterns require manual guards instead
        
        
    """
    
    print(explain_internals.__doc__)



# Benchmark: measure the cost difference



def benchmark():
    # Simulate a production logger with DEBUG turned OFF
    prod_logger = logging.getLogger("prod")
    prod_logger.setLevel(logging.WARNING)       # DEBUG messages are silenced

    big_object = {'data': list(range(10_000))}
    iterations = 50_000


    # Eager: f-string is evaluated every single iteration
    start = time.perf_counter()
    for _ in range(iterations):
        prod_logger.debug(f"Object: {big_object}")  # str() called 50k times
    eager_time = time.perf_counter() - start


    # Lazy: formatting is skipped entirely because level check fails first
    start = time.perf_counter()
    for _ in range(iterations):
        prod_logger.debug("Object: %s", big_object) # str() never called
    lazy_time = time.perf_counter() - start


    print("\n=== BENCHMARK (DEBUG diabled, 50k iterations) ===")
    print(f"    Eager (f-string) : {eager_time * 1000:1f} ms")
    print(f"    Lazy (% style)   : {lazy_time * 1000:.1f} ms")
    print(f"    Speedup          : {eager_time / lazy_time:.0f}  x faster with lazy\n ")




# Outside logging: lazy patterns still exist, but look different


def outside_logging_example():
    """
    Outside the logging module, there is no framework to intercept
    formatting. You must guard manually when the computation is expensive.
    
    """

    DEBUG = False   # Simulated flag
    data = list(range(10_000))


    # Manual guard - the only way to get the laziness outside logging
    if DEBUG:
        print(f"data = {data}") # f-string only runs if DEBUG is True

    # A lambda defers the call, but you still have to call it yourself -
    # no framework does it for you. This is contrived practice.
    msg = lambda: f"data = {data}"
    if DEBUG:
        print(msg())





# REAL WORLD TIPS

TIPS = """
PRODUCTION RULES FOR LAZY LOGGING
------------------------------------------

1. Always use logger.debug("%msg %s", var)          not logger.debug(f"msg {var}")
2. Never pre-build the string:                      not msg = f"...."; logger.debug(msg)
3. For expensive payloads, add an explicit guard:
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug("Payload: %s", json.dumps(big_dict), indent=2)
4. % style (not f-strings) is offcial logging docs recommendation
5. Linters like flake8 with flake8-logging-format will catch eager patterns.


WHY NOT JUST USE F-STRINGS EVERYWHERE?
------------------------------------------
F-strings are great. USe them everywhere *except* inside logger calls.
The logging module is the one place in Python where the framework can
defer and skip string building for you - but only if you pass the raw
arguments. Give it an f-string and you have already done the work yourself.



"""


if __name__ == "__main__":
    print("--Eager examples (anti-patterns) --")
    eager_example()

    print("\n--Lazy examples (preferred)--")
    lazy_example()


    explain_internals()
    benchmark()
    print(TIPS)
    

