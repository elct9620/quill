from behave import when, then


@when("使用者點選 {}")
def step_click(context, label):
    raise NotImplementedError("STEP: When 使用者點選 {}")


@then("可以看到 {} 的訊息")
def step_see_text(context, message):
    raise NotImplementedError("STEP: Then 可以看到 {} 的訊息")
