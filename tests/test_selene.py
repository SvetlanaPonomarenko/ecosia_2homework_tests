from selene import have
from selene.support.shared import browser


def test_complete_task():
    browser.open('http://todomvc.com/examples/emberjs/')

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    browser.element('#todo-list>li:nth-of-type(2) .toggle').click()
    browser.all('#todo-list>li[class~=completed]').should(have.exact_text('b'))
    browser.all('#todo-list>li[class=ember-view]').should(have.exact_texts('a', 'c'))


