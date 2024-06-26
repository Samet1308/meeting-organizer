def find_max(t, z):
    # Verilen bir dizenin tüm alt dizelerini üretir
    def generate_substrings(s):
        substr = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr.append(s[i:j])
        return substr

    # Bir alt dizenin bir dizede kaç kez meydana geldiğini sayan fonksiyon
    def count_occurrences(sub, s):
        count = 0
        pos = s.find(sub)
        while pos != -1:
            count += 1
            pos = s.find(sub, pos + 1)
        return count

    # t'nin tüm alt dizelerini üretir
    substrings = generate_substrings(t)
    
    # Maksimum değeri ve karşılık gelen alt dizeyi başlatır
    max_value = 0
    max_substring = ""
    
    # Tüm alt dizeler üzerinde dolaş
    for sub in substrings:
        count = count_occurrences(sub, z)
        value = len(sub) * count
        if value > max_value:
            max_value = value
            max_substring = sub
    
    return max_substring, max_value

if __name__ == '__main__':
    t = "acldm1labcdhsnd"
    z = "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"
    substring, max_value = find_max(t, z)
    print(f"{substring} is a substring of t, and it occurs {max_value // len(substring)} times in Z, len({substring}) x {max_value // len(substring)} = {max_value} is the solution")

