from tests import tests_helper, helpers

class TestExample(unittest.TestCase):

    def test_other_helper(self):
        assert tests_helper.list_has(3, [1, 2, 3])

    def test_pass(self):
        self.assertEqual(True, True)

    @pytest.mark.xfail
    def test_should_fail(self):
        self.assertEqual(False, True)
