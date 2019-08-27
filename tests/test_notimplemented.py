def test_a_not_implemented_feature(testdir):
    testdir.makepyfile(
        """
        from pytest import mark

        @mark.notimplemented
        def test_not_implemented():
            assert False
    """
    )

    result = testdir.runpytest()

    result.assert_outcomes(xfailed=1)


def test_a_not_implemented_feature_with_an_implemented_one(testdir):
    testdir.makepyfile(
        """
        from pytest import mark

        @mark.notimplemented
        def test_not_implemented():
            assert False

        def test_implemented():
            assert True
    """
    )

    result = testdir.runpytest()

    result.assert_outcomes(xfailed=1, passed=1)
