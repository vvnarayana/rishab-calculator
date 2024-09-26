from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import traceback
import math
import os

# Open the Flask app URL
app_url = 'https://circleci.azurewebsites.net/'
print("Navigating to:", app_url)

options = webdriver.ChromeOptions()
options.add_argument('enable-automation')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")
options.add_argument("--dns-prefetch-disable")
options.add_argument("--disable-gpu")
options.add_argument('--remote-debugging-pipe')
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options=options)
driver.get(app_url)

passed_tests = 0
total_tests = 0
output_lines = []

try:
    test_cases = [
        ("5", "3", "Add", 8),
        ("-5", "3", "Add", -2),
        ("2.5", "1.5", "Add", 4.0),
        ("8", "3", "Subtract", 5),
        ("3", "8", "Subtract", -5),
        ("10", "10", "Subtract", 0),
        ("5", "4", "Multiply", 20),
        ("7", "0", "Multiply", 0),
        ("2.5", "1.5", "Multiply", 3.75),
        ("10", "2", "Divide", 5.0),
        ("8", "0", "Divide", "Cannot divide by zero"),
        ("7", "3", "Divide", 2.33),
    ]

    for test_case in test_cases:
        wait = WebDriverWait(driver, 15)

        num_one_input = wait.until(EC.presence_of_element_located((By.NAME, "number_one")))
        num_two_input = wait.until(EC.presence_of_element_located((By.NAME, "number_two")))
        input_type = wait.until(EC.presence_of_element_located((By.NAME, "operation")))

        num_one_input.clear()
        num_two_input.clear()

        num_one_input.send_keys(test_case[0])
        num_two_input.send_keys(test_case[1])

        operation_select = Select(input_type)
        operation_select.select_by_value(test_case[2].lower())

        calc_button = driver.find_element(By.ID, "calculate_btn")
        calc_button.click()

        result_element = wait.until(EC.visibility_of_element_located((By.ID, "result")))

        actual_result = result_element.text.strip()
        actual_result_numeric = actual_result.split(": ")[-1]

        # Handling the floating-point comparison separately
        if isinstance(test_case[3], float) or isinstance(test_case[3], int):
            if actual_result_numeric == "Cannot divide by zero":
                expected_result = actual_result_numeric
            else:
                expected_result = float(actual_result_numeric)

            tolerance = 0.01  # Adjust tolerance for rounding
            if math.isclose(expected_result, float(test_case[3]), rel_tol=tolerance):
                result_line = f"Test passed for {test_case[:3]}. Expected: {float(test_case[3])}, Actual: {expected_result}"
                passed_tests += 1
            else:
                result_line = f"Test failed for {test_case[:3]}. Expected: {float(test_case[3])}, Actual: {expected_result}"
        else:
            if actual_result_numeric == test_case[3] or actual_result_numeric == "Cannot divide by zero":
                result_line = f"Test passed for {test_case[:3]}. Expected: {test_case[3]}, Actual: {actual_result_numeric}"
                passed_tests += 1
            else:
                result_line = f"Test failed for {test_case[:3]}. Expected: {test_case[3]}, Actual: {actual_result_numeric}"

        print(result_line)
        output_lines.append(result_line)
        total_tests += 1

except TimeoutException as e:
    error_line = f"Timeout occurred while waiting for the element. Details: {e}"
    print(error_line)
    output_lines.append(error_line)
    traceback.print_exc()

finally:
    # Close the browser session
    driver.quit()

summary_line = f"{passed_tests}/{total_tests} test cases passed."
print(summary_line)
output_lines.append(summary_line)

# Write the results to a file
with open("test_results.txt", "w") as f:
    for line in output_lines:
        f.write(line + "\n")
