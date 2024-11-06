# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

> [!NOTE]  
> The main template and also other partial html files listed below were tested as part of the main site files as they include them.
> - base.html
> - clockface.html
> - messages.html
> - pagination.html
> - standard_nav.html

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| templates | 404.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_404.png "watch-o-tron html validation 404") | no errors or warnings |
| templates/account | login.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_login.png "watch-o-tron html validation login") | no errors or warnings |
| templates/account | logout.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_logout.png "watch-o-tron html validation logout") | no errors or warnings |
| templates/account | signup.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_signup.png "watch-o-tron html validation signup") | no errors or warnings |
| watches/templates/watches | index.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_index.png "watch-o-tron html validation index") | |
| watches/templates/watches | manage_watch.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_manage_watch.png "watch-o-tron html validation manage_watch") | no errors or warnings |
| watches/templates/watches | staff_settings.html | ![screenshot](documentation/testing/validation/html/wot_testing_html_staff_settings.png "watch-o-tron html validation staff_settings") | no errors or warnings |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | clockface.css | ![screenshot](documentation/testing/validation/css/wot_testing_css_clockface.png "watch-o-tron css validation clockface") | no errors found |
| static | style.css | ![screenshot](documentation/testing/validation/css/wot_testing_css_style.png "watch-o-tron css validation style") | no errors found |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | base_script.js | ![screenshot](documentation/testing/validation/js/wot_testing_js_base_script.png "watch-o-tron js validation base script") | bootstrap varable picked up as undefined and bootstrap variable tooltips marked as unused |
| static | edit_watch_script.js | ![screenshot](documentation/testing/validation/js/wot_testing_js_edit_watch_script.png "watch-o-tron js validation edit watch script") | bootstrap varable picked up as undefined |
| static | staff_settings_script.js | ![screenshot](documentation/testing/validation/js/wot_testing_js_staff_settings_script.png "watch-o-tron js validation staff settings script") | bootstrap varable picked up as undefined |
| static | watch_script.js | ![screenshot](documentation/testing/validation/js/wot_testing_js_watch_script.png "watch-o-tron js validation watch script") | bootstrap varable picked up as undefined |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/manage.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_manage.png "watch-o-tron py validation manage") | all clear, no errors found |
| watches | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watches/admin.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_admin.png "watch-o-tron py validation admin") | all clear, no errors found |
| watches | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watches/forms.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_forms.png "watch-o-tron py validation forms") | all clear, no errors found |
| watches | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watches/models.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_models.png "watch-o-tron py validation models") | all clear, no errors found |
| watches | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watches/urls.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_watches_urls.png "watch-o-tron py validation watches urls") | all clear, no errors found |
| watches | moons.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watches/utils/moons.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_moons.png "watch-o-tron py validation moons") | all clear, no errors found |
| watches | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watches/views.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_views.png "watch-o-tron py validation views") | all clear, no errors found |
| watchotron | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watchotron/settings.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py_settings.png "watch-o-tron py validation settings") | added # noqa to lines 141, 144, 147 and 150 to ignore Django's long lines then all clear, no errors found |
| watchotron | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p4_watch-o-tron/main/watchotron/urls.py) | ![screenshot](documentation/testing/validation/py/wot_testing_py__watch-o-tron_urls.png "watch-o-tron py validation watch-o-tron urls") | all clear, no errors found |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Login | Logout | Signup | Home | Add/Edit Watch | Staff Settings | 404 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_login.png "watch-o-tron chrome login") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_logout.png "watch-o-tron chrome logout") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_signup.png "watch-o-tron chrome signup") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_home.png "watch-o-tron chrome home") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_add_edit.png "watch-o-tron chrome add edit") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_staff_settings.png "watch-o-tron chrome staff settings") | ![screenshot](documentation/testing/browsers/chrome/wot_testing_browsers_chrome_404.png "watch-o-tron chrome 404") | works as expected |
| Firefox | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_login.png "watch-o-tron firefox login") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_logout.png "watch-o-tron chrome logout") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_signup.png "watch-o-tron firefox signup") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_home.png "watch-o-tron firefox home") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_add_edit.png "watch-o-tron firefox add edit") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_staff_settings.png "watch-o-tron firefox staff settings") | ![screenshot](documentation/testing/browsers/firefox/wot_testing_browsers_firefox_404.png "watch-o-tron firefox 404") | works as expected |
| Edge | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_login.png "watch-o-tron edge login") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_logout.png "watch-o-tron edge logout") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_signup.png "watch-o-tron edge signup") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_home.png "watch-o-tron edge home") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_add_edit.png "watch-o-tron edge add edit") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_staff_settings.png "watch-o-tron edge staff settings") | ![screenshot](documentation/testing/browsers/edge/wot_testing_browsers_edge_404.png "watch-o-tron edge 404") | works as expected |
| Safari | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_login.png "watch-o-tron safari login") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_logout.png "watch-o-tron safari logout") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_signup.png "watch-o-tron safari signup") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_home.png "watch-o-tron safari home") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_add_edit.png "watch-o-tron safari add edit") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_staff_settings.png "watch-o-tron safari staff settings") | ![screenshot](documentation/testing/browsers/safari/wot_testing_browsers_safari_404.png "watch-o-tron safari 404") | works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Login | Logout | Signup | Home | Home with expanded menu | Add/Edit Watch | Staff Settings | 404 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (devtools) | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_login.png "watch-o-tron responsive mobile dev login") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_logout.png "watch-o-tron responsive mobile dev logout") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_signup.png "watch-o-tron responsive mobile dev signup") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_home.png "watch-o-tron responsive mobile dev home") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_home_menu.png "watch-o-tron responsive mobile dev home menu") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_add_edit.png "watch-o-tron responsive mobile dev add edit") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_staff_settings.png "watch-o-tron responsive mobile dev staff settings") | ![screenshot](documentation/testing/responsive/mobile_devtools/wot_testing_resposive_mobile_dev_404.png "watch-o-tron responsive mobile dev 404") | tooltips only show on tap with mobile device |
| Tablet (devtools) | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_login.png "watch-o-tron responsive tablet dev login") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_logout.png "watch-o-tron responsive tablet dev logout") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_signup.png "watch-o-tron responsive tablet dev signup") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_home.png "watch-o-tron responsive tablet dev home") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_home_menu.png "watch-o-tron responsive tablet dev home menu") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_add_edit.png "watch-o-tron responsive tablet dev add edit") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_staff_settings.png "watch-o-tron responsive tablet dev staff settings") | ![screenshot](documentation/testing/responsive/tablet_devtools/wot_testing_resposive_tablet_dev_404.png "watch-o-tron responsive tablet dev 404") | tooltips only show on tap with tablet device |
| Desktop (devtools) | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_login.png "watch-o-tron responsive desktop dev login") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_logout.png "watch-o-tron responsive desktop dev logout") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_signup.png "watch-o-tron responsive desktop dev signup") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_home.png "watch-o-tron responsive desktop dev home") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_home_menu.png "watch-o-tron responsive desktop dev home menu") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_add_edit.png "watch-o-tron responsive desktop dev add edit") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_staff_settings.png "watch-o-tron responsive desktop dev staff settings") | ![screenshot](documentation/testing/responsive/desktop_devtools/wot_testing_resposive_desktop_dev_404.png "watch-o-tron responsive desktop dev 404") | works as expected |
| 4k Screen (devtools) | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_login.png "watch-o-tron responsive 4k dev login") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_logout.png "watch-o-tron responsive 4k dev logout") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_signup.png "watch-o-tron responsive 4k dev signup") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_home.png "watch-o-tron responsive 4k dev home") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_home_menu.png "watch-o-tron responsive 4k dev home menu") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_add_edit.png "watch-o-tron responsive 4k dev add edit") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_staff_settings.png "watch-o-tron responsive 4k dev staff settings") | ![screenshot](documentation/testing/responsive/4k_devtools/wot_testing_resposive_4k_dev_404.png "watch-o-tron responsive 4k dev 404") | works as expected things starting to look a little small |
| iPhone 16 Pro | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_login.PNG "watch-o-tron responsive iphone 16 pro login") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_logout.PNG "watch-o-tron responsive iphone 16 pro logout") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_signup.PNG "watch-o-tron responsive iphone 16 pro signup") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_home.PNG "watch-o-tron responsive iphone 16 pro home") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_home_menu.PNG "watch-o-tron responsive iphone 16 pro home menu") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_add_edit.PNG "watch-o-tron responsive iphone 16 pro add edit") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_staff_settings.PNG "watch-o-tron responsive iphone 16 pro staff settings") | ![screenshot](documentation/testing/responsive/iphone/wot_testing_resposive_iphone_404.PNG "watch-o-tron responsive iphone 16 pro 404") | works as expected |
| iPad Mini | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_login.PNG "watch-o-tron responsive ipad mini login") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_logout.PNG "watch-o-tron responsive ipad mini logout") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_signup.PNG "watch-o-tron responsive ipad mini signup") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_home.PNG "watch-o-tron responsive ipad mini home") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_home_menu.PNG "watch-o-tron responsive ipad mini home menu") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_add_edit.PNG "watch-o-tron responsive ipad mini add edit") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_staff_settings.PNG "watch-o-tron responsive ipad mini staff settings") | ![screenshot](documentation/testing/responsive/ipadmini/wot_testing_resposive_ipad_mini_404.PNG "watch-o-tron responsive ipad mini 404") | works as expected |
| Samsung Galaxy Tab 6 Lite | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_login.jpg "watch-o-tron responsive galaxy tab login") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_logout.jpg "watch-o-tron responsive galaxy tab logout") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_signup.jpg "watch-o-tron responsive galaxy tab signup") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_home.jpg "watch-o-tron responsive galaxy tab home") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_home_menu.jpg "watch-o-tron responsive galaxy tab home menu") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_add_edit.jpg "watch-o-tron responsive galaxy tab add edit") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_staff_settings.jpg "watch-o-tron responsive galaxy tab staff settings") | ![screenshot](documentation/testing/responsive/galaxytab/wot_testing_resposive_galaxytab_404.jpg "watch-o-tron responsive galaxy tab 404") | works as expected |
| Macbook Air M3 | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_login.png "watch-o-tron responsive macbook login") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_logout.png "watch-o-tron responsive macbook logout") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_signup.png "watch-o-tron responsive macbook signup") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_home.png "watch-o-tron responsive macbook home") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_home_menu.png "watch-o-tron responsive macbook home menu") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_add_edit.png "watch-o-tron responsive macbook add edit") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_staff_settings.png "watch-o-tron responsive macbook staff settings") | ![screenshot](documentation/testing/responsive/macbook/wot_testing_resposive_macbook_404.png "watch-o-tron responsive macbook 404") | works as expected |
| 2K Monitor | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_login.png "watch-o-tron responsive 2k monitor login") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_logout.png "watch-o-tron responsive 2k monitor logout") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_signup.png "watch-o-tron responsive 2k monitor signup") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_home.png "watch-o-tron responsive 2k monitor home") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_home_menu.png "watch-o-tron responsive 2k monitor home menu") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_add_edit.png "watch-o-tron responsive 2k monitor add edit") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_staff_settings.png "watch-o-tron responsive 2k monitor staff settings") | ![screenshot](documentation/testing/responsive/2k_monitor/wot_testing_resposive_2k_404.png "watch-o-tron responsive 2k monitor 404") | works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Login | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_login.png "watch-o-tron lighthouse mobile login") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_login.png "watch-o-tron lighthouse desktop login") | Some minor warnings |
| Signup | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_signup.png "watch-o-tron lighthouse mobile signup") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_signup.png "watch-o-tron lighthouse desktop signup") | Some minor warnings |
| Home | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_home.png "watch-o-tron lighthouse mobile home") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_home.png "watch-o-tron lighthouse desktop home") | Slightly slower response time on mobile loading images |
| Add/Edit | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_add_edit.png "watch-o-tron lighthouse mobile add edit") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_add_edit.png "watch-o-tron lighthouse desktop add edit") | Slightly slower performance on mobile caused by render blocking resources |
| Staff Settings | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_staff_settings.png "watch-o-tron lighthouse mobile staff settings") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_staff_settings.png "watch-o-tron lighthouse desktop staff settings") | Some minor warnings |
| Logout | ![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_logout.png "watch-o-tron lighthouse mobile logout") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_logout.png "watch-o-tron lighthouse desktop logout") | Some minor warnings |
| 404 |![screenshot](documentation/testing/lighthouse/mobile/wot_testing_lighthouse_mobile_404.png "watch-o-tron lighthouse mobile 404") | ![screenshot](documentation/testing/lighthouse/desktop/wot_testing_lighthouse_desktop_404.png "watch-o-tron lighthouse desktop 404") | Status code: 404 which is good for the 404 page plus some minor warnings |

