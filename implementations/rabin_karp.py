# Constants used across functions
BASE = 256

def main():
    text = input("Please enter the text: ")
    pattern = input("Please enter your search pattern: ")
    
    try:
        prime = int(input("Please enter the prime number: "))
        #Adjust the value to the length of your text
    except ValueError:
        print("Please enter a valid integer for the prime.")
        return

    m = len(text)
    n = len(pattern)

    # Initial hashes using your specific logic
    hash_text = first_hash(text, n, prime)
    hash_pattern = first_hash(pattern, n, prime)

    matches = rolling_hash_search(text, pattern, m, n, hash_text, hash_pattern, prime)

    if matches > 0:
        print(f"Pattern is found a total of {matches} time(s).")
    else:
        print("Pattern is not found.")


def first_hash(string, length, prime):
    current_hash = 0
    for i in range(length):
        c = ord(string[i])
        # Use formula from the post
        current_hash += c * (BASE ** (length - i - 1))
    return current_hash % prime


def rolling_hash_search(text, pattern, m, n, hash_text, hash_pattern, prime):
    match_count = 0
    # Pre-calculate (256**(n-1)) to use in the rolling formula
    h_multiplier = pow(BASE, n - 1, prime)
    #pow is a built-in function for Modular Exponentiation
    #pow is the same as (BASE**(n-1)) % prime
    #We do mod already here to keep the number small and calculations fast
    
    for i in range(m - n + 1):
        # Check for a match
        if hash_text == hash_pattern:
            # Double-check the match
            if text[i : i + n] == pattern:
                match_count += 1
                print(f"Pattern is found at position: {i}")

        # Calculate hash for the next window (if we aren't at the end)
        if i < m - n:
            c_old = ord(text[i])
            c_new = ord(text[i + n])
            
            # Build new hash
            hash_text = (BASE * (hash_text - c_old * h_multiplier) + c_new) % prime
            
            # Ensure the hash isn't negative
            if hash_text < 0:
                hash_text += prime
                
    return match_count

if __name__ == "__main__":
    main()
