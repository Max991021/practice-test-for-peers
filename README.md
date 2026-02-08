# Python Apprentice Assessment (Linux)

This assessment evaluates fundamental Python proficiency, including control flow, data structures, and command-line familiarity on Linux systems.

## Resources
- **Python Documentation**: [https://docs.python.org/3/]

## Setup Instructions

1.  **Initialize the Environment**
    ```bash
    python3 -m venv venv
    ```
2.  **Activate the Virtual Environment**
    ```bash
    source venv/bin/activate
    ```
3.  **Install Dependencies**
    ```bash
    pip install pytest
    ```

## How to run your tests

**To run all your tests**
```bash
python3 -m pytest test_exam.py -v
```
**To run your tests individually**
```bash
python3 -m pytest test_exam.py::TestSectionA::test_q1_shipping -v
```

## Assessment Sections

    Section A: Coding Challenges (exam.py) Complete the 5 function implementations in exam.py.

    Section B: Multiple Choice and Section C: Command Line (Google Form): [https://forms.gle/CU5GsmQaW8J5LAP78]