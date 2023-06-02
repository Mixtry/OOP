class AutomaticTranslator:
    def __init__(self, NLang, vocabulary, form):
        self.NLang = NLang
        self.vocabulary = vocabulary
        self.form = form

    def __lt__(self, other):
        return self.vocabulary < other.vocabulary or (self.vocabulary == other.vocabulary and self.NLang < other.NLang) or  (self.vocabulary == other.vocabulary and self.NLang == other.NLang and self.form < other.form)

    def __le__(self, other):
        return self.vocabulary <= other.vocabulary or (self.vocabulary == other.vocabulary and self.NLang <= other.NLang) or (self.vocabulary == other.vocabulary and self.NLang == other.NLang and self.form <= other.form)

    def __eq__(self, other):
        return self.NLang == other.NLang and self.vocabulary == other.vocabulary and self.form == other.form

    def __sub__(self, other):
        NLang = min(self.NLang, other.NLang)
        vocabulary = (self.vocabulary + other.vocabulary) // 2
        form = min(self.form, other.form)
        return AutomaticTranslator(NLang, vocabulary, form)

    def __iadd__(self, other):
        self.NLang += other[0]
        self.vocabulary += other[1]
        return self

    def __truediv__(self, other):
        return [AutomaticTranslator(self.NLang // other, self.vocabulary // other, self.form) for _ in range(other)]

    def __ge__(self, other):
        return self.vocabulary >= other.vocabulary or (self.vocabulary == other.vocabulary and self.NLang >= other.NLang) or (self.vocabulary == other.vocabulary and self.NLang == other.NLang and self.form >= other.form)

    def __gt__(self, other):
        return self.vocabulary > other.vocabulary or (self.vocabulary == other.vocabulary and self.NLang > other.NLang) or (self.vocabulary == other.vocabulary and self.NLang == other.NLang and self.form > other.form)

    def __str__(self):
        return f"Translator in the form of {self.form} from {self.NLang} languages, {self.vocabulary} words."

    def __repr__(self):
        return f"AutomaticTranslator({self.NLang}, {self.vocabulary}, '{self.form}')"

    def __call__(self):
        return (self.vocabulary + len(self.form)) // self.NLang

    def add_language(self, nums):
        self.NLang += 1
        self.vocabulary += nums


at = AutomaticTranslator(12, 5432, "box")
at1 = AutomaticTranslator(3, 15, "hat")
print(at <= at1, at == at1, at > at1)
print(at, at1, sep="n")
print()
res = at / 4
res[0] += (2, 187)
print(res, at(), at1(), sep="n")
