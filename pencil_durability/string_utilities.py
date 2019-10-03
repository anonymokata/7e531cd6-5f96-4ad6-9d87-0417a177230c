def reverse_string(original):
    return original[::-1]


def reverse_string_replace(original, old, new, count=...):
    original_reversed = reverse_string(original)
    new_reversed = reverse_string(new)
    old_reversed = reverse_string(old)
    return reverse_string(original_reversed.replace(old_reversed, new_reversed, count))