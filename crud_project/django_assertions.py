from django.test import TestCase

_test_case = TestCase()
assert_contains = _test_case.assertContains  # verifica se existe o conteúdo
assert_not_contains = _test_case.assertNotContains  # verifica se não existe o conteúdo
