import pytest


@pytest.fixture(scope="session", autouse=True)
def before_all(request):
    print("callattr_ahead_of_alltests called")
    seen = {None}
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        if cls not in seen:
            if hasattr(cls.obj, "callme"):
                cls.obj.callme()
            seen.add(cls)

def after_all(session, exitstatus):
    print("Finished!!!!!")