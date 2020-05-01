class TestBase:

    @classmethod
    def setup_class(cls):
        print("Beforeeeeee!!!!!!!!!!")
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """

    @classmethod
    def teardown_class(cls):
        print("Afteeerrrrr!")
        """ teardown any state that was previously setup with a call to
        setup_class.
        """

    def setup_method(self, method):
        print("Do you see this before?")
        """ setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """

    def teardown_method(self, method):
        print("Do you see this after?")
        """ teardown any state that was previously setup with a setup_method
        call.
        """