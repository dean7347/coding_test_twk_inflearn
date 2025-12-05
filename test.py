# test.py
import sys
from solution import solution  # solution은 input() 기반
from io import StringIO
import builtins
import time
import tracemalloc

# 0 = 전체 테스트 실행, 1 = 1번 테스트만 실행
RUN_FLAG = 0
TOTAL_TEST = 5  # 총 테스트 수


class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def estimate_complexity(exec_time_ms: float) -> str:
    """실행 시간 기준으로 대략적인 시간복잡도 느낌만 보여주는 용도(정확 X)"""
    if exec_time_ms < 0.01:
        return "O(1) ~ O(log n) (매우 빠름)"
    elif exec_time_ms < 0.1:
        return "O(log n) ~ O(n) (빠름)"
    elif exec_time_ms < 1:
        return "O(n) ~ O(n log n) (보통)"
    elif exec_time_ms < 10:
        return "O(n log n) ~ O(n^2) (조금 느림)"
    else:
        return "O(n^2) 이상 (느림)"


def format_memory(bytes_val: int) -> str:
    if bytes_val < 1024:
        return f"{bytes_val} B"
    elif bytes_val < 1024 * 1024:
        return f"{bytes_val / 1024:.2f} KB"
    else:
        return f"{bytes_val / (1024 * 1024):.2f} MB"


def run_test(i: int):
    """in{i}.txt로부터 입력을 받아 solution()을 실행하고, out{i}.txt와 비교"""
    # 표준 입력을 inX.txt로 변경
    sys.stdin = open(f"in{i}.txt", "r", encoding="utf-8")

    # 표준 출력 캡처
    output_capture = StringIO()
    original_print = builtins.print
    builtins.print = lambda *args, **kwargs: (
        output_capture.write(" ".join(map(str, args)) + "\n")
        if kwargs.get("file", None) is None or kwargs["file"] is sys.stdout
        else original_print(*args, **kwargs)
    )

    # 시간·메모리 측정 시작
    tracemalloc.start()
    start_time = time.perf_counter()

    try:
        solution()
    except Exception as e:
        builtins.print = original_print
        tracemalloc.stop()
        print(f"[TEST {i}] {Colors.RED}ERROR{Colors.ENDC} - {e}")
        return False, None, None, None, None

    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # 출력 복원
    builtins.print = original_print
    result = output_capture.getvalue().rstrip("\n")

    # 기대값 읽기
    with open(f"out{i}.txt", "r", encoding="utf-8") as f:
        expected = f.read().rstrip("\n")

    # 결과 비교
    passed = (result == expected)
    exec_time_ms = (end_time - start_time) * 1000

    return passed, exec_time_ms, peak_mem, result, expected


def print_test_report(i: int, passed: bool, exec_time_ms: float, peak_mem: int, user_output: str, expected_output: str):
    bar = "=" * 60
    print(f"\n{Colors.BOLD}{bar}{Colors.ENDC}")
    status = f"{Colors.GREEN}PASS{Colors.ENDC}" if passed else f"{Colors.RED}FAIL{Colors.ENDC}"
    print(f"[TEST {i}] {status}")

    if exec_time_ms is not None and peak_mem is not None:
        print(f"{Colors.CYAN}  ⏱ 실행 시간{Colors.ENDC}: {exec_time_ms:.3f} ms")
        print(f"{Colors.CYAN}  🧠 피크 메모리{Colors.ENDC}: {format_memory(peak_mem)}")
        print(f"{Colors.CYAN}  📈 추정 복잡도{Colors.ENDC}: {estimate_complexity(exec_time_ms)}")

    # 사용자 출력과 정답 표시
    print(f"{Colors.YELLOW}  ▶ 사용자 출력{Colors.ENDC}: {user_output}")
    print(f"{Colors.GREEN}  ▶ 정답      {Colors.ENDC}: {expected_output}")

    print(f"{Colors.BOLD}{bar}{Colors.ENDC}")


def main():
    print(f"{Colors.HEADER}{Colors.BOLD}=== 코딩테스트 로컬 채점기 v2.0 ==={Colors.ENDC}\n")

    total_pass = 0
    total_time = 0.0
    max_mem = 0

    if RUN_FLAG == 1:
        passed, t, m, user_output, expected_output = run_test(1)
        if passed is not None:
            print_test_report(1, passed, t, m, user_output, expected_output)
            if passed:
                total_pass += 1
            if t is not None:
                total_time += t
            if m is not None:
                max_mem = max(max_mem, m)
    else:
        for i in range(1, TOTAL_TEST + 1):
            print(f"Running TEST {i}...")
            passed, t, m, user_output, expected_output = run_test(i)
            if passed is not None:
                print_test_report(i, passed, t, m, user_output, expected_output)
                if passed:
                    total_pass += 1
                if t is not None:
                    total_time += t
                if m is not None:
                    max_mem = max(max_mem, m)

    # 요약 출력
    print("\n====== SUMMARY ======")
    if total_pass == TOTAL_TEST:
        print(f"{Colors.GREEN}ALL PASS!{Colors.ENDC}")
    else:
        print(f"{Colors.YELLOW}{total_pass}/{TOTAL_TEST} PASSED{Colors.ENDC}")

    print(f"총 실행 시간: {total_time:.3f} ms")
    print(f"최대 피크 메모리: {format_memory(max_mem)}")
    print("=====================")


if __name__ == "__main__":
    main()
