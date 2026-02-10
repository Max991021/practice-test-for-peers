import pytest
from exam import (
    calculate_shipping_cost,
    filter_even_numbers,
    generate_multiplication_table,
    find_longest_word,
    fizz_buzz_custom
)

class TestSectionA:
    """
    Scoring Logic: Each test function represents 20% of Section A.
    Run with: python3 -m pytest test_exam.py
    """

    def test_q1_shipping(self):
        """Test Question 1: Shipping Logic (20%)"""
        assert calculate_shipping_cost(2, 'domestic') == 8.0
        assert calculate_shipping_cost(2, 'international') == 25.0
        assert calculate_shipping_cost(0, 'domestic') == 0.0

    def test_q2_filter_evens(self):
        """Test Question 2: List Filtering (20%)"""
        assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
        assert filter_even_numbers([1, 3, 5]) == []
        assert filter_even_numbers([]) == []

    def test_q3_multiplication(self):
        """Test Question 3: Multiplication Table (20%)"""
        expected = ["3 * 1 = 3", "3 * 2 = 6"]
        assert generate_multiplication_table(3, 2) == expected
        assert generate_multiplication_table(5, 0) == []

    def test_q4_longest_word(self):
        """Test Question 4: Word Search (20%)"""
        assert find_longest_word("The quick brown fox") == "quick"
        assert find_longest_word("Python is fun") == "Python"
        assert find_longest_word("") == ""

    def test_q5_fizz_buzz(self):
        """Test Question 5: FizzBuzz Logic (20%)"""
        result = fizz_buzz_custom(1, 3, 2, 3)
        assert result == ["1", "Fizz", "Buzz"]
        result_both = fizz_buzz_custom(6, 6, 2, 3)
        assert result_both == ["FizzBuzz"]


@pytest.fixture(scope="session", autouse=True)
def summary_score(request):
    """
    Hook to calculate and print the final percentage after all tests run.
    """
    yield
    terminal_reporter = request.config.pluginmanager.get_plugin("terminalreporter")
    passed = len(terminal_reporter.stats.get("passed", []))
    total = terminal_reporter.stats.get("passed", []) + terminal_reporter.stats.get("failed", [])
    total_count = len(total)
    
    score = (passed / total_count) * 100 if total_count > 0 else 0
    
    print("\n" + "="*30)
    print(f"SECTION A SCORE: {score:.0f}%")
    print("="*30)
    
    
    
