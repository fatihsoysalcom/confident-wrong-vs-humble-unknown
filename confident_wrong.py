import sys

def process_request(request_data):
    """Simulates processing a request, potentially leading to confident error."""
    print(f"Processing request: {request_data}")

    # Simulate a scenario where we might be confidently wrong
    if "version" in request_data and request_data["version"] == "1.0":
        # In a real scenario, this might be a hardcoded assumption or a quick guess
        # that turns out to be incorrect later.
        print("Assuming legacy compatibility for version 1.0...")
        # Let's pretend this assumption leads to a subtle bug, but we're "sure" it's right.
        return {"status": "success", "message": "Processed legacy request.", "data": {"legacy_mode": True}}
    elif "version" in request_data and request_data["version"] == "2.0":
        print("Handling modern request for version 2.0.")
        return {"status": "success", "message": "Processed modern request.", "data": {"legacy_mode": False}}
    else:
        # This is the "I don't know" path, which is better.
        print("Unknown version. This is a good place to ask for clarification.")
        return {"status": "error", "message": "Unknown API version. Please specify '1.0' or '2.0'."}

def simulate_developer_behavior():
    """Demonstrates two developer approaches to an unknown."""
    print("--- Scenario 1: Confidently Wrong Developer ---")
    # Developer makes an assumption without verifying, acting as if they know.
    # They might have seen version '1.0' once and assume all older versions are handled the same.
    confidently_wrong_request = {"command": "get_data", "version": "1.0"}
    response_wrong = process_request(confidently_wrong_request)
    print(f"Response (Confidently Wrong): {response_wrong}\n")

    print("--- Scenario 2: Humble Unknown Developer ---")
    # Developer encounters an unknown and admits it, seeking correct information.
    # This leads to a more accurate outcome or a clear path to resolution.
    humble_unknown_request = {"command": "get_data", "version": "unknown"}
    response_unknown = process_request(humble_unknown_request)
    print(f"Response (Humble Unknown): {response_unknown}\n")

    print("--- Scenario 3: Modern Request ---")
    modern_request = {"command": "get_data", "version": "2.0"}
    response_modern = process_request(modern_request)
    print(f"Response (Modern): {response_modern}\n")

if __name__ == "__main__":
    simulate_developer_behavior()
