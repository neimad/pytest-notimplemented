def test_a_not_written_test(testdir):
    testdir.makepyfile(
        """
        from pytest import mark

        @mark.notwritten
        def test_not_written():
            assert False
    """
    )

    result = testdir.runpytest()

    result.assert_outcomes(skipped=1)


def test_a_not_written_test_with_an_written_one(testdir):
    testdir.makepyfile(
        """
        from pytest import mark

        @mark.notwritten
        def test_not_written():
            assert False

        def test_written():
            assert True
    """
    )

    result = testdir.runpytest()

    result.assert_outcomes(skipped=1, passed=1)
