class reverseex:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

print(reverseex().reverse_words('helllo keval'))

