import src.identifier.identifier as identifier
class Testclass:
    def test_identifier1(self):
        assert identifier.identifier("Ab56") == False
    def test_identifier2(self):
        assert identifier.identifier("aaaaaa") == False
    def test_identifier3(self):
        assert identifier.identifier("9586959496") == True
    def test_identifier4(self):
        assert identifier.identifier("#/*") == False
    def test_identifier5(self):
        assert identifier.identifier("a026456") == True
    def test_identifier6(self):
        assert identifier.identifier("") == False