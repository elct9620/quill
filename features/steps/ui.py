from behave import then


@then('按鈕 "{button_id}" 顯示為 "{label}"')
def step_check_button_label(context, button_id, label):
    assert getattr(context.window.ui, button_id).text() == label