## Defensive Programming

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Defensive programming was manually tested with the below user acceptance testing:

### Creating a new user account

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Login | | | | | |
| | New user clicks on sign up link and is taken to the sign up page | Tested by clicking on the signup link on the login page | SUCCESS - user is taken to signup page | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_link.gif "watch-o-tron testing signup link") |
| Signup | | | | | |
| | New user clicks signup without entering any info and is informed of required fields. | Clicking on the signup button without entering data. | SUCCESS - user is informed that the form is not complete | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_no_info.gif "watch-o-tron testing signup process") |
| | New user clicks signup after entering just a username and is informed of required fields. | Clicking on the signup button with just a username entered. | SUCCESS - user is informed that the form is not complete | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_just_username.gif "watch-o-tron testing signup process") |
| | New user clicks signup after entering just a password and is informed of required fields. | Clicking on the signup button with just a password entered. | SUCCESS - user is informed that the form is not complete | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_just_password.gif "watch-o-tron testing signup process") |
| | New user clicks signup after entering an invalid username and is informed of this. | Clicking on the signup button with an invalid username. | SUCCESS - user is informed that the form is not valid | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_invalid_name.gif "watch-o-tron testing signup process") |
| | New user clicks signup after entering an invalid password and is informed of this. | Clicking on the signup button with an invalid password. | SUCCESS - user is informed that the form is not valid | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_invalid_password.gif "watch-o-tron testing signup process") |
| | New user clicks signup after entering mismatching passwords and is informed of this. | Clicking on the signup button with mismatched passwords. | SUCCESS - user is informed that the form is not valid | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_mismatched_passwords.gif "watch-o-tron testing signup process") |
| | New user clicks signup after entering valid username and password. They are then logged in and taken to the homepage  | Clicking on the signup button with valid info. | SUCCESS - user is created and logged in | n/a | ![screenrecording](documentation/testing/manual_testing/signup/wot_testing_manual_signup_success.gif "watch-o-tron testing signup process") |

