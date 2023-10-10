import time

from coder_retriever.utils.time import timing_decorator


def test_time_decorator():
    @timing_decorator
    def dummy_loop():
        for i in range(2):
            time.sleep(1)

    dummy_loop()