### Logging in

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Login | | | | | |
| | User clicks on sign in without entering username or password and is informed of required fields. | Clicking on sign in without entering username or password. | SUCCESS - user is informed that the form is not complete. | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_no_input.gif "watch-o-tron testing login process") |
| | User clicks on sign in without entering password and is informed of required fields. | Clicking on sign in without entering password. | SUCCESS - user is informed that the form is not complete. | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_no_password.gif "watch-o-tron testing login process") |
| | User clicks on sign in without entering username and is informed of required fields. | Clicking on sign in without entering username. | SUCCESS - user is informed that the form is not complete. | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_no_username.gif "watch-o-tron testing login process") |
| | User clicks on sign in with invalid username or password and is informed of invalid input. | Clicking on sign in with invalid username or password. | SUCCESS - user is informed that the form is not valid. | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_invalid.gif "watch-o-tron testing login process") |
| | User clicks on sign in with valid username an password and is taken to homepage. | Clicking on sign in with valid username and password. | SUCCESS - user is logged in and taken to homepage. | n/a | ![screenrecording](documentation/testing/manual_testing/login/wot_testing_manual_login_success.gif "watch-o-tron testing login process") |


## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I can sign up for an account so that I can log in and use the app. | ![screeshot](documentation/features/accounts/wot_feature_accounts_sign_up.png "watch-o-tron user story signup") |
| As a site user, I can log in so that I can use the app. | ![screeshot](documentation/features/accounts/wot_feature_accounts_sign_in.png "watch-o-tron user story login") |
| As a site user, I can log out so that I can keep my data private. | ![screeshot](documentation/features/accounts/wot_feature_accounts_sign_out.png "watch-o-tron user story logout") |
| As a site user, I am notified on successful login and logout so that I know that I am logged in or out. | ![screeshot](documentation/features/messaging/wot_feature_comms_message_sign_in.png "watch-o-tron user story login message") ![screeshot](documentation/features/messaging/wot_feature_comms_message_sign_out.png "watch-o-tron user story logout message") |
| As a site user, I can view my watch collection so that I can view images and details of the watches I own. | ![screeshot](documentation/features/viewing/wot_feature_viewing_desktop.png "watch-o-tron user story home") |
| As a site user, I can view my wish list so that I can see what watches I want or plan my next purchase. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_wish_list.png "watch-o-tron user story wish list") |
| As a site user, I can view watches that I have placed in potentially added new list types so that I can see the watch details for this list. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_other_lists.png "watch-o-tron user story custom lists") |
| As a site user, I can see the details of each watch so that I can find out more information about them. | ![screeshot](documentation/features/viewing/wot_feature_viewing_card_image.png "watch-o-tron user story watch details") |
| As a site user, I am notified when I have switched views to a new list so that I know which list I am viewing. | ![screeshot](documentation/features/messaging/wot_feature_comms_message_switching_page_1.png "watch-o-tron user story switched view message") ![screeshot](documentation/features/messaging/wot_feature_comms_message_switching.png "watch-o-tron user story switched view message") |
| As a site user, I can add a new watch so that I ca see it in my collection or wish list. | ![screeshot](documentation/features/addwatch/wot_feature_add_watch_desktop.png "watch-o-tron user story add watch") |
| As a site user, I am asked to confirm new watch details I entered are correct so that no accidental erroneous data is saved. | ![screeshot](documentation/features/addwatch/wot_feature_add_watch_desktop_confirm.png "watch-o-tron user story add watch confirm") |
| As a site user, I am notified when a watch has been added successfully so that I know the addition was successful or not. | ![screeshot](documentation/features/messaging/wot_feature_comms_message_confirm_add_watch.png "watch-o-tron user story add watch message") |
| As a site user, I can see a spinner when I click add watch so that I know something is happening. | ![screeshot](documentation/features/messaging/wot_feature_spinner.png "watch-o-tron user story spinner") |
| As a site user, I should be prompted to confirm watch deletions so that I do not delete watches by accident. | ![screeshot](documentation/features/delete/wot_feature_delete_desktop.png "watch-o-tron user story delete confirm") |
| As a site user, I can edit stored watches in my collection so that I can add more detail or update existing information. | ![screeshot](documentation/features/editing/wot_feature_editing_desktop.png "watch-o-tron user story watch edit") |
| As a site user, I can move a watch in my wish list to my collection so that I know that I have purchased it. | ![screeshot](documentation/features/purchased/wot_feature_purchased_desktop_confirm.png "watch-o-tron user story watch purchase") |
| As a site user, I can delete a watch from the wish list so that I can update my wish list should I no longer want a particular watch. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_delete_wish_list.png "watch-o-tron user story delete from wish list") |
| As a site user, I can delete a watch from a new list type so that I can update this list when I no longer want the watch to appear in it. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_delete_other_list.png "watch-o-tron user story delete from other list") |
| As a site user, I can edit stored watches in my wish list so that I can add more detail or update existing information. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_edit_wish_list.png "watch-o-tron user story edit in wish list") |
| As a site user, I can edit stored watches in a new list type so that I can add more detail or update existing information. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_edit_other_list.png "watch-o-tron user story edit in other list") |
| As a site user, I can delete a watch from my collection so that I can update my lists if I no longer own a particular watch. | ![screeshot](documentation/features/delete/wot_feature_delete_desktop.png "watch-o-tron user story delete watch") |
| As a site user, I should be prompted to confirm alterations so that edits are correct. | ![screeshot](documentation/features/editing/wot_feature_edit_confirm_desktop.png "watch-o-tron user story edit confirm") |
| As a site user, I should be asked to confirm when I set a watch as purchased so that I don't accidentally move a watch to my collection if I haven't bought it. | ![screeshot](documentation/features/purchased/wot_feature_purchased_desktop_confirm.png "watch-o-tron user story watch purchase") |
| As a site user, I am notified after editing and deleting watches so that I know if the process was successful. | ![screeshot](documentation/features/messaging/wot_feature_comms_message_confirm_edit_watch.png "watch-o-tron user story edit message") ![screeshot](documentation/features/messaging/wot_feature_comms_message_confirm_delete_watch.png "watch-o-tron user story delete message") |
| As a site user, I am notified when I move a watch to the collection so that it is confirmed whether the process was successful. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_message_moved_to_collection.png "watch-o-tron user story move to collection") |
| As a site user, I can see a spinner when I confirm a watch edit so that I know something is happening. | ![screeshot](documentation/features/messaging/wot_feature_spinner.png "watch-o-tron user story spinner") |
| As a curious site user, I can discover a hidden Easter egg in the site logo so that I experience an unexpected, delightful surprise within the application. | ![screeshot](documentation/features/logo/wot_feature_logo.png "watch-o-tron user story site logo") |
| As a curious site user, I can discover a hidden Easter egg in the date complication icon so that I experience an unexpected, delightful surprise within the application. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_ee_date.png "watch-o-tron user story date easter egg") |
| As a curious site user, I can discover a hidden Easter egg in the day complication icon so that I experience an unexpected, delightful surprise within the application. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_ee_day.png "watch-o-tron user story day easter egg") |
| As a curious site user, I can discover a hidden Easter egg in the moon phase complication icon so that I experience an unexpected, delightful surprise within the application. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_ee_moonphase.png "watch-o-tron user story moonphase easter egg") |
| As a client, I can log in as a staff member so that I can add potential new, important options for users. | ![screeshot](documentation/features/accounts/wot_feature_accounts_staff_logged_in_desktop.png "watch-o-tron user story staff login") |
| As a site staff member, I can add new watch movement types to the model so that users can add watches with any new movement types that may become available in the future. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_add_movement.png "watch-o-tron user story add movement") |
| As a site staff member, I can add new list types so that users can expand their lists from collection and wish list to other types specified by the site staff member. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_add_list.png "watch-o-tron user story add list") |
| As a site staff member, I can edit any movement types I have added so that I can change them if needed. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_edit_movement.png "watch-o-tron user story edit movement") |
| As a site staff member, I can delete any new movement types so that I can keep the list relevant. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_delete_movement.png "watch-o-tron user story delete movement") |
| As a site staff member, I can edit any added list types so that I keep the app up to date. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_edit_list.png "watch-o-tron user story edit list") |
| As a site staff member, I can delete custom added lists so that I can remove any unwanted list types. | ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_delete_list.png "watch-o-tron user story delete list") |
| As a staff member, I am notified about edits and deletes I make for custom movements so that I know if the change was successful. | ![screeshot](documentation/features/messaging/wot_feature_comms_message_confirm_edit_staff_item.png "watch-o-tron user story messages edit movement") ![screeshot](documentation/features/messaging/wot_feature_comms_message_confirm_delete_staff_item.png "watch-o-tron user story messages delete movement") |
| As a staff member, I am notified of successful list edits and deletions so that I know the process was successful. | ![screeshot](documentation/features/messaging/wot_feature_comms_message_confirm_edit_staff_item.png "watch-o-tron user story messages edit list") ![screeshot](documentation/testing/user_story_extras/wot_testing_user_story_delete_list_message.png "watch-o-tron user story messages delete list") |
| As a site admin, I can log in as a super user so that I can access the admin panel. | ![screeshot](documentation/features/accounts/wot_feature_accounts_admin_logged_in_desktop.png "watch-o-tron user story super user login") |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

`pip3 install coverage`

`pip3 freeze --local > requirements.txt`

`coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/tests/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/tests/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/tests/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/tests/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/tests/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/tests/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/tests/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/tests/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/tests/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/tests/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/apeskinian/p4_watch-o-tron/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Aapeskinian%2Fp4_watch-o-tron%20label%3Abug&label=bugs)](https://github.com/apeskinian/p4_watch-o-tron/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/apeskinian/p4_watch-o-tron/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/apeskinian/p4_watch-o-tron/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/apeskinian/p4_watch-o-tron/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/apeskinian/p4_watch-o-tron/issues/3) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/apeskinian/p4_watch-o-tron)](https://github.com/apeskinian/p4_watch-o-tron/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/apeskinian/p4_watch-o-tron)](https://github.com/apeskinian/p4_watch-o-tron/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/apeskinian/p4_watch-o-tron/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/apeskinian/p4_watch-o-tron/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/apeskinian/p4_watch-o-tron/issues/5) | Open |

## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.
